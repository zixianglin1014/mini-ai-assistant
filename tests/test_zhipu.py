from unittest.mock import Mock

from core.llm import ZhipuLLM


def test_zhipu_chat():
    """
    测试LLM调用流程

    不请求真实智谱API
    使用Mock返回结果
    """

    llm = ZhipuLLM()

    # =====================
    # 创建模拟返回
    # =====================

    fake_response = Mock()

    fake_response.choices = [Mock(message=Mock(content="你好，我是测试模型"))]

    # =====================
    # 替换真实client
    # =====================

    llm.client.chat.completions.create = Mock(return_value=fake_response)

    # =====================
    # 调用
    # =====================

    result = llm.chat([{"role": "user", "content": "你好"}])

    # =====================
    # 断言
    # =====================

    assert result == "你好，我是测试模型"
