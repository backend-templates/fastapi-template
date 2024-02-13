#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
from pydantic import BaseModel
from typing import Any

from constants.api_status import APIStatus


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
