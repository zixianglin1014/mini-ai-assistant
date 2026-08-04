from core.cache_manager import CacheManager
from utils.logger import logger


class QueryRewriter:

    def __init__(self, llm):

        self.llm = llm

        self.cache = CacheManager()

    def rewrite(self, question):

        # =====================
        # 查询缓存
        # =====================

        cached = self.cache.get_rewrite(question)

        if cached:

            logger.info("Query Rewrite缓存命中")

            return cached

        logger.info("正在进行问题重写")

        prompt = f"""

你是一个搜索优化专家。


请把用户的问题改写成适合知识库检索的问题。


要求：

1. 保留核心意思

2. 去除口语表达

3. 增加必要关键词

4. 只输出优化后的问题



用户问题：

{question}


优化后的检索问题：

"""

        result = self.llm.chat(prompt)

        result = result.strip()

        # =====================
        # 写入缓存
        # =====================

        self.cache.set_rewrite(question, result)

        return result
