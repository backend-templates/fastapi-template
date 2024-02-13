#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
from enum import Enum

from pydantic import BaseModel
from typing import Any


class APIStatus(Enum):
    SUCCESS = 0, "操作成功"
    NOT_FOUND = 404, "资源未找到"
    BAD_REQUEST = 400, "错误的请求"
    UNAUTHORIZED = 401, "未授权"
    FORBIDDEN = 403, "禁止访问"
    INTERNAL_SERVER_ERROR = 500, "服务器内部错误"
    SERVICE_UNAVAILABLE = 503, "服务暂时不可用"
    # ... 其他状态码

    def __init__(self, value: int, message: str):
        self.value = value
        self.message = message

    def __repr__(self):
        return f"{self.name}({self.value}): {self.message}"


class APIJsonResponse(BaseModel):
    code: APIStatus
    message: str = None
    data: Any = None

    def __init__(self, *, code: APIStatus = None, message: str = None, data: Any = None):
        super().__init__(code=code, message=message, data=data)

        # 如果没有指定message，使用枚举的默认message
        if not message:
            self.message = self.code.message

    @property
    def status_code(self) -> int:
        return self.code.value
