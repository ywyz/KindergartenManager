from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from .promptinsert_ui import Ui_Form
from functions.prompts.promptsql import PromptSql

class PromptInsertWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 信号绑定
        self.commit.clicked.connect(self.on_commit)
        self.clear.clicked.connect(self.clear_fields)
        self.exit.clicked.connect(self.exit_form)

    def on_commit(self):
        prompt = self.insert_prompt()
        if prompt is None:
            return
        prompt_sql = PromptSql()
        result = prompt_sql.insert_prompt(prompt)
        if result:
            QMessageBox.information(self, "成功", "提示词插入成功！")
            self.exit_form()
        else:
            QMessageBox.critical(self, "错误", "提示词插入失败！")

    # 其余 insert_prompt、clear_fields、exit_form 方法可直接复用 Ui_Form 的实现
    # 如果需要自定义，可以在此处重写

if __name__ == "__main__":
    app = QApplication([])
    window = PromptInsertWindow()
    window.show()
    app.exec()