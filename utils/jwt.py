#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
from authlib.jose import jwt

# 定义JWT的头部，指定算法（alg）和类型（typ）
header = {
    "alg": "HS256",  # 使用HMAC SHA256算法
    "typ": "JWT"
}

# 定义JWT的载荷，包含一些声明（claims）
payload = {
    "sub": "1234567890",  # 主题（Subject），通常是用户ID
    "name": "John Doe",
    "iat": 1516239022,  # 签发时间（Issued At）
    "exp": 1516239022 + 60,  # 过期时间（Expiration Time）
}

# 生成密钥（Secret），用于签名
secret = "your-secret-key"

# 使用jwt.encode()方法生成JWT
token = jwt.encode(header, payload, secret)

# todo

# 使用jwt.decode()方法验证JWT
try:
    claims = jwt.decode(token, secret, algorithms=["HS256"])
    print(claims)  # 如果JWT有效，将打印出解码后的载荷
except jwt.ExpiredSignatureError:
    print("Token has expired.")
except jwt.InvalidTokenError:
    print("Invalid token.")