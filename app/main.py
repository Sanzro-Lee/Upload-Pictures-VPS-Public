#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/14
# @Author  : Sanzro Lee
# @Contact : sanzrolee@gmail.com
# @File    : main.py
# @Software: PyCharm
"""
主控制
"""

import sys
sys.path.insert(0, '/home/Uplad-Pictures-VPS/app/api/v1/')
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.middleware.cors import CORSMiddleware

# from app.api.v1.Pictures import Pictures
from Pictures import Pictures

# 服务器端配置
app = FastAPI(
    docs_url=None
)

security = HTTPBasic()


@app.get("/api/docs", include_in_schema=False)
async def get_documentation(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "admin":
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
           headers={"WWW-Authenticate": "Basic"},
        )
    else:
        return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

app.include_router(Pictures.router, tags=["图片 API"])

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8011",
    "http://127.0.0.1",
    "http://127.0.0.1:8011",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
