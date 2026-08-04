import sys
from pathlib import Path

from loguru import logger

# ==========================
# 初始化
# ==========================

logger.remove()


# ==========================
# 日志目录
# ==========================

LOG_DIR = Path("logs")

LOG_DIR.mkdir(exist_ok=True)


# ==========================
# 控制台日志
# ==========================

logger.add(
    sys.stdout,
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | " "{level} | " "{message}",
)


# ==========================
# 应用日志
# ==========================

logger.add(
    LOG_DIR / "app.log",
    level="INFO",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    encoding="utf-8",
    enqueue=True,
    backtrace=True,
    diagnose=True,
)


# ==========================
# 错误日志
# ==========================

logger.add(
    LOG_DIR / "error.log",
    level="ERROR",
    rotation="10 MB",
    retention="60 days",
    compression="zip",
    encoding="utf-8",
    enqueue=True,
    backtrace=True,
    diagnose=True,
)
