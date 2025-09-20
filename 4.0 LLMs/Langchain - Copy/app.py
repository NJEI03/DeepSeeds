from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return{
        "data":"Hello buddy"
    }

@app.get("/sentiment")
def sentiment_analysis():
    # After doing sentiment analysis logic
    return{
        "sentiment": "positive",
        "sentiment-score": "0.7",
        "model": "vader-en"
    }

@app.get("summary")
def text_summarization():
    # After doing text summary logic
    return{

        "summary": "This is a sample summary",
    }


#Create an endpoint that returna information about a user
@app.get('/me')
def me():
    return{
        "name": "JJ",
        "age": "22",
        "location": "Canada",
        "Ocupation": "AI Engineer",
        "Know-how": {
            "skills": ["Python", "Machine Learning", "Deep Learning", "NLP"]
        }
    }

## Path parameters
@app.get("/sentiments/{text}")
def sentiment_analizer(text):
    text=input("Enter your text")
    if text.lower() in ["good", "happy", "great", "awesome", "love"]:
        return{
            "sentiment": "positive",
            "score":"0.8",
            "model":"bert-base",
            
        }
        
    
    return{
        "sentiment": "negative",
        "score":"-0.6",
        "model":"bert-base"
    }

#Exercise: Take a prompt from the user, pass it as a parmeter to your endpoint, also pass it to your llm model and return in json the user prompt and the llm response
# Hint: Use path parameters

#Question : is it possible to get user input from fastapi on the browser?
from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv, find_dotenv

def environement_variables():
    load_dotenv(find_dotenv())  
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def load_google_llm():
    # loading our keys
    environement_variables()
    google_llm = GoogleGenerativeAI(
        # pass our configurations here
        model="gemini-2.5-flash", 
        temperature=0.7
        )
    return google_llm
llm = load_google_llm()
@app.get("/chat/{user_prompt}")
def chat(user_prompt):
    llm_response = llm(user_prompt)
    return{
        "user_prompt": user_prompt,
        "llm_response": llm_response

    }
