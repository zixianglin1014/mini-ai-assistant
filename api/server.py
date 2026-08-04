import time
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from api.chat import router as chat_router
from api.rag import router as rag_router
from core.app_state import app_state
from core.exceptions import AppException
from schemas.response import APIResponse
from utils.logger import logger
from utils.request_context import get_request_id, set_request_id


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("FastAPI服务启动")

    app_state.startup()

    yield

    app_state.shutdown()

    logger.info("FastAPI服务关闭")


app = FastAPI(
    title="Mini AI Assistant API",
    description="基于LLM和RAG技术的智能助手",
    version="1.0.0",
    lifespan=lifespan,
)


# =====================================================
# 全局异常处理
# =====================================================


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):

    request_id = get_request_id()

    logger.error(f"[{request_id}] " f"应用异常:{exc.message}")

    return JSONResponse(
        status_code=400,
        content=APIResponse(
            code=exc.code,
            message=exc.message,
            data={"detail": exc.detail, "request_id": request_id},
        ).model_dump(),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):

    request_id = get_request_id()

    logger.warning(f"[{request_id}] " f"参数错误:{exc.errors()}")

    return JSONResponse(
        status_code=422,
        content=APIResponse(
            code=422,
            message="请求参数错误",
            data={"errors": exc.errors(), "request_id": request_id},
        ).model_dump(),
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    request_id = get_request_id()

    logger.exception(f"[{request_id}] " f"系统异常:{exc}")

    return JSONResponse(
        status_code=500,
        content=APIResponse(
            code=500, message="服务器内部错误", data={"request_id": request_id}
        ).model_dump(),
    )


# =====================================================
# 请求日志中间件
# =====================================================


@app.middleware("http")
async def request_logger(request: Request, call_next):

    request_id = str(uuid.uuid4())

    set_request_id(request_id)

    start_time = time.time()

    logger.info(f"[{request_id}] " f"{request.method} " f"{request.url.path} 开始")

    response = await call_next(request)

    cost = time.time() - start_time

    logger.info(
        f"[{request_id}] "
        f"完成 "
        f"status={response.status_code} "
        f"time={cost:.3f}s"
    )

    response.headers["X-Request-ID"] = request_id

    return response


# =====================================================
# Router
# =====================================================


app.include_router(chat_router)


app.include_router(rag_router)


@app.get("/", response_model=APIResponse)
def root():

    return APIResponse(data={"service": "mini-ai-assistant"})


@app.get("/health")
def health():

    if app_state.ready:

        return {
            "status": "ok",
            "service": "mini-ai-assistant",
            "ready": True,
            "models": app_state.model_status(),
        }

    return JSONResponse(status_code=503, content={"status": "starting", "ready": False})


@app.get("/status")
def status():

    return {
        "service": "mini-ai-assistant",
        "ready": app_state.ready,
        "models": app_state.model_status(),
    }
