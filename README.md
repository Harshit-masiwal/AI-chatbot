# 🤖 AI Chatbot using FastAPI + LangChain + Streamlit
# This is just a demo project.

## 📌 Project Overview

This project is a smart AI chatbot built using FastAPI and LangChain with a Streamlit frontend.

It can handle:

* 💬 General conversation
* 🔢 Mathematical calculations
* 🌍 Basic geographical queries

---

## 🛠️ Tech Stack

* FastAPI (Backend API)
* LangChain (LLM + Tools)
* Google Gemini API
* SymPy (Math calculations)
* Streamlit (Frontend UI)
* uv (Python package manager)

---

## Create a .env file and add your API key.

## 🌐 Live Demo (Frontend)

streamlit_url

```
  Local URL: http://localhost:8501
  Network URL: http://192.168.1.73:8501
```

---

## 📁 Project Structure

```id="struct12"
New/
├── main.py          # FastAPI backend
├── frontend.py           # Streamlit frontend
├── requirements.txt
├── README.md
```

---

## Setup 

### 1. Install dependencies

```bash id="cmd1"
uv pip install -r requirements.txt
```

### 2. Create `.env` file

```id="env1"
GOOGLE_API_KEY=your_api_key_here
```

---

## 🌐 Live Backend

FastAPI backend deployed on Render:

👉 https://ai-chatbot-ldjt.onrender.com

# 🤖 AI Chatbot (Streamlit Frontend)

This is the frontend of an AI-powered chatbot built using **Streamlit**.  
It connects to a FastAPI backend deployed on Render and uses Google Gemini via LangChain.

---

## 🌐 Live Demo

👉 Frontend (Streamlit):  
https://ai-chatbot-2wjmrraec3zewjwgukze9c.streamlit.app/

👉 Backend (FastAPI):  
https://ai-chatbot-ldjt.onrender.com

## 🌐 API Testing

Swagger UI:

```id="url4"
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Input

```json id="json1"
{
  "message": "2+5*10"
}
```

---

## ✅ Features

* AI-powered chatbot
* Math solving using SymPy
* Tool-based architecture (LangChain)
* FastAPI backend API
* Interactive Streamlit UI

---

## ⚠️ Notes

* `.venv` is excluded from project
* Add your API key in `.env`


---

## 🚀 Future Improvements

*  will Add real maps API 🌍
*  will Add chat memory 🧠
*  will Improve UI design
*  will Add file upload (PDF chatbot)

---

## 👨‍💻 Author

Harshit Masiwal
# AI-chatbot
