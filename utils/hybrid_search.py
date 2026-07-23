from collections import OrderedDict

from utils.bm25 import bm25
from utils.vectordb import similarity_search


def hybrid_search(
    query,
    selected_document=None,
    vector_k=6,
    bm25_k=6,
    final_k=8
):
    """
    Hybrid Retrieval

    1. Semantic Search (Chroma)
    2. Keyword Search (BM25)
    3. Merge
    4. Remove duplicates
    5. Return top chunks
    """

    # -----------------------------------
    # Vector Search
    # -----------------------------------

    vector_docs = similarity_search(
        query=query,
        selected_document=selected_document,
        k=vector_k
    )

    # -----------------------------------
    # BM25 Search
    # -----------------------------------

    bm25.build_index(selected_document)

    keyword_docs = bm25.search(
        query,
        top_k=bm25_k
    )

    # -----------------------------------
    # Merge Results
    # -----------------------------------

    merged = vector_docs + keyword_docs

    unique = OrderedDict()

    for doc in merged:

        key = (

            doc.metadata.get("source"),

            doc.metadata.get("page"),

            doc.metadata.get("chunk_id")

        )

        if key not in unique:

            unique[key] = doc

    return list(unique.values())[:final_k]