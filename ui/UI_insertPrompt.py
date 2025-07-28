from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from ui.promptinsert_ui import Ui_Form
from functions.prompts.prompt import add_prompt


class PromptInsertWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 信号绑定
        self.submit.clicked.connect(self.on_submit)
        self.clear.clicked.connect(self.clear_fields)
        self.exit.clicked.connect(self.exit_form)

    def on_submit(self):
        result = add_prompt(
            name=self.promptname.text(),
            grade=self.grade.currentText(),
            subject=self.subject.text(),
            content=self.prompt.toPlainText(),
            output_format=self.outputformat.toPlainText()
        )
        if result:
            QMessageBox.information(self, "成功", "提示词插入成功！")
        else:
            QMessageBox.critical(self, "错误", "提示词插入失败！")

    def clear_fields(self):
        self.promptname.clear()
        self.grade.setCurrentIndex(0)
        self.subject.clear()
        self.prompt.clear()
        self.outputformat.clear()

    def exit_form(self):
        self.close()
        # 这里可以添加其他退出逻辑，比如保存状态等


if __name__ == "__main__":
    app = QApplication([])
    window = PromptInsertWindow()
    window.show()
    app.exec()