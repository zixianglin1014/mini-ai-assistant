from typing import Any, Optional

from pydantic import BaseModel


class APIResponse(BaseModel):
    """
    统一API响应结构
    """

    code: int = 0

    message: str = "success"

    data: Optional[Any] = None

    request_id: Optional[str] = None
