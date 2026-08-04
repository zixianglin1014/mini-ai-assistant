from rank_bm25 import BM25Okapi

from utils.logger import logger


class KeywordRetriever:

    def __init__(self, documents, metadatas):

        self.documents = documents

        self.metadatas = metadatas

        # 中文简单分词

        tokenized_docs = [list(doc) for doc in documents]

        self.bm25 = BM25Okapi(tokenized_docs)

        logger.info("关键词检索初始化成功")

    def search(self, query, top_k=3):

        logger.info("执行关键词检索")

        tokens = list(query)

        scores = self.bm25.get_scores(tokens)

        results = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:top_k]

        docs = []

        for index, score in results:

            docs.append(
                {
                    "content": self.documents[index],
                    "metadata": self.metadatas[index],
                    "score": float(score),
                }
            )

        return docs
