from fastapi import FastAPI, WebSocket, Depends
import openai
import pinecone
import psycopg2
import json
import os
from dotenv import load_dotenv

# Load API keys from environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("")
PINECONE_API_KEY = os.getenv("PINCONE_API")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "chatbot_db")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

# Initialize FastAPI app
app = FastAPI()

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment="us-west1-gcp")
index = pinecone.Index("learning-bot")

# Connect to PostgreSQL
def get_db_connection():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port="5432")

# WebSocket for real-time chat
@app.websocket("/ws")
async def chat(websocket: WebSocket):
    await websocket.accept()
    
    while True:
        user_input = await websocket.receive_text()

        # Convert input to vector
        query_embedding = openai.Embedding.create(
            input=user_input,
            model="text-embedding-ada-002"
        )["data"][0]["embedding"]

        # Search Pinecone for similar courses
        results = index.query(vector=query_embedding, top_k=3, include_metadata=True)
        recommendations = [{"course_name": match["metadata"]["course_name"]} for match in results["matches"]]

        # Store user query and recommendation in PostgreSQL
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO recommendations (course_name) VALUES (%s)", (recommendations[0]["course_name"],))
        conn.commit()
        cur.close()
        conn.close()

        # Send recommendations to frontend
        await websocket.send_text(json.dumps({"recommendations": recommendations}))

# REST API to get user recommendations
@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT course_name FROM recommendations WHERE user_id = %s", (user_id,))
    recommendations = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return {"user_id": user_id, "recommendations": recommendations}
