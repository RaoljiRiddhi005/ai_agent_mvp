from fastapi import FastAPI
from pydantic import BaseModel
import requests
from uuid import uuid4

app = FastAPI()

class ChatRequest(BaseModel):
    chat_id: str = None
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    chat_id = req.chat_id or str(uuid4())
    message = req.message

    # Step 1: Try Knowledge Base
    kb_res = requests.post("http://localhost:8002/query", json={"query": message})
    answer = ""

    if kb_res.ok:
        kb_data = kb_res.json()
        docs = kb_data.get("results", {}).get("documents", [[]])[0]
        if docs:
            answer = docs[0]  # pick the top match from ChromaDB

    # Step 2: Fallback to Search if no KB match
    if not answer.strip():
        search_res = requests.get("http://localhost:8004/search", params={"query": message})
        answer = search_res.json().get("answer", "Sorry, I couldn't find an answer.")

    # Step 3: Save to History
    requests.post("http://localhost:8003/history", json={
        "chat_id": chat_id,
        "user": message,
        "agent": answer
    })

    return {"chat_id": chat_id, "answer": answer}

@app.get("/chat/{chat_id}")
def get_history(chat_id: str):
    res = requests.get(f"http://localhost:8003/history/{chat_id}")
    return res.json()
