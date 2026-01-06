import chromadb
from embedder import embed_text

client= chromadb.PersistentClient(path="vectordb")
collection=client.get_collection(name="pages")

def search(query, n_results=3):
    query_vector = embed_text(query)

    results=collection.query(query_embeddings=[query_vector], n_results=n_results)

    return results