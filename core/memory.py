import json
from pathlib import Path

from core.redis_cache import RedisCache
from utils.logger import logger


class ConversationMemory:
    """
    会话记忆管理

    Redis主存储
    JSON文件备份

    """

    def __init__(self, session_id, max_rounds=10):

        self.session_id = session_id

        self.max_rounds = max_rounds

        # =====================
        # Redis
        # =====================

        self.redis = RedisCache()

        # =====================
        # JSON backup
        # =====================

        self.memory_dir = Path("memory")

        self.memory_dir.mkdir(exist_ok=True)

        self.file_path = self.memory_dir / f"{session_id}.json"

        self.messages = []

        self.load()

    # =====================
    # 加载Memory
    # =====================

    def load(self):

        # 优先Redis

        data = self.redis.get(self.session_id)

        if data:

            self.messages = data

            logger.info(f"Redis加载Memory成功:{self.session_id}")

            return

        # Redis没有

        # 尝试文件

        if self.file_path.exists():

            try:

                with open(self.file_path, "r", encoding="utf-8") as f:

                    self.messages = json.load(f)

                logger.info(f"文件加载Memory:{self.session_id}")

                # 回写Redis

                self.redis.set(self.session_id, self.messages)

            except Exception as e:

                logger.error(f"Memory文件读取失败:{e}")

                self.messages = []

        else:

            self.messages = []

    # =====================
    # 添加消息
    # =====================

    def add_message(self, role, content):

        self.messages.append({"role": role, "content": content})

        self.trim()

        self.save()

    # =====================
    # 获取消息
    # =====================

    def get_messages(self):

        return self.messages

    # =====================
    # 限制上下文
    # =====================

    def trim(self):

        system_messages = [m for m in self.messages if m["role"] == "system"]

        chat_messages = [m for m in self.messages if m["role"] != "system"]

        max_messages = self.max_rounds * 2

        chat_messages = chat_messages[-max_messages:]

        self.messages = system_messages + chat_messages

    # =====================
    # 保存
    # =====================

    def save(self):

        # Redis保存

        self.redis.set(self.session_id, self.messages)

        # JSON备份

        try:

            with open(self.file_path, "w", encoding="utf-8") as f:

                json.dump(self.messages, f, ensure_ascii=False, indent=4)

        except Exception as e:

            logger.error(f"Memory备份失败:{e}")
