from chunker import chunk_text
from database import add_chunk

def ingest_page(page_json):
    if not isinstance(page_json, dict):
        raise ValueError("Input must be a dictionary")
    
    required_keys = {"url","title","text"}
    if not required_keys.issubset(page_json.keys()):
        raise ValueError("Missing required keys")
    
    url = page_json["url"]
    title = page_json["title"]
    text = page_json["text"]

    chunks = chunk_text(text)

    for chunk in chunks:
        add_chunk(chunk, url, title)