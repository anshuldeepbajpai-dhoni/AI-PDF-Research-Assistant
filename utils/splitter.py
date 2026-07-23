from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(documents, filename):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    for i, chunk in enumerate(chunks):

        chunk.metadata["source"] = filename
        chunk.metadata["chunk_id"] = i

    return chunks