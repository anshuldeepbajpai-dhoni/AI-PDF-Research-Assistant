from langchain_community.document_loaders import PyPDFLoader

from utils.ocr import (
    is_scanned_pdf,
    extract_text_from_scanned_pdf
)


def load_pdf(pdf_path):
    """
    Automatically loads both digital and scanned PDFs.
    """

    if is_scanned_pdf(pdf_path):

        docs = extract_text_from_scanned_pdf(pdf_path)

        return docs, len(docs)

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    return docs, len(docs)