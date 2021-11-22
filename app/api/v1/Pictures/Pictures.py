#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/14
# @Author  : Sanzro Lee
# @Contact : sanzrolee@gmail.com
# @File    : Pictures
# @Software: PyCharm
"""
图片上传、查看
"""

import os
from pathlib import Path
from tempfile import NamedTemporaryFile
import shutil
from typing import List
from fastapi import Response, APIRouter, File, UploadFile

router = APIRouter()


# 上传图片
@router.post("/api/pictures/uploads", summary="上传图片")
async def upload_picture(
        files: List[UploadFile] = File(...)
):


    # save_dir = f"././././blog/assets/"
    save_dir = f"/home/Uplad-Pictures-VPS/blog/assets/"

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    farray = []
    for file in files:
        try:
            suffix = Path(file.filename).suffix

            with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
                shutil.copyfileobj(file.file, tmp)
                tmp_file_name = Path(tmp.name).name
        finally:
            file.file.close()

        farray.append(f"http://www.sanzro.xyz/api/pictures/{tmp_file_name}")

    return {"code": 200, "image": farray}


# 查看特定
@router.get('/api/pictures/{filename}', summary="查看特定命名图片")
async def get_pictures(filename: str):

    with open(r'/home/Uplad-Pictures-VPS/blog/assets/{}'.format(filename), 'rb') as f:
        resp = Response(f.read())
        return resp


# 查询所有图片
@router.get("/api/pictures/", summary="查看所有图片")
async def get_all_pictures():
    filepath = '/home/Uplad-Pictures-VPS/blog/assets/'
    return os.listdir(filepath)
