@echo off
echo Starting all AI Agent microservices + ChromaDB...

:: Activate virtual environment
cd /d D:\work\chatbot\ai_agent_mvp
call .\venv\Scripts\activate.bat

:: Start Chroma DB
start cmd /k "cd /d D:\work\chatbot\ai_agent_mvp && chroma run --path ./chroma_data"

:: Run ingest.py
cd /d D:\work\chatbot\ai_agent_mvp\knowledge_base_service
python ingest.py

:: Start Knowledge Base Service
start cmd /k "cd /d D:\work\chatbot\ai_agent_mvp\knowledge_base_service && uvicorn main:app --port 8002 --reload"

:: Start Search Service
start cmd /k "cd /d D:\work\chatbot\ai_agent_mvp\search_service && uvicorn main:app --port 8004 --reload"

:: Start History Service
start cmd /k "cd /d D:\work\chatbot\ai_agent_mvp\history_service && uvicorn main:app --port 8003 --reload"

:: Start Chat Service
start cmd /k "cd /d D:\work\chatbot\ai_agent_mvp\chat_service && uvicorn main:app --port 8001 --reload"

echo All services and ChromaDB are starting...
:: pause

start http://localhost:8001/docs

