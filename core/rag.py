import time

from core.cache_manager import CacheManager
from core.prompt_manager import PromptManager
from utils.logger import logger


class RAG:

    def __init__(
        self,
        embedding,
        vector_store,
        llm,
        query_rewriter=None,
        keyword_retriever=None,
        reranker=None,
    ):

        self.embedding = embedding

        self.vector_store = vector_store

        self.llm = llm

        self.query_rewriter = query_rewriter

        self.keyword_retriever = keyword_retriever

        self.reranker = reranker

        self.prompt_manager = PromptManager()

        self.cache_manager = CacheManager()

    def merge_documents(self, vector_docs, keyword_docs):

        merged = []

        seen = set()

        for doc in vector_docs + keyword_docs:

            key = doc.strip()

            if key not in seen:

                seen.add(key)

                merged.append(doc)

        logger.info(f"融合后文档数量:{len(merged)}")

        return merged

    def ask(self, question):

        logger.info("开始RAG查询")

        request_start = time.time()

        timing = {}

        # =========================
        # 0.Cache检查
        # =========================

        cached_answer = self.cache_manager.get_query(question)

        if cached_answer:

            logger.info("命中RAG缓存")

            return cached_answer

        # =========================
        # 防止缓存击穿
        # =========================

        self.cache_manager.acquire_lock()

        try:

            # 双重检查

            cached_answer = self.cache_manager.get_query(question)

            if cached_answer:

                logger.info("等待后命中RAG缓存")

                return cached_answer

            # =========================
            # 1.Query Rewrite
            # =========================

            search_question = question

            if self.query_rewriter:

                start = time.time()

                search_question = self.query_rewriter.rewrite(question)

                timing["rewrite"] = round(time.time() - start, 3)

            # =========================
            # 2.Vector Retrieval
            # =========================

            start = time.time()

            query_vector = self.embedding.embed_text(search_question)

            timing["embedding"] = round(time.time() - start, 3)

            vector_result = self.vector_store.search(query_vector, top_k=5)

            vector_documents = []

            metadatas = []

            for doc, meta in zip(
                vector_result["documents"][0], vector_result["metadatas"][0]
            ):

                vector_documents.append(doc)

                metadatas.append(meta)

            logger.info(f"向量召回数量:{len(vector_documents)}")

            # =========================
            # 3.Keyword Retrieval
            # =========================

            keyword_documents = []

            if self.keyword_retriever:

                keyword_results = self.keyword_retriever.search(
                    search_question, top_k=5
                )

                for item in keyword_results:

                    keyword_documents.append(item["content"])

                    metadatas.append(item["metadata"])

            logger.info(f"关键词召回数量:{len(keyword_documents)}")

            # =========================
            # 4.Merge
            # =========================

            documents = self.merge_documents(vector_documents, keyword_documents)

            # =========================
            # 5.Rerank
            # =========================

            if self.reranker:

                documents = self.reranker.rerank(search_question, documents, top_k=3)

            logger.info(f"Rerank后数量:{len(documents)}")

            # =========================
            # 6.Context
            # =========================

            context = "\n\n".join(documents)

            # =========================
            # 7.Prompt
            # =========================

            prompt = self.prompt_manager.render(
                "qa", context=context, question=question
            )

            # =========================
            # 8.LLM
            # =========================

            start = time.time()

            answer = self.llm.chat(prompt)

            timing["llm"] = round(time.time() - start, 3)

            # =========================
            # 9.Source
            # =========================

            sources = []

            for meta in metadatas:

                source = meta.get("source")

                page = meta.get("page")

                if page:

                    sources.append(f"{source} 第{page}页")

                else:

                    sources.append(source)

            timing["total"] = round(time.time() - request_start, 3)

            logger.info(f"RAG耗时统计:{timing}")

            result = {"answer": answer, "sources": sources}

            # =========================
            # 10.写缓存
            # =========================

            self.cache_manager.set_query(question, result)

            return result

        finally:

            self.cache_manager.release_lock()
