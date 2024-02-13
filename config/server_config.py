#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
from dotenv import load_dotenv
from pydantic import BaseModel

import os


class ServerConfig(BaseModel):
    host: str
    port: int
    reload: bool = False


def get_server_config():
    try:
        # 加载.env文件
        load_dotenv()

        # 读取环境变量
        host = os.getenv('HOST')
        port = os.getenv('PORT')
        port = int(port)

        return ServerConfig(
            host=host,
            port=port,
            reload=True if os.getenv('RELOAD') == 'True' else False
        )

    except Exception as e:
        print(e)
        return ServerConfig(host='0.0.0.0', port=8000)
