'''
Date: 2025-01-31 16:46:52
Author: ywyz
LastModifiedBy: ywyz
Github: https://github.com/ywyz
LastEditors: ywyz
LastEditTime: 2025-01-31 16:53:34
ToDo: 登陆界面位置不在正中
'''
from nicegui import ui
from web.webPageLayout import WebPageLayout
from web.login.login import WebLogin

class WebPageFramework():
    def __init__(self):
        pass

    def show_all_elements(self):
        webframework = WebPageLayout()
        webframework.show_all_elements()


if __name__ in {"__main__", "__mp_main__"}:
    webpageframework = WebPageFramework()
    webpageframework.show_all_elements()
    weblogin = WebLogin()
    weblogin.show_login()
    ui.run()