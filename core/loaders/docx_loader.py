from docx import Document

from utils.logger import logger


class DocxLoader:

    def load(self, path):

        logger.info(f"读取DOCX文件:{path}")

        doc = Document(path)

        texts = []

        for paragraph in doc.paragraphs:

            if paragraph.text.strip():

                texts.append(paragraph.text)

        content = "\n".join(texts)

        return [{"content": content, "metadata": {"source": path}}]
