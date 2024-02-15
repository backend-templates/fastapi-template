#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
from builtins import str, bytes

from pydantic import BaseModel
from typing import Any, Optional
from authlib.jose import jwt
from datetime import datetime, timedelta


class JWTMeta(BaseModel):
    exp: int  # 过期时间（Expiration Time）
    sub: Optional[Any]  # 主题（Subject），通常是用户ID
    iat: int  # 签发时间（Issued At）
    iss: str  # 签发者（Issuer）


# 定义JWT的头部，指定算法（alg）和类型（typ）
header = {
    "alg": "HS256",  # 使用HMAC SHA256算法
    "typ": "JWT"
}


def generate_token(payload: JWTMeta, secret: str) -> bytes:
    # current_timestamp = datetime.now().timestamp()
    # payload demo
    # payload = {
    #     "sub": payload.sub,  # 主题（Subject），通常是用户ID
    #     "user_id": payload.user_id,
    #     "iat": current_timestamp,  # 签发时间（Issued At）
    #     "exp": current_timestamp + 60,  # 过期时间（Expiration Time）
    # }

    # 生成密钥（Secret），用于签名
    # secret = "your-secret-key"
    token = jwt.encode(header, payload, secret)
    return token


def validate_token(token: str, secret: str) -> Any:
    try:
        claims = jwt.decode(token, secret, algorithms=["HS256"])
        return claims
    except jwt.ExpiredSignatureError:
        return "Token has expired."
    except jwt.InvalidTokenError:
        return "Invalid token."
