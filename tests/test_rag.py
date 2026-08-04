from unittest.mock import Mock

from application.rag_app import RAGApplication


def test_rag_application():
    """
    测试RAG应用是否可以正常初始化并回答

    使用Mock替代真实LLM
    """

    rag_app = RAGApplication()

    # =====================
    # Mock LLM
    # =====================

    rag_app.llm.chat = Mock(return_value="这是一个模拟的大语言模型回答")

    # RAG内部使用的是同一个llm对象

    rag_app.rag.llm = rag_app.llm

    question = "什么是大语言模型"

    answer = rag_app.ask(question)

    assert answer is not None

    assert isinstance(answer, str)

    assert len(answer) > 0
