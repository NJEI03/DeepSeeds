

# Create AI enhancement for each news article: - Use your existing
# PromptTemplate pattern - Create prompts that take news article and
# generate: - AI summary (2 sentences max) - Sentiment analysis (positive/
# negative/neutral) - Key topics extraction (3-5 topics) - Credibility assessment
# (brief explanation) based on the news gotten from the newdataapi in our config.py file
# the idea is to tale a news context param from the user like ports politics and let them ask questions then you use the news context to get relevant news articles
# then you use the articles to answer the questions asked by the user by giviing a summary sentiment analysis key topics and credibility assessment
# Finally, display the enhanced news articles with the original articles in a readable format.

# chat_prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are an {expert} in {domain}, please break down any  questions the user is going to ask you in a clear and concisise manner with real world analogies"),
#     ("user", "Please {expert} help me with my questions"),  
#     ("ai", "Sure {name}, I can do just that"),
#     ("user", "{user_input}")            
# ])
# def prompt_template(expert, domain, name, user_input):
#     prompt = chat_prompt.format_messages(
#         expert=expert,
#         domain=domain,
#         name=name,
#         user_input=user_input
#     )
#     return prompt
# #Function to get news based on user query
# def get_news(query):
#     news_response = newsContext(query)
#     articles = news_response.get("results", [])
#     return articles 
# #Function to enhance news articles using AI
# def enhance_news(articles, user_question):
#     enhanced_articles = []
#     for article in articles:
#         title = article.get("title", "No Title")
#         description = article.get("description", "No Description")
#         content = article.get("content", "No Content")
#         full_text = f"Title: {title}\nDescription: {description}\nContent: {content}"
        
#         prompt = prompt_template(
#             expert="News Analyst",
#             domain="Journalism and Media",
#             name="Mben",
#             user_input=f"Based on the following news article, please provide a brief summary, sentiment analysis, key topics, and credibility assessment. Article: {full_text} Question: {user_question}"
#         )
        
#         response_parts = []
#         for part in chat_model.stream(prompt):
#             response_parts.append(part.content)
#         enhanced_response = ''.join(response_parts)
        
#         enhanced_articles.append({
#             "original_article": article,
#             "enhanced_response": enhanced_response
#         })
#     return enhanced_articles
# #Function to display enhanced news articles
# def display_enhanced_news(enhanced_articles):
#     for idx, item in enumerate(enhanced_articles):
#         original = item["original_article"]
#         enhanced = item["enhanced_response"]
        
#         print(f"\nArticle {idx + 1}:")
#         print(f"Title: {original.get('title', 'No Title')}")
#         print(f"Description: {original.get('description', 'No Description')}")
#         print(f"Content: {original.get('content', 'No Content')}")
#         print("\nEnhanced Analysis:")
#         print(enhanced)
#         print("-" * 80)
# #Main function to run the pipeline
# def main():
#     load_dotenv(find_dotenv())
#     user_query = input("Enter a news topic (e.g., sports, politics, technology): ")
#     user_question = input("What would you like to know about this topic? ")
    
#     print("\nFetching news articles...")
#     articles = get_news(user_query)
    
#     if not articles:
#         print("No articles found for the given topic.")
#         return
    
#     print(f"Found {len(articles)} articles. Enhancing with AI...")
#     enhanced_articles = enhance_news(articles, user_question)
    
#     print("\nDisplaying enhanced news articles:")
#     display_enhanced_news(enhanced_articles)
# if __name__ == "__main__":
#     main()

# #what to do to display the both the enhanced and original articles in a json format
# you can use the pprint module to display the articles in a readable format


#Seeting chat template 
from streamlit import json
from config import load_google_chat_model
chat_model = load_google_chat_model()
from langchain_core.prompts import ChatPromptTemplate
from config import newsContext, load_embeddings
from dotenv import load_dotenv, find_dotenv
import os
from pprint import pprint
# Create AI enhancement for each news article: - Use your existing
# PromptTemplate pattern - Create prompts that take news article and
# generate: - AI summary (2 sentences max) - Sentiment analysis (positive/
# negative/neutral) - Key topics extraction (3-5 topics) - Credibility assessment
# (brief explanation) based on the news gotten from the newdataapi in our config.py file
# the idea is to tale a news context param from the user like ports politics and let them ask questions then you use the news context to get relevant news articles
# then you use the articles to answer the questions asked by the user by giviing a summary sentiment analysis key topics and credibility assessment, no complexity because I am learning to implement RAG. We can do this with the help of pydantic models in less than 30  lines of code
from pydantic import BaseModel
class NewsArticle(BaseModel):
    title: str
    description: str
    content: str
class EnhancedNewsArticle(BaseModel):
    original_article: NewsArticle
    ai_summary: str
    sentiment_analysis: str
    key_topics: list[str]
    credibility_assessment: str
def enhance_news_article(article, user_question):           
    full_text = f"Title: {article.title}\nDescription: {article.description}\nContent: {article.content}"
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an {expert} in {domain}, please break down any  questions the user is going to ask you in a clear and concisise manner with real world analogies"),
        ("user", "Please {expert} help me with my questions"),  
        ("ai", "Sure {name}, I can do just that"),
        ("user", "{user_input}")            
    ])
    prompt = chat_prompt.format_messages(
        expert="News Analyst",
        domain="Journalism and Media",
        name="Mben",
        user_input=f"Based on the following news article, please provide a brief summary, sentiment analysis, key topics, and credibility assessment. Article: {full_text} Question: {user_question}"
    )
    response_parts = []
    for part in chat_model.stream(prompt):
        response_parts.append(part.content)
    enhanced_response = ''.join(response_parts)
    # For simplicity, let's assume the enhanced_response is structured as follows:
    # Summary: <summary>\nSentiment: <sentiment>\nTopics: <topic1>, <topic2>, ...\nCredibility: <assessment>
    try:
        summary_part, sentiment_part, topics_part, credibility_part = enhanced_response.split('\n')
        ai_summary = summary_part.replace("Summary: ", "").strip()
        sentiment_analysis = sentiment_part.replace("Sentiment: ", "").strip()
        key_topics = [topic.strip() for topic in topics_part.replace("Topics: ", "").split(',')]
        credibility_assessment = credibility_part.replace("Credibility: ", "").strip()
    except ValueError:
        ai_summary = "N/A"
        sentiment_analysis = "N/A"
        key_topics = []
        credibility_assessment = "N/A"
    return EnhancedNewsArticle(
        original_article=article,
        ai_summary=ai_summary,
        sentiment_analysis=sentiment_analysis,
        key_topics=key_topics,
        credibility_assessment=credibility_assessment
    )
def main():
    load_dotenv(find_dotenv())
    user_query = input("Enter a news topic (e.g., sports, politics, technology): ")
    user_question = input("What would you like to know about this topic? ")
    print("\nFetching news articles...")
    news_response = newsContext(user_query)
    articles_data = news_response.get("results", [])
    articles = [NewsArticle(
        title=art.get("title", "No Title"),
        description=art.get("description", "No Description"),
        content=art.get("content", "No Content")
    ) for art in articles_data]
    if not articles:
        print("No articles found for the given topic.")
        return
    print(f"Found {len(articles)} articles. Enhancing with AI...")
    enhanced_articles = [enhance_news_article(article, user_question) for article in articles]
    print("\nDisplaying enhanced news articles:")
    for idx, enhanced in enumerate(enhanced_articles):
        print(f"\nArticle {idx + 1}:")
        pprint(enhanced.dict())
        print("-" * 80)

if __name__ == "__main__":
    main()

# #what to do to display the both the enhanced and original articles in a json format