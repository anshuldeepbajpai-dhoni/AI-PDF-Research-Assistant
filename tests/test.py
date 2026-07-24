from utils.hybrid_search import hybrid_search

docs = hybrid_search(
    "machine learning"
)

print(len(docs))

for doc in docs:

    print(doc.metadata)