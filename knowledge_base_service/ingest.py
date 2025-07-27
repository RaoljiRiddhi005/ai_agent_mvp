import chromadb
import os

client = chromadb.HttpClient(host="localhost", port=8000)
collection = client.get_or_create_collection("knowledge_base")

data_folder = "./data"
for filename in os.listdir(data_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(data_folder, filename), "r", encoding="utf-8") as f:
            text = f.read()
            collection.add(documents=[text], ids=[filename])
print("✅ Documents added to ChromaDB.")
