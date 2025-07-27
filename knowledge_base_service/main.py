from fastapi import FastAPI
from pydantic import BaseModel
import chromadb

app = FastAPI()
client = chromadb.HttpClient(host="localhost", port=8000)
collection = client.get_or_create_collection(name="knowledge_base")

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_kb(request: QueryRequest):
    result = collection.query(
        query_texts=[request.query],
        n_results=3,
        include=["distances", "documents"]
    )

    # Threshold filtering for relevance
    THRESHOLD = 0.4
    docs = [
        doc for doc, dist in zip(result["documents"][0], result["distances"][0])
        if dist <= THRESHOLD
    ]

    if not docs:
        return {"answer": None}
    
    return {"answer": docs[0]}  # return top relevant answer
