'''
Author: ywyz@admin@ywyz.tech
Date: 2025-07-26 13:31:10
LastEditors: ywyz@admin@ywyz.tech
LastEditTime: 2025-07-27 15:01:48
FilePath: \KindergardenManager\database\models\BaseModel.py
Description: https://github.com/ywyz

Copyright (c) 2025 by $ywyz@admin@ywyz.tech, All Rights Reserved. 
'''

import os
from peewee import Model, AutoField, DateTimeField, MySQLDatabase

from datetime import datetime

kindergarten_db = MySQLDatabase(
            'kindergarten',
            user=os.getenv('SQL_USER'),
            password=os.getenv('SQL_PASSWORD'),
            host=os.getenv('SQL_HOST'),
            port=int(os.getenv('SQL_PORT'))
        )


class BaseModel(Model):
    id = AutoField(primary_key=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)
    
    class Meta:
        database = kindergarten_db
        legacy_table_names = False  # 禁用旧式表名