import os

os.environ["ANONYMIZED_TELEMETRY"] = "False"

from langchain_chroma import Chroma

from utils.embeddings import get_embedding_model


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


def create_vector_db(chunks):
    """
    Add new document chunks to the existing Chroma collection.
    """

    db = get_vector_db()

    db.add_documents(chunks)

    return db


def similarity_search(query, selected_document=None, k=5):
    """
    Search the vector database.

    If selected_document is None -> search all PDFs.
    Otherwise search only the selected PDF.
    """

    db = get_vector_db()

    if selected_document is None:

        return db.max_marginal_relevance_search(
            query=query,
            k=k,
            fetch_k=20
        )

    return db.max_marginal_relevance_search(
        query=query,
        k=k,
        fetch_k=20,
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