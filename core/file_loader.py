from pathlib import Path

from utils.logger import logger


class FileLoader:

    def __init__(self, file_path):

        self.file_path = Path(file_path)

        logger.info(f"初始化文件加载器：{file_path}")

    def load(self):

        logger.info("开始读取文件")

        if not self.file_path.exists():

            logger.error("文件不存在")
            raise FileNotFoundError("文件不存在")

        content = self.file_path.read_text(encoding="utf-8")

        logger.info("文件读取成功")

        return content
