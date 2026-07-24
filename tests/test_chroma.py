from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded.")

docs = [
    Document(page_content="Artificial Intelligence is the simulation of human intelligence.")
]

print("Creating Chroma DB...")

db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="test_db"
)

print("Success!")
print("Documents:", db._collection.count())