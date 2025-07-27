r'''
Author: ywyz@admin@ywyz.tech
Date: 2025-07-27 15:00:55
LastEditors: ywyz@admin@ywyz.tech
LastEditTime: 2025-07-27 15:12:28
FilePath: \KindergardenManager\database\db_init.py
Description: https://github.com/ywyz

Copyright (c) 2025 by $ywyz@admin@ywyz.tech, All Rights Reserved. 
'''

from models.utils import prompts

Models = [prompts]


def initialize_database():
    for model in Models:
        if not model.table_exists():
            model.create_table()
            print(f"已创建表: {model.__name__}")
        else:
            print(f"表已存在，跳过: {model.__name__}")

