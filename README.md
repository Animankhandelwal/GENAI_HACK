# 🚀 GENAI_HACK - Learning Path Chatbot  

> **An AI-powered chatbot that delivers personalized learning recommendations based on user inputs.**  
> Built using **FastAPI, OpenAI GPT, Pinecone vector search, WebSockets, and PostgreSQL** for **real-time, intelligent learning guidance**.

---

## 📌 **Features**  

✅ **Real-time chat** via WebSockets  
✅ **Personalized learning recommendations** using **LLMs & Pinecone**  
✅ **FastAPI backend** for high-performance API handling  
✅ **PostgreSQL for structured user data storage**  
✅ **Secure API key management using `.env`**  

---

## 🛠 **Tech Stack**  

| **Technology**  | **Purpose** |
|---------------|------------|
| **FastAPI** | Web framework for backend APIs |
| **OpenAI API** | AI-powered chatbot responses |
| **Pinecone** | Vector search for learning recommendations |
| **PostgreSQL** | Database for storing user data |
| **WebSockets** | Real-time chat functionality |
| **Uvicorn** | ASGI server for FastAPI |

---

## 📂 **Project Structure**  


📂 learning-path-chatbot
│── 📂 database        # PostgreSQL schema
│── 📂 models          # ML models and embeddings
│── 📂 api             # FastAPI routes and WebSocket
│── 📂 scripts         # Utility scripts (populate Pinecone, DB setup)
│── .env.example       # Sample .env file
│── main.py            # FastAPI entry point
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation

---

## 🚀 **Installation & Setup**

1️⃣ Clone the Repository

2️⃣ Set Up Python Virtual Environment

3️⃣ Install Dependencies

4️⃣ Set Up PostgreSQL Database

5️⃣ Configure Environment Variables

6️⃣ Populate Pinecone with Learning Data

---

### 💡 **Running the Chatbot**

Start FastAPI Server

uvicorn main:app --reload

API runs at http://localhost:8000

WebSocket available at ws://localhost:8000/ws

## 📝 **Usage**

 WebSocket Chat Example
 
import websockets

import asyncio

import json

async def chat():

    uri = "ws://localhost:8000/ws"
    
    async with websockets.connect(uri) as websocket:
    
        await websocket.send("I want to learn deep learning")

        response = await websocket.recv()
        
        print("Chatbot response:", json.loads(response))

asyncio.run(chat())



