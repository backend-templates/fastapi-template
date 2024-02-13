#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
from pydantic import BaseModel

from database.mysql import session


class Product(BaseModel):
    id: int


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float


def get_db_session():
    return session


class ProductService:
    def __init__(self):
        self.db_session = get_db_session()

    def create_product(self, product_data):
        try:
            # 开始事务
            self.db_session.begin()

            # 创建产品
            new_product = Product(**product_data)
            self.db_session.add(new_product)

            # 提交事务
            self.db_session.commit()
            return new_product

        except Exception as e:
            # 如果发生异常，回滚事务
            self.db_session.rollback()
            raise e  # 重新抛出异常

        finally:
            # 关闭Session（可选，取决于你的应用逻辑）
            self.db_session.close()