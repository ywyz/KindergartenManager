from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from ui.promptinsert_ui import Ui_Form
from ..functions.prompts.prompt import add_prompt


class PromptInsertWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 信号绑定
        self.commit.clicked.connect(self.on_commit)
        self.clear.clicked.connect(self.clear_fields)
        self.exit.clicked.connect(self.exit_form)

    def on_commit(self):
        result = add_prompt(
            name=self.name.text(),
            grade=self.grade.currentText(),
            subject=self.subject.currentText(),
            content=self.content.toPlainText(),
            output_format=self.output_format.currentText()
        )
        if result:
            QMessageBox.information(self, "成功", "提示词插入成功！")
            self.exit_form()
        else:
            QMessageBox.critical(self, "错误", "提示词插入失败！")


if __name__ == "__main__":
    app = QApplication([])
    window = PromptInsertWindow()
    window.show()
    app.exec()
    window.exit_form = lambda: window.close()  # 退出窗口的简化方法