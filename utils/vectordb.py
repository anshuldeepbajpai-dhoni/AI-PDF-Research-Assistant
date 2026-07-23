from langchain_chroma import Chroma

from config import CHROMA_DB
from utils.embeddings import get_embedding_model


def create_vector_db(chunks):

    embeddings = get_embedding_model()

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB
    )

    return db


def load_vector_db():

    embeddings = get_embedding_model()

    db = Chroma(
        persist_directory=CHROMA_DB,
        embedding_function=embeddings
    )

    return db