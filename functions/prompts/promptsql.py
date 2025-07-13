'''
Date: 2025-07-09 17:28:21
Author: ywyz
LastModifiedBy: ywyz
Github: https://github.com/ywyz
LastEditors: ywyz
LastEditTime: 2025-07-10 15:27:38
'''
from database.sqlconnect import SQLConnect

class PromptSql:
    def __init__(self):
        self.sql_connect = SQLConnect()

    def insert_prompt(self, prompt):
        query = "INSERT INTO ai_templates (prompt) VALUES (%s)"
        params = (prompt,)
        result = self.sql_connect.execute_query(query, params)
        return result

    def get_all_prompts(self):
        return self.sql_connect.get_all("prompts")

    def get_prompt_by_id(self, id):
        return self.sql_connect.get_by_id("prompts", id)