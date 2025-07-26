'''
Author: ywyz@admin@ywyz.tech
Date: 2025-07-26 13:31:10
LastEditors: ywyz@admin@ywyz.tech
LastEditTime: 2025-07-26 14:25:51
FilePath: \KindergardenManager\database\SQLdatabase.py
Description: https://github.com/ywyz

Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''
from peewee import MySQLDatabase
import os


class SQLDatabase:
    def __init__(self):
        self.kindergarden_db = MySQLDatabase(
            'kindergarten',
            user=os.getenv('SQL_USER'),
            password=os.getenv('SQL_PASSWORD'),
            host=os.getenv('SQL_HOST'),
            port=int(os.getenv('SQL_PORT'))
        )

    def connect(self):
        try:
            self.kindergarden_db.connect()
            print("Database connection successful.")
        except Exception as e:
            print(f"Failed to connect to the database: {e}")

    def close(self):
        if self.kindergarden_db.is_closed():
            print("Database connection is already closed.")
        else:
            self.kindergarden_db.close()
            print("Database connection closed.")

    def execute_query(self, query):
        try:
            with self.kindergarden_db.atomic():
                result = self.kindergarden_db.execute_sql(query)
                return result.fetchall()
        except Exception as e:
            print(f"Query execution failed: {e}")
            return None


