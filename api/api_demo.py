#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
# main.py
from fastapi import FastAPI, Depends
from service.service_demo import ProductService, ProductCreate

app = FastAPI()


@app.post("/products/")
async def create_product(product_data: ProductCreate, product_service: ProductService = Depends()):
    try:
        new_product = await product_service.create_product(product_data)
        return new_product
    except Exception as e:
        # 这里可以处理异常，比如记录日志
        raise e
