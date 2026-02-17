# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(645, 533)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        Form.setStyleSheet(u"background-color: rgb(244, 241, 251);\n"
"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(120, 70, 411, 361))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 100))
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setStyleSheet(u"QLabel {\n"
"    background-color: #5E3F9C;\n"
"    border-radius: 50px;\n"
"	padding: 10px;\n"
"}")
        self.label.setPixmap(QPixmap(u"img/login.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(400, 0))
        self.frame.setMaximumSize(QSize(420, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"QFrame{\n"
"    background-color: white;\n"
"    border-radius: 14px;\n"
"    padding: 20px;\n"
"	 border: 1px solid #E6DFF5;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"color: rgb(76, 29, 149);")
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_user)

        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet(u"color: rgb(76, 29, 149);")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_password)

        self.QPushButton = QPushButton(self.frame)
        self.QPushButton.setObjectName(u"QPushButton")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.QPushButton.setFont(font1)
        self.QPushButton.setLayoutDirection(Qt.LeftToRight)
        self.QPushButton.setStyleSheet(u"QPushButton{\n"
"    background: #6C4AB6;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 5px 20px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton:hover {\n"
"    background: #5A3AA0;\n"
"}\n"
"QPushButton:disabled {\n"
"    background: #C8BEE6;\n"
"    color: #FFFFFF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: #4E368E; \n"
"}")

        self.verticalLayout.addWidget(self.QPushButton)


        self.verticalLayout_2.addWidget(self.frame)

        QWidget.setTabOrder(self.txt_user, self.txt_password)
        QWidget.setTabOrder(self.txt_password, self.QPushButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.txt_user.setPlaceholderText(QCoreApplication.translate("Form", u"User", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.QPushButton.setText(QCoreApplication.translate("Form", u"Login", None))
    # retranslateUi

