from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.agents import create_agent

load_dotenv()

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

llm = init_chat_model("google_genai:gemini-2.5-flash-lite")


@tool
def calculator(expression: str) -> str:
    """Solve mathematical expressions like 2+2, 5*10"""
    import sympy as sp
    try:
        result = sp.sympify(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def geo_info(place: str) -> str:
    """Get basic information about a place"""
    return f"{place} is a place on Earth 🌍"


tools = [calculator, geo_info]

agent = create_agent(
    model=llm,
    tools=tools
)


@app.get("/")
async def home():
    return {"message": "Server is running 🚀"}


@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = llm.invoke(req.message)
        return {"response": response.content}
    except Exception as e:
        return {"error": str(e)}