#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
import time
from fastapi import Request, Response
from fastapi.responses import JSONResponse


async def process_time_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
