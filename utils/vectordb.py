import os

os.environ["ANONYMIZED_TELEMETRY"] = "False"

from langchain_chroma import Chroma

from utils.embeddings import get_embedding_model
from chromadb.config import Settings

settings = Settings(
    anonymized_telemetry=False
)

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "research_documents"


def get_vector_db():
    """
    Load the existing Chroma database or create it if it doesn't exist.
    """

    embedding = get_embedding_model()

    db = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_PATH,
        embedding_function=embedding,
    )

    return db

def get_all_documents(selected_document=None):
    """
    Retrieve all stored documents from Chroma.

    This is used by BM25 indexing and Hybrid Search.
    """

    db = get_vector_db()

    if selected_document is None:

        results = db._collection.get(
            include=["documents", "metadatas"]
        )

    else:

        results = db._collection.get(
            where={
                "source": selected_document
            },
            include=["documents", "metadatas"]
        )

    from langchain_core.documents import Document

    documents = []

    docs = results.get("documents", [])
    metas = results.get("metadatas", [])

    for text, metadata in zip(docs, metas):

        documents.append(

            Document(

                page_content=text,

                metadata=metadata

            )

        )

    return documents


def create_vector_db(chunks):
    """
    Add new document chunks to the existing Chroma collection.
    """

    db = get_vector_db()

    db.add_documents(chunks)

    return db

def similarity_search(
    query,
    selected_document=None,
    k=6
):
    """
    Perform MMR search while preventing
    fetch_k from exceeding collection size.
    """

    db = get_vector_db()

    collection = db._collection

    total_chunks = collection.count()

    fetch_k = min(20, total_chunks)

    k = min(k, fetch_k)

    if selected_document is None:

        return db.max_marginal_relevance_search(
            query=query,
            k=k,
            fetch_k=fetch_k
        )

    return db.max_marginal_relevance_search(
        query=query,
        k=k,
        fetch_k=fetch_k,
        filter={
            "source": selected_document
        }
    )

def delete_document_vectors(filename):
    """
    Delete all vector embeddings belonging to a PDF.
    """

    db = get_vector_db()

    db._collection.delete(
        where={
            "source": filename
        }
    )