from fastapi import APIRouter
from pydantic import BaseModel
from utils.logger import logger
from core.app_state import app_state

router = APIRouter(prefix="/api", tags=["RAG"])


class RAGRequest(BaseModel):

    question: str


class RAGResponse(BaseModel):

    answer: str


# 初始化RAG应用


@router.post("/rag", response_model=RAGResponse)
def rag(request: RAGRequest):
    """
    RAG知识库问答接口
    """

    logger.info(f"API收到RAG问题:{request.question}")

    answer = app_state.rag_app.ask(request.question)

    return RAGResponse(answer=answer)
