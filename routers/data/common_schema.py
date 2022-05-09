from pydantic import BaseModel
from typing import Optional


class Result(BaseModel):
    status: int = 0
    msg: str = ''
    data: Optional[dict] = {}
