from typing import Optional


class AppException(Exception):
    """
    应用基础异常
    """

    def __init__(self, message: str, code: int = 500, detail: Optional[str] = None):

        self.message = message

        self.code = code

        self.detail = detail

        super().__init__(message)


class LLMException(AppException):
    """
    LLM调用异常
    """

    def __init__(self, message="LLM服务异常", detail=None):

        super().__init__(message=message, code=5001, detail=detail)


class MemoryException(AppException):
    """
    Memory异常
    """

    def __init__(self, message="Memory服务异常", detail=None):

        super().__init__(message=message, code=5002, detail=detail)


class RAGException(AppException):
    """
    RAG异常
    """

    def __init__(self, message="RAG服务异常", detail=None):

        super().__init__(message=message, code=5003, detail=detail)
