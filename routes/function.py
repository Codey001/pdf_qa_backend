from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


class TestData(BaseModel):
    filename: str
    question: str


API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_NAME = os.getenv("MODEL_NAME")

genai.configure(api_key=API_KEY)
model_name = MODEL_NAME


def call_genai_api(context: str, question: str) -> str:
    # GEMINI RESPONSE CALL
    model = genai.GenerativeModel(model_name)
    text_response = []
    response = model.generate_content(f"{context}\n\nQ: {question}\nA:", stream=True)

    for chunk in response:
        text_response.append(chunk.text)

    return response.text
