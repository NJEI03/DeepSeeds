from transformers import pipeline
from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel
from fastapi import Body
app = FastAPI()



@app.get("/search-product")
def search(  page:int, id:int, category:Optional[str]=None):
    return{
        "category":category,
        "page":page,
        "id":id
    }

# Dictionary of data

data = {
    1:{
        "name":"Desktop",
        "price":"5000XAF",
        "data_posted":"2024-10-10"
    },
    2:{
        "name":"Laptop",
        "price":"3000XAF",
        "data_posted":"2024-09-10"
    },
    3:{
        "name":"Tablet",
        "price":"2000XAF",
        "data_posted":"2024-08-10"
    }
}

@app.get("/get-product/")
def get_product(id:int):
    if id in data:
        filtered_data=data[id]
        return filtered_data
    return{
        "error":"Product not found"
    }

class UserData(BaseModel):
    name:str
    age:int
    city:str
    occupation:Optional[str]=None
    isMarried:Optional[bool]=None

## Request body
@app.post("/post")
def posting(request:dict=UserData):
    return{
      "Info": request
          }      

class AIData(BaseModel):
    model_name:str
    model_id: int
    prompt: str

@app.get("/ai-model")
def ai_model(request:dict=AIData):
    