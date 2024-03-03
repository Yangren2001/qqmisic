# encoding=utf-8

"""
    @Project ：qqmusic 
    @File：Sparder
    @Time:2024/3/2 22:01
    @Author:YR
    @describe:爬虫

"""
import os.path

import requests
import time
import pandas as pd
import json
import urllib

from lxml.html import etree
from .utils import load_js,get_sub_dict
from .Config import (SONG_LIST_FILE, CLASS_TAG_FILE, ONE_SONG_LIST_NUM, SONG_LIST_TOTAL_NUM,PROJECT_PATH, REQUESTS_HEADERS, REQUEST_URL, REQUEST_SIGN_JS_PATH)



class Spader:
    # f_get_song_list_flag = True # 首次获取歌单
    js_env:load_js = None
    post_data_table = {
        # 分类标签
       "tag":'{"req_0":{"method":"GetAllTag","param":{"qq":""},"module":"music.playlist.PlaylistSquare"},"comm":{"g_tk":5381,"uin":0,"format":"json","ct":20,"cv":2005,"platform":"wk_v17","uid":"5440251060","guid":"8B49B593263B4E86D4C29D12A629222B"}}',
        # 该分类首次读取歌单,size class_id
        "first_song_list" :'{"req_0":{"module":"playlist.PlayListCategoryServer","method":"get_category_content","param":{"caller":"0","category_id":%s,"page":0,"use_page":1,"size":%s}},"comm":{"g_tk":5381,"uin":0,"format":"json","ct":20,"cv":2005,"platform":"wk_v17","uid":"5440251060","guid":"8B49B593263B4E86D4C29D12A629222B"}}',
        # 从一个tid后开始计算,tid size class_id
        "tid_song_list":'{"req_0":{"module":"playlist.PlayListCategoryServer","method":"get_category_content","param":{"last_id":"%s","size":%s,"order":5,"is_parent":0,"caller":"0","titleid":59,"category_id":%s}},"comm":{"g_tk":5381,"uin":0,"format":"json","ct":20,"cv":2005,"platform":"wk_v17","uid":"5440251060","guid":"8B49B593263B4E86D4C29D12A629222B"}}',

    }
    class_tag_temp = []

    def __init__(self):
        self.js_env = load_js(REQUEST_SIGN_JS_PATH)

    # def build_request(self, data=None, d_key=None, need_arg=False, *args):
    #     """
    #     构建url
    #     :param data:
    #     :param d_key:
    #     :param need_arg: data是否格式化字符
    #     :param args: 格式数据
    #     :return:
    #     """
    #     if data is None:
    #         data = self.post_data_table[d_key]
    #     if need_arg:
    #         data.format(*args)
    #     url = REQUEST_URL.format(self.get_time_arg(), self.get_sign(data))

    def get_all_tag(self, data=None):
        """
        获取所有分类
        :param data:json string
        :return:
        """
        if not os.path.exists(CLASS_TAG_FILE):
            if data is None:
                data = self.post_data_table['tag']
            url = REQUEST_URL.format(self.get_time_arg(), self.get_sign(data))
            # # proxy = {
            # #     "http": "127.0.0.1:8888",
            # #     "https": "127.0.0.1:8888"
            # #          }
            #
            res = requests.post(url, data=data, headers=REQUESTS_HEADERS)
            v_group = res.json()["req_0"]["data"]["v_group"]
            df = pd.DataFrame(v_group)
            df['v_item'].apply(lambda a: self.parse_tag(eval(a)) if isinstance(a ,str) else self.parse_tag(a))
            df1 = pd.DataFrame(self.class_tag_temp)
            df1.to_csv(CLASS_TAG_FILE,index=False)
            return df1
        else:
            df = pd.read_csv(CLASS_TAG_FILE)
            return df

    def get_song_list(self, class_id=None, f_size=None, tid=None, data=None):
        """
        获取歌单信息
        :param f_size: 第一次读取大小
        :param data:
        :return:df, tid
        """
        # if not os.path.exists(CLASS_TAG_FILE):
        if data is None:
            data = self.post_data_table['first_song_list']

        if tid is None:
            data = data % (class_id, f_size)
            # self.f_get_song_list_flag = False
        else:
            data = self.post_data_table['tid_song_list'] % (tid,  ONE_SONG_LIST_NUM, class_id,)
        url = REQUEST_URL.format(self.get_time_arg(), self.get_sign(data))
        res = requests.post(url, data=data, headers=REQUESTS_HEADERS)
        # 此处可采用多进程技术
        # 使用循环
        v_item = res.json()['req_0']["data"]["content"]['v_item']
        return self.parse_song_list(v_item, class_id)

    def get_class_song_list(self, class_id,data=None):
        """

        :param class_id:
        :param data:
        :return:
        """
        iter_num, f_szie = self.count_circulation_num()
        tid = None
        for i in range(iter_num):
            tid = self.get_song_list(class_id, f_szie, tid)[1]

    def parse_song_list(self, v, class_id):
        """
        解析歌单
        :param v:
        :return:
        """
        song_list = []
        for s in v:
            sc = s['basic']
            # 粉丝数,播放量，作者,标题
            song_info = get_sub_dict(sc, ['fav_cnt', 'play_cnt', 'tid', 'title', 'creator'])
            song_list.append(song_info)
        song_df = pd.DataFrame(song_list)
        # print(song_df.columns)
        song_df['uin'] = song_df['creator'].apply(lambda x: x['uin'])
        song_df['encrypt_uin'] = song_df['creator'].apply(lambda x: x['encrypt_uin'])
        song_df['nick'] = song_df['creator'].apply(lambda x: x['nick'])
        song_df['class'] = class_id
        song_df = song_df.drop(columns='creator')
        # print(song_df)
        if not os.path.exists(SONG_LIST_FILE):
            song_df.to_csv(SONG_LIST_FILE, mode="w", index=False)
        else:
            song_df.to_csv(SONG_LIST_FILE, mode="a+", index=False)
        return song_df, song_df.tail(1)['tid'].values[0]




    def count_circulation_num(self):
        """
        计算获取目标数量歌单的所需
        :return: 循环次数num，首次大小size
        """
        return (SONG_LIST_TOTAL_NUM // ONE_SONG_LIST_NUM) + 1, SONG_LIST_TOTAL_NUM % ONE_SONG_LIST_NUM

    def parse_tag(self, v_item):
        """

        :param x:
        :return:
        """
        for i in v_item:
            self.class_tag_temp.append(get_sub_dict(i, ['id', 'name']))


    def get_time_arg(self):
        """
        :return:
        """
        return str(time.time()).replace(".", "")[:12]


    def get_sign(self,data):
        """
        获取sign
        :param data:
        :return:
        """
        return self.js_env.call("sign", data)