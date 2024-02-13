#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
import os

from pydantic import BaseModel, ValidationError


class MysqlConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    db: str


def get_mysql_config():
    try:
        # 从环境变量中获取配置
        mysql_database_host = os.getenv('MYSQL_DATABASE_HOST')
        mysql_database_port = os.getenv('MYSQL_DATABASE_PORT')
        mysql_database_user = os.getenv('MYSQL_DATABASE_USER')
        mysql_database_password = os.getenv('MYSQL_DATABASE_PASSWORD')
        mysql_database_db = os.getenv('MYSQL_DATABASE_DB')

        # 检查是否所有配置项都存在且非空
        missing_fields = []
        if not mysql_database_host:
            missing_fields.append('host')
        if not mysql_database_port:
            missing_fields.append('port')
        if not mysql_database_user:
            missing_fields.append('user')
        if not mysql_database_password:
            missing_fields.append('password')
        if not mysql_database_db:
            missing_fields.append('db')

        if missing_fields:
            raise ValueError(f"Missing configuration fields: {', '.join(missing_fields)}")

        # 如果所有配置项都存在，创建MysqlConfig实例
        return MysqlConfig(
            host=mysql_database_host,
            port=int(mysql_database_port),
            user=mysql_database_user,
            password=mysql_database_password,
            db=mysql_database_db
        )

    except ValueError as e:
        raise ValidationError("Missing or invalid MySQL configuration: " + str(e))


mysql_config = get_mysql_config()
