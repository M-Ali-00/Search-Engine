def chunk_text(text, max_words=150):
    words = text.split()
    chunks = []

    for i in range(0,len(words),max_words):
        chunk = " ".join(words[i:i +max_words])
        chunks.append(chunk)
    return chunks