import re
from sentence_transformers import SentenceTransformer

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text.strip()

def smart_chunk(text, size=60, stride=30):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words) - size + 1, stride)]

def load_model(path):
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(path)
