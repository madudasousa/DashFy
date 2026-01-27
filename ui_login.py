# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(645, 533)
        Form.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        Form.setStyleSheet(u"	background-color:rgb(178, 158, 255)")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 180, 401, 291))
        font = QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(100, 60, 211, 21))
        font1 = QFont()
        font1.setPointSize(11)
        self.txt_user.setFont(font1)
        self.txt_user.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_user.setAlignment(Qt.AlignCenter)
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(100, 130, 211, 21))
        self.txt_password.setFont(font1)
        self.txt_password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.QPushButton = QPushButton(self.frame)
        self.QPushButton.setObjectName(u"QPushButton")
        self.QPushButton.setGeometry(QRect(130, 210, 151, 31))
        self.QPushButton.setFont(font1)
        self.QPushButton.setLayoutDirection(Qt.LeftToRight)
        self.QPushButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" 	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:rgb(0, 0, 0);\n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 70, 141, 121))
        self.label.setPixmap(QPixmap(u"img/user.png"))
        self.label.setScaledContents(True)
        self.label.raise_()
        self.frame.raise_()
        QWidget.setTabOrder(self.txt_user, self.txt_password)
        QWidget.setTabOrder(self.txt_password, self.QPushButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Form", u"User", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.QPushButton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label.setText("")
    # retranslateUi

