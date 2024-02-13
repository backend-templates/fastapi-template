#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
from enum import Enum


class APIStatus(Enum):
    SUCCESS = 0, "操作成功"
    NOT_FOUND = 404, "资源未找到"
    BAD_REQUEST = 400, "错误的请求"
    UNAUTHORIZED = 401, "未授权"
    FORBIDDEN = 403, "禁止访问"
    INTERNAL_SERVER_ERROR = 500, "服务器内部错误"
    SERVICE_UNAVAILABLE = 503, "服务暂时不可用"
    # ... 其他状态码

    def __new__(cls, value, message):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.message = message
        return obj

    def __repr__(self):
        return f"{self.name}({self.value}): {self.message}"
