import threading

from configs.settings import settings
from core.cache import LRUCache
from core.redis_cache import RedisCache
from utils.logger import logger


class CacheManager:
    """
    全局缓存管理器


    一级:
        LRU内存缓存


    二级:
        Redis缓存


    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if hasattr(self, "initialized"):

            return

        logger.info("初始化缓存管理器")

        # =====================
        # Redis
        # =====================

        self.redis = RedisCache()

        # =====================
        # LRU一级缓存
        # =====================

        self.query_cache = LRUCache(capacity=settings.QUERY_CACHE_SIZE)

        self.rewrite_cache = LRUCache(capacity=settings.REWRITE_CACHE_SIZE)

        # =====================
        # 并发锁
        # =====================

        self.lock = threading.Lock()

        self.initialized = True

    # =====================
    # Query缓存
    # =====================

    def get_query(self, question):

        # 一级缓存

        value = self.query_cache.get(question)

        if value:

            logger.info(f"LRU缓存命中:{question}")

            return value

        # 二级缓存

        value = self.redis.get(f"query:{question}")

        if value:

            logger.info(f"Redis缓存命中:{question}")

            # 回填LRU

            self.query_cache.set(question, value)

            return value

        return None

    def set_query(self, question, answer):

        # 一级缓存

        self.query_cache.set(question, answer)

        # 二级缓存

        self.redis.set(f"query:{question}", answer, expire=settings.REDIS_CACHE_TTL)

        logger.info(f"写入Redis缓存:{question}")

    # =====================
    # Query Rewrite缓存
    # =====================

    def get_rewrite(self, question):

        value = self.rewrite_cache.get(question)

        if value:

            logger.info(f"Rewrite LRU命中:{question}")

            return value

        value = self.redis.get(f"rewrite:{question}")

        if value:

            logger.info(f"Rewrite Redis命中:{question}")

            self.rewrite_cache.set(question, value)

        return value

    def set_rewrite(self, question, rewrite):

        self.rewrite_cache.set(question, rewrite)

        self.redis.set(f"rewrite:{question}", rewrite, expire=settings.REDIS_CACHE_TTL)

    # =====================
    # Lock
    # =====================

    def acquire_lock(self):

        logger.info("获取缓存锁")

        self.lock.acquire()

    def release_lock(self):

        self.lock.release()

        logger.info("释放缓存锁")

    # =====================
    # 清理
    # =====================

    def clear(self):

        self.query_cache.clear()

        self.rewrite_cache.clear()

        logger.info("LRU缓存清理完成")

        # Redis清理

        if self.redis.client:

            self.redis.client.flushdb()

            logger.info("Redis缓存清理完成")

    # =====================
    # 状态
    # =====================

    def status(self):

        return {
            "query_cache_size": self.query_cache.size(),
            "rewrite_cache_size": self.rewrite_cache.size(),
            "redis": self.redis.client is not None,
        }
