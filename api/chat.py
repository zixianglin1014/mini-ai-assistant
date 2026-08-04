import uuid

from fastapi import APIRouter
from pydantic import BaseModel

from core.app_state import app_state
from schemas.response import APIResponse
from utils.logger import logger

router = APIRouter(prefix="/api", tags=["Chat"])


# 请求模型


class ChatRequest(BaseModel):

    session_id: str = "default"

    message: str

    role: str = "student"


@router.post("/chat", response_model=APIResponse)
def chat(request: ChatRequest):
    """
    普通聊天接口
    """

    request_id = str(uuid.uuid4())

    logger.info(
        f"[{request_id}] "
        f"API收到消息 "
        f"session={request.session_id} "
        f"message={request.message}"
    )

    try:

        answer = app_state.chat_app.chat(
            session_id=request.session_id, message=request.message, role=request.role
        )

        return APIResponse(
            code=0,
            message="success",
            data={
                "session_id": request.session_id,
                "role": request.role,
                "answer": answer,
            },
            request_id=request_id,
        )

    except Exception as e:

        logger.error(f"[{request_id}] 聊天失败:{e}")

        return APIResponse(
            code=500, message="Internal Server Error", data=None, request_id=request_id
        )
