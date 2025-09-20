from fastapi import FastAPI
from  day2.config import load_google_llm
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

    return google_llm
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

import os
from dotenv import load_dotenv, find_dotenv

def environement_variables():
    load_dotenv(find_dotenv())  
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = load_google_llm()
@app.get("/chat/{user_prompt}")
def chat(user_prompt):
    llm_response = llm(user_prompt)
    return{
        "user_prompt": user_prompt,
        "llm_response": llm_response

    }
@app.get("/get-config/{temp}")
def get_config(temp:float):
    if temp < 0 or temp >1:
        print('Temperature must be between 0  and 1')
        return{
            "error": "Temperature must be between 0 and 1"
        }
    return{
        "temperature":temp
    }
