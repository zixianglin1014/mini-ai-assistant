from core.embedding import EmbeddingClient
from core.keyword_search import KeywordRetriever
from core.llm import ZhipuLLM
from core.loaders.document_loader import DocumentLoader
from core.query_rewriter import QueryRewriter
from core.rag import RAG
from core.reranker import Reranker
from core.text_splitter import TextSplitter
from core.vector_store import VectorStore
from utils.logger import logger


class RAGApplication:

    def __init__(self):

        logger.info("初始化RAG应用")

        # =====================
        # 1.加载知识库文档
        # =====================

        loader = DocumentLoader("data")

        documents = loader.load_all()

        logger.info(f"加载文档数量:{len(documents)}")

        # =====================
        # 2.文本切片
        # =====================

        splitter = TextSplitter()

        all_chunks = []
        all_metadata = []

        for doc in documents:

            chunks = splitter.split(doc["content"])

            for chunk in chunks:

                all_chunks.append(chunk)

                all_metadata.append(doc["metadata"])

        logger.info(f"生成文本块:{len(all_chunks)}")

        # =====================
        # 3.初始化核心组件
        # =====================

        self.embedding = EmbeddingClient()

        self.vector_store = VectorStore()

        self.llm = ZhipuLLM()

        # =====================
        # 4.关键词检索
        # =====================

        self.keyword_retriever = KeywordRetriever(all_chunks, all_metadata)

        # =====================
        # 5.Query Rewrite
        # =====================

        self.query_rewriter = QueryRewriter(self.llm)

        # =====================
        # 6.Reranker
        # =====================

        self.reranker = Reranker()

        # =====================
        # 7.RAG核心
        # =====================

        self.rag = RAG(
            embedding=self.embedding,
            vector_store=self.vector_store,
            llm=self.llm,
            query_rewriter=self.query_rewriter,
            keyword_retriever=self.keyword_retriever,
            reranker=self.reranker,
        )

    def ask(self, question):

        result = self.rag.ask(question)

        if isinstance(result, dict):

            answer = result.get("answer", "")

            sources = result.get("sources", [])

            output = answer

            if sources:

                output += "\n\n参考来源：\n"

                for source in sources:
                    output += "- " + source + "\n"

            return output

        return result
