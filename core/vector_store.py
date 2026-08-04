import chromadb

from utils.logger import logger


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="chroma_db")

        self.collection = self.client.get_or_create_collection(name="knowledge_base")

        logger.info("Chroma初始化成功")

    def add_documents(self, documents, embeddings, metadatas):

        ids = [str(i) for i in range(len(documents))]

        self.collection.add(
            ids=ids, documents=documents, embeddings=embeddings, metadatas=metadatas
        )

        logger.info("文档写入向量数据库成功")

    def search(self, query_vector, top_k=3):

        result = self.collection.query(query_embeddings=[query_vector], n_results=top_k)

        return result

    def get_all_documents(self):
        """
        获取知识库全部文档

        用于BM25关键词检索初始化
        """

        result = self.collection.get(include=["documents", "metadatas"])

        return (result.get("documents", []), result.get("metadatas", []))
