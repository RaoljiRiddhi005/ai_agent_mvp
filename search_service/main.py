from fastapi import FastAPI
from duckduckgo_search import DDGS

app = FastAPI()

@app.get("/search")
def search(query: str):
    if not query.strip():
        return {"answer": "Please enter a valid question."}

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        for res in results:
            if "body" in res and res["body"].strip():
                return {"answer": res["body"]}

    return {"answer": "I couldn't find a relevant answer. Please refine your question."}
