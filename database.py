import chromadb
from embedder import embed_text

client = chromadb.PersistentClient(path="vectordb")

collection = client.get_or_create_collection(name="pages")

def add_chunk(text, url, title):
    vector = embed_text(text)

    collection.add(
        documents=[text],
        embeddings=[vector],
        metadatas=[{"url": url, "title": title}],
        ids=[f"{url}_{hash(text)}"]
    )
    print(f"✅ [Brain] Ingested chunk from: {title} ({url})")
    
