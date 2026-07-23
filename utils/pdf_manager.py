import os

from utils.database import (
    get_documents,
    delete_document
)

from utils.vectordb import delete_document_vectors


PDF_FOLDER = "pdfs"


def list_documents():
    return get_documents()


def delete_pdf(filename):
    """
    Delete PDF file, SQLite record, and Chroma vectors.
    """

    pdf_path = os.path.join(
        PDF_FOLDER,
        filename
    )

    # Delete PDF file
    if os.path.exists(pdf_path):
        os.remove(pdf_path)

    # Delete vectors
    delete_document_vectors(filename)

    # Delete SQLite record
    delete_document(filename)

def get_document_names():

    documents = get_documents()

    return [
        document[0]
        for document in documents
    ]