from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_search(query: str, docs: list[str], max_results=10) -> list[float]:
    query_embeddings = model.encode(query)
    doc_embeddings = model.encode(docs)
    similarities = model.similarity(query_embeddings, doc_embeddings)
    result_idx = similarities[0].argsort(descending=True)[0:max_results]
    results = [docs[i] for i in result_idx]
    return results, result_idx