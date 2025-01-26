'''
Author: ywyz admin@ywyz.tech
Date: 2025-01-20 01:55:06
LastEditors: ywyz admin@ywyz.tech
LastEditTime: 2025-01-20 06:49:44
FilePath: /KindergardenManager/web/webFramework.py
Description: https://github.com/ywyz

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved.
'''
'''
TODO:
    2.左侧导航栏位置需要调整
    3.主页需要完成上部导航栏
    4.主页需要完成中部内容
'''
from nicegui import ui



class WebPageLayout():                   # 网页框架
    def __init__(self):
        pass

    def show_footer(self):              # 显示底部
        with ui.footer().style('background-color:rgb(50, 113, 201);').classes('items-center justify-center'):
            ui.label('© 2025 幼儿园信息管理系统')
            ui.label('powered by Python NiceGUI ywyz')


    def show_header(self):              # 显示头部
        with ui.left_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as left_drawer:
            ui.label('幼儿园信息管理系统').style('font-size: 20px; font-weight: bold;')
            ui.label('首页').style('font-size: 20px; font-weight: bold;')
            ui.label('幼儿园信息').style('font-size: 20px; font-weight: bold;')
            ui.label('教师信息').style('font-size: 20px; font-weight: bold;')
            ui.label('学生信息').style('font-size: 20px; font-weight: bold;')
            ui.label('班级信息').style('font-size: 20px; font-weight: bold;')
            ui.label('课程信息').style('font-size: 20px; font-weight: bold;')
            ui.label('活动信息').style('font-size: 20px; font-weight: bold;')
            ui.label('退出').style('font-size: 20px; font-weight: bold;')
        with ui.header().style('background-color:rgb(50, 113, 201);')\
                .classes('items-center justify-between'):
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu')\
                .props('flat color=white')
            ui.image('./web/static/title.png').\
                style('width: 150px; height: 30px')





    def show_all_elements(self):
        self.show_header()
        self.show_footer()
        # self.show_left_drawer()


webframework = WebPageLayout()
webframework.show_all_elements()
ui.run()