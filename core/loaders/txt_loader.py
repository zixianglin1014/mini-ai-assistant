from utils.logger import logger


class TxtLoader:

    def load(self, path):

        logger.info(f"读取TXT文件:{path}")

        with open(path, "r", encoding="utf-8") as f:

            text = f.read()

        return [{"content": text, "metadata": {"source": path}}]
