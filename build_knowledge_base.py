from core.embedding import EmbeddingClient
from core.loaders.document_loader import DocumentLoader
from core.text_splitter import TextSplitter
from core.vector_store import VectorStore
from utils.logger import logger


def main():

    logger.info("开始构建知识库")

    # 1.加载所有文档

    loader = DocumentLoader("data")

    documents = loader.load_all()

    logger.info(f"加载文档数量:{len(documents)}")

    # 2.文本切片

    splitter = TextSplitter()

    all_chunks = []

    all_metadata = []

    for doc in documents:

        chunks = splitter.split(doc["content"])

        for chunk in chunks:

            all_chunks.append(chunk)

            all_metadata.append(doc["metadata"])

    logger.info(f"生成文本块:{len(all_chunks)}")

    # 3.生成Embedding

    embedding = EmbeddingClient()

    vectors = embedding.embed_documents(all_chunks)

    logger.info("Embedding完成")

    # 4.写入向量数据库

    db = VectorStore()

    db.add_documents(texts=all_chunks, embeddings=vectors, metadatas=all_metadata)

    logger.info("知识库构建完成")


if __name__ == "__main__":

    main()
