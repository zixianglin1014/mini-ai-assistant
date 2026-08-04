import os
from pathlib import Path

from dotenv import load_dotenv

from utils.logger import logger

# ==========================
# 项目根目录
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================
# 环境
# ==========================

APP_ENV = os.getenv("APP_ENV", "dev")


# ==========================
# 加载环境文件
# ==========================


ENV_FILE = BASE_DIR / "configs" / "env" / f".env.{APP_ENV}"


load_dotenv(ENV_FILE, override=False)


# ==========================
# API
# ==========================

ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")


# ==========================
# LLM
# ==========================

MODEL_NAME = os.getenv("MODEL_NAME", "glm-4-flash")


BASE_URL = os.getenv("BASE_URL", "https://open.bigmodel.cn/api/paas/v4/")


TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))


MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))


# ==========================
# 本地缓存
# ==========================

QUERY_CACHE_SIZE = int(os.getenv("QUERY_CACHE_SIZE", 200))


REWRITE_CACHE_SIZE = int(os.getenv("REWRITE_CACHE_SIZE", 200))


# ==========================
# Redis
# ==========================


REDIS_HOST = os.getenv("REDIS_HOST", "localhost")


REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))


REDIS_DB = int(os.getenv("REDIS_DB", 0))


REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)


REDIS_CACHE_TTL = int(os.getenv("REDIS_CACHE_TTL", 3600))


# ==========================
# Settings对象
# ==========================


class Settings:

    APP_ENV = APP_ENV

    ZHIPU_API_KEY = ZHIPU_API_KEY

    MODEL_NAME = MODEL_NAME

    BASE_URL = BASE_URL

    TEMPERATURE = TEMPERATURE

    MAX_TOKENS = MAX_TOKENS

    QUERY_CACHE_SIZE = QUERY_CACHE_SIZE

    REWRITE_CACHE_SIZE = REWRITE_CACHE_SIZE

    REDIS_HOST = REDIS_HOST

    REDIS_PORT = REDIS_PORT

    REDIS_DB = REDIS_DB

    REDIS_PASSWORD = REDIS_PASSWORD

    REDIS_CACHE_TTL = REDIS_CACHE_TTL


settings = Settings()


# ==========================
# 检查
# ==========================


if ZHIPU_API_KEY:

    logger.info(f"配置加载成功 ENV={APP_ENV}")


else:

    logger.warning(f"未读取到ZHIPU_API_KEY ENV={APP_ENV}")
