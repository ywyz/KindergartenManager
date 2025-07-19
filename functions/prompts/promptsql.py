'''
Date: 2025-07-09 17:28:21
Author: ywyz
LastModifiedBy: ywyz
Github: https://github.com/ywyz
LastEditors: ywyz
LastEditTime: 2025-07-19 09:19:51
'''
import time
from database.sqlconnect import SQLConnect

class PromptSql:
    def __init__(self):
        self.sql_connect = SQLConnect()

    def insert_prompt(self, prompt):
        # 假设 ai_templates 表有 name, grade, subject, content, output_format 字段
        query = "INSERT INTO ai_templates (promptname, prompt, outputformat,gradename,outputsubject) VALUES (%s,%s, %s, %s, %s)"
        params = (
            prompt.get("name"),
            prompt.get("content"),
            prompt.get("output_format"),
            prompt.get("grade"),
            prompt.get("subject"),
        )
        try:
            result = self.sql_connect.execute_query(query, params)
            # 如果没有异常，认为插入成功
            return True
        except Exception as e:
            print(f"插入失败: {e}")
            return False

    def get_all_prompts(self):
        return self.sql_connect.get_all("prompts")

    def get_prompt_by_id(self, id):
        return self.sql_connect.get_by_id("prompts", id)