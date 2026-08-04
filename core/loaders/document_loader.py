import os

from core.loaders.docx_loader import DocxLoader
from core.loaders.pdf_loader import PdfLoader
from core.loaders.txt_loader import TxtLoader
from utils.logger import logger


class DocumentLoader:

    def __init__(self, directory):

        self.directory = directory

        self.loaders = {".txt": TxtLoader(), ".pdf": PdfLoader(), ".docx": DocxLoader()}

        logger.info(f"初始化文档加载器:{directory}")

    def load_file(self, path):

        suffix = os.path.splitext(path)[1].lower()

        if suffix not in self.loaders:

            logger.warning(f"不支持文件:{suffix}")

            return []

        return self.loaders[suffix].load(path)

    def load_all(self):

        documents = []

        for filename in os.listdir(self.directory):

            filepath = os.path.join(self.directory, filename)

            if not os.path.isfile(filepath):

                continue

            docs = self.load_file(filepath)

            documents.extend(docs)

        logger.info(f"成功加载{len(documents)}个文档块")

        return documents
