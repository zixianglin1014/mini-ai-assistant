from utils.logger import logger


class ModelManager:
    """
    模型统一生命周期管理
    """

    def __init__(self):

        self.models = {}

    def register(self, name, model):
        """
        注册模型
        """

        self.models[name] = model

        logger.info(f"注册模型:{name}")

    def load_all(self):
        """
        加载全部模型
        """

        logger.info("开始加载全部模型")

        for name, model in self.models.items():

            if hasattr(model, "load"):

                logger.info(f"加载模型:{name}")

                model.load()

        logger.info("全部模型加载完成")

    def unload_all(self):
        """
        释放全部模型
        """

        logger.info("释放全部模型")

        for name, model in self.models.items():

            if hasattr(model, "unload"):

                logger.info(f"释放模型:{name}")

                model.unload()

    def status(self):
        """
        查看模型状态
        """

        result = {}

        for name, model in self.models.items():

            if hasattr(model, "is_loaded"):

                result[name] = model.is_loaded()

            else:

                result[name] = True

        return result
