from utils.database import (
    initialize_database,
    add_document,
    get_documents,
)

initialize_database()

add_document(
    "AI.pdf",
    42,
    180
)

docs = get_documents()

print(docs)