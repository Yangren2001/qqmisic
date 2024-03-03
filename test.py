# encoding=utf-8

"""
    @Project ：qqmusic 
    @File：test.py
    @Time:2024/2/29 18:46
    @Author:YR
    @describe:

"""

# import requests
import execjs
#
# url = "https://y.qq.com/n/ryqq/category"
#
# headers= {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
#     "Cookie": "K=TT3YRyvI5u; ptcz=ddae176f55b47dd158b9ca102fffc7e65762bde9591ddf416f921e50125a7f34; pac_uid=0_1520fdd025483; iip=0; pgv_pvid=627541048; fqm_pvqid=0074a61f-c09a-45cc-af46-79496ec9f456; fqm_sessionid=784b33fc-75e4-4f71-a6be-6eed620e13db; pgv_info=ssid=s982386496; ts_refer=www.baidu.com/link; ts_uid=2061501128; _qpsvr_localtk=0.9465111021630557; ts_last=y.qq.com/n/ryqq/category",
# }
#
# res = requests.get(url, headers=headers)
# print(res.text)
# print(res)


#
# print(driver.page_source.encode("utf-8"))
#
# driver.quit()

from Package import utils
from Package.Config import *
# from Package.SpaderDriver import SpaderDirver
#sd = SpaderDirver()
# browser= sd.get_web_driver()
# browser.get("https://y.qq.com/n/ryqq/category")
# print(browser.page_source)
# # sd.get_web_driver().quit()

# data = '{"req_0":{"method":"GetAllTag","param":{"qq":""},"module":"music.playlist.PlaylistSquare"},"comm":{"g_tk":5381,"uin":0,"format":"json","ct":20,"cv":2005,"platform":"wk_v17","uid":"5440251060","guid":"8B49B593263B4E86D4C29D12A629222B"}}'
ctx = utils.load_js(REQUEST_SIGN_JS_PATH)
print(execjs.get().name)
data = '{"req_0":{"module":"playlist.PlayListCategoryServer","method":"get_category_content","param":{"caller":"0","category_id":3317,"page":0,"use_page":3,"size":60}},"comm":{"g_tk":5381,"uin":0,"format":"json","ct":20,"cv":2005,"platform":"wk_v17","uid":"5440251060","guid":"8B49B593263B4E86D4C29D12A629222B"}}'
t = ctx.call("sign", data)
print(t)
# print(ctx.exec_("window"))
