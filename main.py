from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.messages import HumanMessage, SystemMessage

load_dotenv()

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    user_id: str

llm = init_chat_model("google_genai:gemini-2.5-flash-lite")

system_msg = SystemMessage(
    content="""
You are an AI assistant.
Remember user information from previous messages.
If user tells their name, store it and use it later.
Use weather tool when needed.
"""
)

user_sessions = {}

from langchain.tools import tool

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


@tool
def weather(city: str) -> str:
    """Get current weather of a city"""
    return f"The weather in {city} is sunny ☀️"

tools = [calculator, geo_info, weather]

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
        if req.user_id not in user_sessions:
            user_sessions[req.user_id] = []

        chat_history = user_sessions[req.user_id]

        chat_history.append(HumanMessage(content=req.message))

        response = agent.invoke({
            "messages": [system_msg] + chat_history
        })

        ai_msg = response["messages"][-1]

        chat_history.append(ai_msg)

        return {"response": ai_msg.content}

    except Exception as e:
        return {"error": str(e)}