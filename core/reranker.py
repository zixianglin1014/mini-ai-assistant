from FlagEmbedding import FlagReranker

from utils.logger import logger


class Reranker:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.model = None

        return cls._instance

    def load(self):

        if self.model is not None:

            return

        logger.info("加载Reranker模型")

        self.model = FlagReranker("./models/bge-reranker-base", use_fp16=False)

        logger.info("Reranker模型加载成功")

    def is_loaded(self):

        return self.model is not None

    def unload(self):

        if self.model is None:

            return

        logger.info("释放Reranker模型")

        del self.model

        self.model = None

    def rerank(self, question, documents, top_k=3):

        if not self.is_loaded():

            self.load()

        logger.info("开始Rerank排序")

        pairs = []

        for doc in documents:

            pairs.append([question, doc])

        scores = self.model.compute_score(pairs)

        results = list(zip(documents, scores))

        results.sort(key=lambda x: x[1], reverse=True)

        return [item[0] for item in results[:top_k]]
