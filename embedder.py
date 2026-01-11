from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
def embed_text(text:str):
    if not isinstance(text,str):
        raise ValueError("Text must be a string")
    return model.encode(text).tolist()