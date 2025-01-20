
'''
Author: ywyz admin@ywyz.tech
Date: 2025-01-20 01:55:06
LastEditors: ywyz admin@ywyz.tech
LastEditTime: 2025-01-20 05:51:56
FilePath: /github/KindergardenManager/web/webFramework.py
Description: https://github.com/ywyz

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
'''
TODO:
    1.显示不出logo,需要修复
    2.左侧导航栏位置需要调整
    3.主页需要完成上部导航栏
'''
from nicegui import ui


class WebFramework():                   # 网页框架
    def __init__(self):
        pass

    def show_footer(self):              # 显示底部              
        with ui.footer().style('background-color:rgb(50, 113, 201);'):
            ui.label('© 2025 幼儿园信息管理系统')
            ui.label('powered by Python NiceGUI ywyz')

    def show_header(self):              # 显示头部
        with ui.header().style('background-color:rgb(50, 113, 201);')\
                .classes('items-center justify-between'):
            ui.image('/static/logo.ico')
            ui.button(on_click=lambda: self.left_drawer.toggle(), icon='menu')\
                .props('flat color=white')

    def show_left_drawer(self):         # 显示左侧导航栏
        with ui.left_drawer(top_corner=True, bottom_corner=True)\
                .style('background-color:rgb(#000000);'):
            ui.label('幼儿园信息管理系统')
            ui.label('首页')
            ui.label('幼儿园信息')
            ui.label('教师信息')
            ui.label('学生信息')
            ui.label('班级信息')
            ui.label('课程信息')
            ui.label('活动信息')
            ui.label('退出')

    def show_all_elements(self):
        self.show_header()
        self.show_left_drawer()
        self.show_footer()


