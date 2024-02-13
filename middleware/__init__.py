#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
from .process_time_middleware import process_time_middleware

middlewares = [
    process_time_middleware,
    # ... 其他中间件
]
