import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

# 加载.env

load_dotenv()


# 配置文件路径

BASE_DIR = Path(__file__).resolve().parent.parent


CONFIG_PATH = BASE_DIR / "configs" / "config.yaml"


# 读取yaml

with open(CONFIG_PATH, "r", encoding="utf-8") as f:

    config = yaml.safe_load(f)


def get_config():
    """
    获取全部配置
    """

    return config


def get_value(key, default=None):
    """
    根据路径获取配置

    示例:

    get_value(
        "llm.model"
    )

    """

    value = config

    for item in key.split("."):

        if value is None:

            return default

        value = value.get(item)

    return value if value is not None else default


def get_api_key():
    """
    获取智谱API KEY

    从环境变量读取
    """

    return os.getenv("ZHIPU_API_KEY")
