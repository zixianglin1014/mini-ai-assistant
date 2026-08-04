from fastapi import APIRouter

from core.app_state import app_state
from utils.logger import logger

router = APIRouter(prefix="/models", tags=["models"])


@router.get("/status")
def model_status():
    """
    查看模型状态
    """

    return {"models": app_state.model_status()}


@router.post("/load")
def load_models():
    """
    加载全部模型
    """

    logger.info("API请求:加载模型")

    app_state.load_models()

    return {"message": "模型加载完成", "models": app_state.model_status()}


@router.post("/unload")
def unload_models():
    """
    卸载全部模型
    """

    logger.info("API请求:释放模型")

    app_state.unload_models()

    return {"message": "模型释放完成", "models": app_state.model_status()}
