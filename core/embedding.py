from sentence_transformers import SentenceTransformer

from utils.logger import logger


MODEL_PATH = "./models/bge-small-zh-v1.5"

MODEL_NAME = "BAAI/bge-small-zh-v1.5"


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

        if self.model is not None:
            return


        logger.info("加载Embedding模型")


        if os.path.exists(MODEL_PATH):

            logger.info(
                f"加载本地模型:{MODEL_PATH}"
            )

            self.model = SentenceTransformer(
                MODEL_PATH
            )


        else:

            logger.info(
                "本地模型不存在，开始下载Embedding模型"
            )


            self.model = SentenceTransformer(
                MODEL_NAME
            )


            logger.info(
                "保存模型到本地"
            )


            self.model.save(
                MODEL_PATH
            )


        logger.info(
            "Embedding模型加载成功"
        )


    def is_loaded(self):

        return self.model is not None



    def unload(self):

        if self.model is None:
            return


        logger.info(
            "释放Embedding模型"
        )


        del self.model

        self.model=None


    def embed_text(self,text):

        if not self.is_loaded():

            self.load()


        vector=self.model.encode(text)

        return vector.tolist()



    def embed_documents(self,texts):

        if not self.is_loaded():

            self.load()


        vectors=self.model.encode(texts)

        return vectors.tolist()
