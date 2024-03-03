# encoding=utf-8

"""
    @Project ：qqmusic 
    @File：utils
    @Time:2024/2/29 20:49
    @Author:YR
    @describe:function lib

"""

import os
from typing import Union

import execjs

def load_js(file=None, loaders=execjs.compile) -> execjs.ExternalRuntime.Context:
    if file is None:
        raise Exception("miss args file")
    if os.path.isfile(file) and not os.path.exists(file):
        raise FileExistsError(f"file {file} not exists.")
    file = os.path.abspath(file) if not os.path.isabs(file) else file
    if not os.path.splitext(file)[1].strip(".") == "js":
        raise Exception("File suffix must be js!")
    # print(file)
    with open(file, "r",encoding="utf-8") as f:
        return loaders(f.read())

def get_sub_dict(d:dict, keys:Union[list, tuple,]):
    """
    获取新字典
    :param d:原字典
    :param keys:list
    :return:
    """
    return dict(zip(keys, [d.get(i, None) for i in keys]))



