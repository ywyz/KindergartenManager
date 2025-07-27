'''
Author: ywyz@admin@ywyz.tech
Date: 2025-07-27 15:36:54
LastEditors: ywyz@admin@ywyz.tech
LastEditTime: 2025-07-27 15:54:17
FilePath: \KindergardenManager\database\crud.py
Description: https://github.com/ywyz

Copyright (c) 2025 by $ywyz@admin@ywyz.tech, All Rights Reserved. 
'''
from models.utils import prompts


def create_prompt(**kwargs):
    return prompts.create(**kwargs)


def get_prompt_by_id(prompt_id):
    return prompts.get_or_none(prompts.id == prompt_id)


def update_prompt(prompt_id, **kwargs):
    query = prompts.update(**kwargs).where(prompts.id == prompt_id)
    return query.execute()


def delete_prompt(prompt_id):
    query = prompts.delete().where(prompts.id == prompt_id)
    return query.execute()