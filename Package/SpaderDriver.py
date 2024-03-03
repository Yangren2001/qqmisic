# encoding=utf-8

"""
    @Project ：qqmusic 
    @File：Spader
    @Time:2024/2/29 21:59
    @Author:YR
    @describe:爬虫

"""

from .Config import *
from selenium import webdriver


class SpaderDirver:
    """
    爬虫
    :param options: selenium browser options
    """
    web_driver: webdriver.Chrome = None

    def __init__(self, options: webdriver.ChromeOptions=None):
        if options is None:
            options = self.defult_driver_options()
        self.web_driver = self.init_driver(options)

    def get_web_driver(self):
        return self.web_driver

    def init_driver(self, options):
        """
        初始化驱动
        :param options:
        :return:
        """
        return webdriver.Chrome(
            service=webdriver.ChromeService(BROWSER_EXE_DRIVER_PATH),
            options=options
        )

    @classmethod
    def defult_driver_options(cls):
        """
        默认驱动启动参数
        :return:
        """
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # 无界面启动
        return options

    def __del__(self):
        if self.web_driver is not None:
            self.web_driver.quit()