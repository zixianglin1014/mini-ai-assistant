from collections import OrderedDict

from utils.logger import logger


class LRUCache:
    """
    简单LRU缓存
    """

    def __init__(self, capacity=100):

        self.capacity = capacity

        self.cache = OrderedDict()

    def get(self, key):

        if key not in self.cache:

            return None

        value = self.cache.pop(key)

        self.cache[key] = value

        logger.info(f"缓存命中:{key}")

        return value

    def set(self, key, value):

        if key in self.cache:

            self.cache.pop(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:

            removed = self.cache.popitem(last=False)

            logger.info(f"缓存淘汰:{removed[0]}")

    def clear(self):

        self.cache.clear()

    def size(self):

        return len(self.cache)
