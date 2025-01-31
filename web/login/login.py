'''
Date: 2025-01-29 22:45:54
Author: ywyz
LastModifiedBy: ywyz
Github: https://github.com/ywyz
LastEditors: ywyz
LastEditTime: 2025-01-31 16:49:40
'''
from nicegui import ui

class WebLogin:
    def __init__(self):
        self.username = " "
        self.password = " "

    def show_login(self):
        with ui.card(align_items="center"):
            with ui.column():
                ui.label("欢迎登陆")
                self.username= ui.input(label="用户名", placeholder='请输入用户名')
                self.password=ui.input(label="密码", placeholder='请输入密码',password=True, password_toggle_button=True)
                self.login_button = ui.button("登陆",on_click=self.on_login)

    def on_login(self):
        print('Logging in as', self.username.value)
