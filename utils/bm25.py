import re

from rank_bm25 import BM25Okapi

from utils.vectordb import get_all_documents


class BM25Search:

    def __init__(self):

        self.documents = []

        self.tokenized = []

        self.bm25 = None

    def _tokenize(self, text):

        return re.findall(
            r"\w+",
            text.lower()
        )

    def build_index(
        self,
        selected_document=None
    ):
        """
        Build a BM25 index using all
        chunks already stored in ChromaDB.
        """

        docs = get_all_documents(
            selected_document
        )

        self.documents = docs

        self.tokenized = [

            self._tokenize(
                doc.page_content
            )

            for doc in docs

        ]

        if self.tokenized:

            self.bm25 = BM25Okapi(
                self.tokenized
            )

    def search(
        self,
        query,
        top_k=5
    ):

        if self.bm25 is None:

            self.build_index()

        if self.bm25 is None:

            return []

        scores = self.bm25.get_scores(
            self._tokenize(query)
        )

        ranked = sorted(

            zip(
                self.documents,
                scores
            ),

            key=lambda x: x[1],

            reverse=True

        )

        return [

            doc

            for doc, score in ranked[:top_k]

        ]


bm25 = BM25Search()