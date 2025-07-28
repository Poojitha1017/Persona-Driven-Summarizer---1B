import numpy as np

def find_top_k_sections(model, query, chunks, k=7):
    query_embedding = model.encode(f"query: {query}", convert_to_numpy=True, normalize_embeddings=True)
    chunk_texts = [f"passage: {text}" for _, _, text in chunks]
    chunk_embeddings = model.encode(chunk_texts, convert_to_numpy=True, normalize_embeddings=True)

    scores = np.dot(chunk_embeddings, query_embedding)
    top_indices = np.argsort(scores)[::-1][:k]

    top_sections = []
    for rank, idx in enumerate(top_indices, 1):
        doc, page, text = chunks[idx]
        top_sections.append({
            "document": doc,
            "importance_rank": rank,
            "section_title": text[:80] + ("..." if len(text) > 80 else ""),
            "refined_text": text,
            "page_number": page
        })
    return top_sections
