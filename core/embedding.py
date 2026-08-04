from sentence_transformers import SentenceTransformer

from utils.logger import logger


class EmbeddingClient:
    """
    Embedding模型生命周期管理
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.model = None

        return cls._instance

    def load(self):
        """
        加载Embedding模型
        """

        if self.model is not None:

            return

        logger.info("加载本地Embedding模型")

        self.model = SentenceTransformer("./models/bge-small-zh-v1.5")

        logger.info("Embedding模型加载成功")

    def is_loaded(self):
        """
        判断模型状态
        """

        return self.model is not None

    def unload(self):
        """
        释放Embedding模型
        """

        if self.model is None:

            return

        logger.info("释放Embedding模型")

        del self.model

        self.model = None

        logger.info("Embedding模型释放完成")

    def embed_text(self, text):
        """
        单文本向量化
        """

        if not self.is_loaded():

            self.load()

        vector = self.model.encode(text)

        return vector.tolist()

    def embed_documents(self, texts):
        """
        批量文本向量化
        """

        if not self.is_loaded():

            self.load()

        vectors = self.model.encode(texts)

        return vectors.tolist()
