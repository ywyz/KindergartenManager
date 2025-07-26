'''
Author: ywyz@admin@ywyz.tech
Date: 2025-07-26 12:36:48
LastEditors: ywyz@admin@ywyz.tech
LastEditTime: 2025-07-26 13:44:14
FilePath: \KindergardenManager\ui\UI_insertPormpt.py
Description: https://github.com/ywyz
Copyright (c) 2025 by ${git_name_email}, All Rights Reserved. 
'''

from PySide6.QtWidgets import QWidget, Qapplication, QMessageBox
from .promptinsert_ui import Ui_PromptInsert
class PromptInsert(QWidget, Ui_PromptInsert):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        pass