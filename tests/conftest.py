import os
import sys

import pytest

# ============================
# 添加项目根目录到Python路径
# ============================

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if ROOT_DIR not in sys.path:

    sys.path.insert(0, ROOT_DIR)


@pytest.fixture
def fake_session_id():

    return "test_session"


@pytest.fixture
def fake_message():

    return "你好"
