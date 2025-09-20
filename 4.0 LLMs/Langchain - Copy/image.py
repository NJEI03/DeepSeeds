from fastapi import FastAPI,File, UploadFile, HTTPException
from  day2.config import load_google_chat_model
import base64

llm=load_google_chat_model()
app = FastAPI()

@app.post("/post-image")
async def process_image(file:UploadFile=File(...)):
    try:
        #get image and convert into bytes
        image_bytes = await file.read()
        #Cpu is going tp be idle
        image_base_64 = base64.b64encode(image_bytes).decode('UTF-8')
        format_image = f"data:image/jpeg;base64,{image_base_64}"

        #pass image llm
        prompt = f"""
        Given the image :{format_image}, please analyze doing it step by step and let us know what iside the image
        """
        response=llm.invoke(prompt)
        return{
            "response": response.content,
            "file":file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail= "An error occurred while processing the image")
