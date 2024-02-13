#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: feiandxs
from server.server_base import app

from middleware import middlewares

# Add middleware to app
for middleware in middlewares:
    app.add_middleware(middleware)

