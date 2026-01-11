import chromadb
from embedder import embed_text

client= chromadb.PersistentClient(path="vectordb")
collection=client.get_collection(name="pages")

<<<<<<< HEAD
def search(query, n_results=6):
=======
def search(query, n_results=3):
>>>>>>> ca00f169f30fc7164a26e861c02ad8877907a83d
    print(f"🔍 [Brain] Searching for: '{query}'...")
    query_vector = embed_text(query)

    results=collection.query(query_embeddings=[query_vector], n_results=n_results)
    return results
