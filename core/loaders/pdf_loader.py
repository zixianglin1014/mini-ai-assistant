from pypdf import PdfReader

from utils.logger import logger


class PdfLoader:

    def load(self, path):

        logger.info(f"读取PDF文件:{path}")

        reader = PdfReader(path)

        documents = []

        for index, page in enumerate(reader.pages):

            text = page.extract_text()

            if text:

                documents.append(
                    {"content": text, "metadata": {"source": path, "page": index + 1}}
                )

        return documents
