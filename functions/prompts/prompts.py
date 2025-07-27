'''
Author: ywyz@admin@ywyz.tech
Date: 2025-07-26 15:57:35
LastEditors: ywyz@admin@ywyz.tech
LastEditTime: 2025-07-26 16:03:04
FilePath: \KindergardenManager\functions\prompts\prompts.py
Description: https://github.com/ywyz

Copyright (c) 2025 by $ywyz@admin@ywyz.tech, All Rights Reserved. 
'''


class prompts:
    def __init__(self):
        self.prompts = {
            "promptname": " ",
            "prompt": " ",
            "outputformat": " ",
            "gradename": " ",
            "outputsubject": " "
        }

    def get_prompt(self, prompt_name):
        if prompt_name in self.prompts:
            return self.prompts[prompt_name]
        else:
            raise ValueError(f"Prompt '{prompt_name}' not found.")
    
    def set_prompt(self, prompt_name, prompt_value):
        if prompt_name in self.prompts:
            self.prompts[prompt_name] = prompt_value
        else:
            raise ValueError(f"Prompt '{prompt_name}' not found.")
        
    def get_all_prompts(self):
        return self.prompts
    
    def clear_prompts(self):
        self.prompts = {
            "promptname": " ",
            "prompt": " ",
            "outputformat": " ",
            "gradename": " ",
            "outputsubject": " "
        }

    def submit_prompt(self, prompt_name, prompt_value):
        self.set_prompt(prompt_name, prompt_value)
        print(f"Prompt '{prompt_name}' submitted with value: {prompt_value}")