#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
# database/mysql.py
from config.mysql_config import mysql_config

from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 创建数据库连接
engine = create_engine(
    f"mysql+pymysql://{mysql_config.user}:{mysql_config.password}@{mysql_config.host}:{mysql_config.port}/{mysql_config.db}",
    poolclass=QueuePool,
    pool_size=10,  # 连接池大小
    max_overflow=20,  # 最大溢出数量
    pool_timeout=30,  # 连接池超时时间（秒）
    pool_recycle=1800,  # 连接回收时间（秒）
    echo=True  # 是否打印SQL语句
)

session = sessionmaker(bind=engine)


