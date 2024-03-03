# encoding=utf-8

"""
    @Project ：qqmusic 
    @File：Config
    @Time:2024/2/29 20:49
    @Author:YR
    @describe:config file

"""
import os

PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
BROWSER_EXE_DRIVER_NAME = "chromedriver.exe"   # 浏览器驱动文件
BROWSER_EXE_DRIVER_PATH = os.path.join(PROJECT_PATH, "driver",
                                       BROWSER_EXE_DRIVER_NAME)

REQUEST_SIGN_JS_PATH = os.path.join(PROJECT_PATH, "js", "sign.js")
REQUEST_URL = "https://u.y.qq.com/cgi-bin/musics.fcg?_={}&sign={}"
REQUESTS_HEADERS= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.47.134 Safari/537.36 QBCore/3.53.47.400 QQBrowser/9.0.2524.400 pcqqmusic/20.05.2431.0102 SkinId/10001|1ecc94|144|1|||20d6c0",
    "Cookie": "fqm_pvqid=320e900c-3ed9-46ac-869f-228598493fcf; fqm_sessionid=be76b4d1-2b7b-4374-9a72-b94f7591dd10; ts_refer=i2.y.qq.com/n3/wk_v20/entry/index/musicroom/recommend; qqmusic_miniversion=5; qqmusic_version=20; uid=5440251060; pgv_info=ssid=s8850016976; ts_last=y.qq.com/wk_v17/; pgv_pvid=92300472; ts_uid=2231574760",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "http://y.qq.com/wk_v17/",
    # "Accept": "application/json",
    "Host":"u.y.qq.com",
}

CLASS_TAG_FILE = os.path.join(PROJECT_PATH, "data", "class_tag.csv")
SONG_LIST_FILE = os.path.join(PROJECT_PATH, "data", "song_list.csv")
ONE_SONG_LIST_NUM = 60  # 单次读取歌单数大小
SONG_LIST_TOTAL_NUM = 1000



