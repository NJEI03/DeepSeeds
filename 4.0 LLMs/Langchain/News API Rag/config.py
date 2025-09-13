# API key loader
import os
from dotenv import load_dotenv, find_dotenv
import requests
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pprint import pprint
def environement_variables():
    load_dotenv(find_dotenv())
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    return NEWS_API_KEY, GOOGLE_API_KEY
environement_variables()
#Testing pasic API connection with request.get
# response = requests.get(f' https://newsdata.io/api/1/latest?apikey=pub_6c3454b336d04db1aae68d20c08b3a02&q=pizza')
# print(response.status_code)
# print(response.json())
class NewsAPILoader:
    def __init__(self, query, api_key):
        # initialize properties
        self.query = query
        self.api_key = api_key

    # Create method that loads the data live

    def load(self):
        # pass info to url; city and api key
        url = f"https://newsdata.io/api/1/news?country=us&language=en&q={self.query}&apikey={self.api_key}&size=3"
        # Make request and store in response
        # JSON==Dictionary in Python
        response = requests.get(url).json()
        return response
# load = NewsAPILoader(query="general", api_key=os.getenv("NEWS_API_KEY")).load()
# pprint(load) 
#Creating an instance of the class

def newsContext(query):
    # Initialize or create an instance of the class
    environement_variables()
    newsData = NewsAPILoader(query=query, api_key=os.getenv("NEWS_API_KEY"))
    response = newsData.load()
    return response


#Function to load embeddings
def load_embeddings():
    environement_variables()
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    # Test with sample text
    # sample_text = ["Hello, world!", "This is a test."]
    # embedded_docs = embeddings.embed_documents(sample_text)
    

###Step 3: AI Enhancement Pipeline (30 minutes)
# Create AI enhancement for each news article: - Use your existing
# PromptTemplate pattern - Create prompts that take news article and
# generate: - AI summary (2 sentences max) - Sentiment analysis (positive/
# negative/neutral) - Key topics extraction (3-5 topics) - Credibility assessment
# (brief explanation)
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
def load_google_llm():
    environement_variables()
    google_llm = GoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7
    )
    return google_llm

def load_google_chat_model():
    environement_variables()
    google_chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    return google_chat


