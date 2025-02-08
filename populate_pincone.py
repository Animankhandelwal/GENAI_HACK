import pinecone
import openai
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINCONE_API")

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment="us-west1-gcp")
index = pinecone.Index("learning-bot")

# Sample courses
courses = [
    {"name": "Deep Learning with PyTorch", "description": "Learn PyTorch and deep learning techniques."},
    {"name": "Machine Learning Fundamentals", "description": "Intro to ML with Python."},
    {"name": "AI Ethics", "description": "Understand AI's impact on society."},
]

# Store courses in Pinecone
for course in courses:
    embedding = openai.Embedding.create(
        input=course["description"], model="text-embedding-ada-002"
    )["data"][0]["embedding"]

    index.upsert(vectors=[(course["name"], embedding, {"course_name": course["name"]})])

print("Courses successfully added to Pinecone!")
