from application.chat_app import ChatApplication
from application.rag_app import RAGApplication
from core.model_manager import ModelManager
from utils.logger import logger


class AppState:
    """
    应用全局状态管理
    """

    def __init__(self):

        self.chat_app = None

        self.rag_app = None

        # 模型管理器
        self.model_manager = ModelManager()

        self.ready = False

    def startup(self):
        """
        服务启动初始化
        """

        logger.info("开始初始化AI服务")

        # =====================
        # 初始化应用
        # =====================

        self.chat_app = ChatApplication()

        self.rag_app = RAGApplication()

        # =====================
        # 注册模型
        # =====================

        logger.info("注册模型")

        self.model_manager.register("embedding", self.rag_app.embedding)

        self.model_manager.register("reranker", self.rag_app.reranker)

        # =====================
        # 加载模型
        # =====================

        self.model_manager.load_all()

        # =====================
        # 模型预热
        # =====================

        self.warmup_models()

        self.ready = True

        logger.info("AI服务初始化完成")

    def warmup_models(self):
        """
        模型预热
        """

        try:

            logger.info("开始模型预热")

            if self.rag_app:

                self.rag_app.embedding.embed_text("人工智能正在改变世界")

            logger.info("模型预热完成")

        except Exception as e:

            logger.error(f"模型预热失败:{e}")

    def model_status(self):
        """
        返回模型状态
        """

        return self.model_manager.status()

    def shutdown(self):
        """
        服务关闭
        """

        logger.info("关闭AI服务")

        self.model_manager.unload_all()

        self.ready = False

        logger.info("AI服务关闭")


app_state = AppState()
