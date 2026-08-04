from core.memory import ConversationMemory
from core.redis_cache import RedisCache
from utils.logger import logger


class MemoryManager:
    """
    Memory统一管理

    Redis优先
    本地文件兜底
    """

    def __init__(self):

        self.redis = RedisCache()

        self.local_pool = {}

        logger.info("MemoryManager初始化完成")

    def get_memory(self, session_id):

        # =====================
        # Redis读取
        # =====================

        redis_messages = self.redis.get(f"memory:{session_id}")

        if redis_messages:

            logger.info(f"Redis加载memory:{session_id}")

            memory = ConversationMemory(session_id)

            memory.messages = redis_messages

            return memory

        # =====================
        # 本地缓存
        # =====================

        if session_id in self.local_pool:

            return self.local_pool[session_id]

        memory = ConversationMemory(session_id)

        self.local_pool[session_id] = memory

        return memory

    def save_memory(self, session_id, messages):

        self.redis.set(f"memory:{session_id}", messages, expire=86400)

        logger.info(f"Memory保存Redis:{session_id}")
