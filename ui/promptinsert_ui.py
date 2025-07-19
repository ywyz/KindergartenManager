# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'promptinsert.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 720)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1070, 180, 161, 221))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.commit = QPushButton(self.layoutWidget)
        self.commit.setObjectName(u"commit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commit.sizePolicy().hasHeightForWidth())
        self.commit.setSizePolicy(sizePolicy)
        self.commit.setMinimumSize(QSize(159, 0))

        self.verticalLayout_2.addWidget(self.commit)

        self.clear = QPushButton(self.layoutWidget)
        self.clear.setObjectName(u"clear")
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        self.clear.setMinimumSize(QSize(159, 0))

        self.verticalLayout_2.addWidget(self.clear)

        self.exit = QPushButton(self.layoutWidget)
        self.exit.setObjectName(u"exit")
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QSize(159, 0))

        self.verticalLayout_2.addWidget(self.exit)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(270, 40, 711, 621))
        self.formLayout = QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.promptname = QLineEdit(self.layoutWidget1)
        self.promptname.setObjectName(u"promptname")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.promptname)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.grade_choose = QComboBox(self.layoutWidget1)
        self.grade_choose.addItem("")
        self.grade_choose.addItem("")
        self.grade_choose.addItem("")
        self.grade_choose.setObjectName(u"grade_choose")
        self.grade_choose.setEditable(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.grade_choose)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.subject_choose = QComboBox(self.layoutWidget1)
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.addItem("")
        self.subject_choose.setObjectName(u"subject_choose")
        self.subject_choose.setEditable(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.subject_choose)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.prompt = QPlainTextEdit(self.layoutWidget1)
        self.prompt.setObjectName(u"prompt")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.prompt)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.outputformat = QPlainTextEdit(self.layoutWidget1)
        self.outputformat.setObjectName(u"outputformat")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.outputformat)


        self.retranslateUi(Form)

        self.grade_choose.setCurrentIndex(0)
        self.subject_choose.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u63d0\u793a\u8bcd\u63d2\u5165\u7cfb\u7edf", None))
        self.commit.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4", None))
        self.clear.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.exit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u63d0\u793a\u8bcd\u540d\u79f0\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5e74\u7ea7\u7ec4\uff1a", None))
        self.grade_choose.setItemText(0, QCoreApplication.translate("Form", u"\u5c0f\u73ed", None))
        self.grade_choose.setItemText(1, QCoreApplication.translate("Form", u"\u4e2d\u73ed", None))
        self.grade_choose.setItemText(2, QCoreApplication.translate("Form", u"\u5927\u73ed", None))

        self.grade_choose.setCurrentText(QCoreApplication.translate("Form", u"\u5c0f\u73ed", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u79d1\u76ee\uff1a", None))
        self.subject_choose.setItemText(0, QCoreApplication.translate("Form", u"\u79d1\u5b66", None))
        self.subject_choose.setItemText(1, QCoreApplication.translate("Form", u"\u4f53\u80fd\u5927\u5faa\u73af\u2014\u2014\u96c6\u4f53\u6d3b\u52a8", None))
        self.subject_choose.setItemText(2, QCoreApplication.translate("Form", u"\u4f53\u80fd\u5927\u5faa\u73af\u2014\u2014\u81ea\u9009\u6d3b\u52a8", None))
        self.subject_choose.setItemText(3, QCoreApplication.translate("Form", u"\u827a\u672f", None))
        self.subject_choose.setItemText(4, QCoreApplication.translate("Form", u"\u5065\u5eb7", None))
        self.subject_choose.setItemText(5, QCoreApplication.translate("Form", u"\u8bed\u8a00", None))
        self.subject_choose.setItemText(6, QCoreApplication.translate("Form", u"\u793e\u4f1a", None))
        self.subject_choose.setItemText(7, QCoreApplication.translate("Form", u"\u6668\u95f4\u8c08\u8bdd", None))
        self.subject_choose.setItemText(8, QCoreApplication.translate("Form", u"\u96c6\u4f53\u6d3b\u52a8", None))
        self.subject_choose.setItemText(9, QCoreApplication.translate("Form", u"\u6237\u5916\u6d3b\u52a8", None))
        self.subject_choose.setItemText(10, QCoreApplication.translate("Form", u"\u4e13\u7528\u5ba4\u2014\u2014\u6c99\u753b\u574a", None))
        self.subject_choose.setItemText(11, QCoreApplication.translate("Form", u"\u4e13\u7528\u5ba4\u2014\u2014\u79d1\u5b66\u5ba4", None))
        self.subject_choose.setItemText(12, QCoreApplication.translate("Form", u"\u4e13\u7528\u5ba4\u2014\u2014\u9605\u89c8\u5ba4", None))
        self.subject_choose.setItemText(13, QCoreApplication.translate("Form", u"\u4e13\u7528\u5ba4\u2014\u2014\u70d8\u7119\u574a", None))
        self.subject_choose.setItemText(14, QCoreApplication.translate("Form", u"\u4e13\u7528\u5ba4\u2014\u2014\u5efa\u6784\u574a", None))
        self.subject_choose.setItemText(15, QCoreApplication.translate("Form", u"\u4e13\u7528\u5ba4\u2014\u2014\u624e\u67d3\u574a", None))
        self.subject_choose.setItemText(16, QCoreApplication.translate("Form", u"\u533a\u57df\u6d3b\u52a8", None))

        self.subject_choose.setCurrentText(QCoreApplication.translate("Form", u"\u79d1\u5b66", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u63d0\u793a\u8bcd\u5185\u5bb9\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u683c\u5f0f\uff1a", None))
    # retranslateUi

