- AI Agent MVP :
    A microservices-based AI agent app built with FastAPI, MongoDB, ChromaDB, and OpenAI API.  
    Supports querying a knowledge base, chat history, and web search using DuckDuckGo.


-----------------------------------------------------------------------------------------------------------------
- Technologies Used :
    FastAPI - Web framework for APIs
    MongoDB - Database for storing chat history
    ChromaDB - Embedding-based vector search
    OpenAI API - Generates responses
    DuckDuckGo Search - External knowledge
    python-dotenv - Manage environment variables

- Services Overview :
    chat_service -            Handles chat flow & orchestrates services (not fully wired in .bat yet)
    knowledge_base_service -  Stores and retrieves knowledge using ChromaDB.
    search_service -          Performs real-time web search.
    history_service -         Stores conversation history using MongoDB.
    start_all_services.bat -  Windows batch script to run the entire system easily.

- API Endpoints :
  Each microservice provides its own Swagger documentation:
    Knowledge Base: http://localhost:8002/docs
    Search Service: http://localhost:8004/docs
    History Service: http://localhost:8003/docs
    Chat Service: http://localhost:8001/docs


-----------------------------------------------------------------------------------------------------------------
1. Install dependencies (in bash)
   pip install -r requirements.txt

2. Run all services with one command (in bash)
   start_all_services.bat

    This .bat file will:
      - Activate the virtual environment
      - Start ChromaDB with local data path
      - Run ingest.py to populate the knowledge base
      - start the following services on separate ports:
          - Knowledge Base Service (8002)
          - Search Service (8004)
          - History Service (8003)
          - chat Service (8001)


-----------------------------------------------------------------------------------------------------------------
--> Chat Service (Ask Questions)
1. Open: http://localhost:8001/docs
   or
   run: start_all_services.bat (automatically open chat services)
2. Click on POST /chat
3. Click "Try it out"
4. Input example:(enter chat_id, query)
     {
        "chat_id": "user1",
        "query": "what is fastapi"
      }
5. Click "Execute"
6. Scroll down to see the response in the Response body section.


--> History Service (Ask Questions)
1. Open: http://localhost:8003/docs
   or
   run: start_all_services.bat (automatically open chat services)
2. Click on GET /history/{chat_id}
3. Click "Try it out"
4. Enter chat_id,
    e.g.: user1
5. Click "Execute"
6. You’ll see all previous queries made by that user in the response.


-----------------------------------------------------------------------------------------------------------------
--> Folder Structure :
ai_agent_mvp/
│
├── chat_service/
│ └── main.py
│
├── history_service/
│ └── main.py
│
├── knowledge_base_service/
│ ├── data/
│ ├── ingest.py
│ └── main.py
│
├── search_service/
│ └── main.py
│
├── chroma_data/
│ └── chroma.sqlite3
│
├── .env
├── requirements.txt
├── start_all_services.bat















## 🧰 Technologies Used
- FastAPI
- Uvicorn
- MongoDB (`pymongo`)
- ChromaDB
- OpenAI API
- DuckDuckGo Search API
- Python Dotenv

---

## 📦 Setup

### 1. Clone the Repo
```bash
git clone https://github.com/RaolijiRiddhi005/ai_agent_mvp.git
cd ai_agent_mvp
