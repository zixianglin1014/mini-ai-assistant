import json

import redis

from configs.settings import settings
from utils.logger import logger


class RedisCache:

    PREFIX = "rag:"

    def __init__(self):

        try:

            self.client = redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                password=settings.REDIS_PASSWORD,
                decode_responses=True,
                socket_connect_timeout=3,
            )

            self.client.ping()

            logger.info("Redis缓存连接成功")

        except Exception as e:

            logger.error(f"Redis连接失败:{e}")

            self.client = None

    def build_key(self, key):

        return self.PREFIX + key

    def get(self, key):

        if not self.client:

            return None

        value = self.client.get(self.build_key(key))

        if value:

            return json.loads(value)

        return None

    def set(self, key, value, expire=3600):

        if not self.client:

            return

        self.client.set(
            self.build_key(key), json.dumps(value, ensure_ascii=False), ex=expire
        )

    def delete(self, key):

        if self.client:

            self.client.delete(self.build_key(key))
