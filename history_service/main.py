from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGODB_URI"))
db = client.chat_db

app = FastAPI()

class HistoryItem(BaseModel):
    chat_id: str
    user: str
    agent: str

@app.post("/history")
def save_history(item: HistoryItem):
    db.history.insert_one(item.dict())
    return {"status": "saved"}

@app.get("/history/{chat_id}")
def get_history(chat_id: str):
    history = list(db.history.find({"chat_id": chat_id}, {"_id": 0}))
    return {"history": history}
