# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QStackedWidget,
    QTabWidget, QTableView, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 661)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(214, 207, 242);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 35))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_home)

        self.btn_import = QPushButton(self.frame)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(0, 35))
        self.btn_import.setFont(font)
        self.btn_import.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_import.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_import)

        self.btn_table = QPushButton(self.frame)
        self.btn_table.setObjectName(u"btn_table")
        self.btn_table.setMinimumSize(QSize(0, 35))
        self.btn_table.setFont(font)
        self.btn_table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_table.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_table)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 35))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 35))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_contato)


        self.verticalLayout_8.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"\n"
"background-color: rgb(214, 207, 242);")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setSizeIncrement(QSize(0, 0))
        self.label.setStyleSheet(u"\n"
"background-color: rgb(244, 242, 248);")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lbl_logo = QLabel(self.pg_home)
        self.lbl_logo.setObjectName(u"lbl_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_logo.sizePolicy().hasHeightForWidth())
        self.lbl_logo.setSizePolicy(sizePolicy)
        self.lbl_logo.setStyleSheet(u"background-color: rgb(244, 242, 248);")
        self.lbl_logo.setScaledContents(False)
        self.lbl_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_logo)

        self.label_47 = QLabel(self.pg_home)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"background-color: rgb(244, 242, 248);")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_47)

        self.btn_cadastro = QPushButton(self.pg_home)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_cadastro.setFont(font1)
        self.btn_cadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastro.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.verticalLayout.addWidget(self.btn_cadastro)

        self.Pages.addWidget(self.pg_home)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.verticalLayout_9 = QVBoxLayout(self.pg_import)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_27 = QLabel(self.pg_import)
        self.label_27.setObjectName(u"label_27")
        font2 = QFont()
        font2.setPointSize(25)
        self.label_27.setFont(font2)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_27)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_file = QLineEdit(self.pg_import)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 28))
        font3 = QFont()
        font3.setPointSize(12)
        self.txt_file.setFont(font3)
        self.txt_file.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.pg_import)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(120, 28))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.btn_open.setFont(font4)
        self.btn_open.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-top-right-radius: 15px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_open)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_28 = QLabel(self.pg_import)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_17.addWidget(self.label_28)

        self.btn_importar = QPushButton(self.pg_import)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setMinimumSize(QSize(0, 35))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.btn_importar.setFont(font5)
        self.btn_importar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_importar.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.horizontalLayout_17.addWidget(self.btn_importar)

        self.label_29 = QLabel(self.pg_import)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_17.addWidget(self.label_29)


        self.verticalLayout_9.addLayout(self.horizontalLayout_17)

        self.progressBar = QProgressBar(self.pg_import)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_9.addWidget(self.progressBar)

        self.Pages.addWidget(self.pg_import)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_7 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_32 = QLabel(self.pg_contato)
        self.label_32.setObjectName(u"label_32")
        font6 = QFont()
        font6.setPointSize(20)
        self.label_32.setFont(font6)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_32)

        self.label_14 = QLabel(self.pg_contato)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_14)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_39 = QLabel(self.pg_contato)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_26.addWidget(self.label_39)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_37 = QLabel(self.pg_contato)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(80, 80))
        self.label_37.setPixmap(QPixmap(u":/img/img/email.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_37)

        self.label_33 = QLabel(self.pg_contato)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_21.addWidget(self.label_33)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_21)

        self.label_40 = QLabel(self.pg_contato)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_26.addWidget(self.label_40)


        self.verticalLayout_7.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_41 = QLabel(self.pg_contato)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_25.addWidget(self.label_41)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_36 = QLabel(self.pg_contato)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(80, 80))
        self.label_36.setPixmap(QPixmap(u":/img/img/phone.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_36)

        self.label_34 = QLabel(self.pg_contato)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_22.addWidget(self.label_34)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_22)

        self.label_42 = QLabel(self.pg_contato)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_25.addWidget(self.label_42)


        self.verticalLayout_7.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_43 = QLabel(self.pg_contato)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_24.addWidget(self.label_43)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_35 = QLabel(self.pg_contato)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(80, 80))
        self.label_35.setPixmap(QPixmap(u":/img/img/rede.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_35)

        self.label_38 = QLabel(self.pg_contato)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777215, 80))

        self.horizontalLayout_23.addWidget(self.label_38)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_23)

        self.label_44 = QLabel(self.pg_contato)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_24.addWidget(self.label_44)


        self.verticalLayout_7.addLayout(self.horizontalLayout_24)

        self.Pages.addWidget(self.pg_contato)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_5 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_31 = QLabel(self.pg_sobre)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 0))
        self.label_31.setMaximumSize(QSize(16777215, 50))
        self.label_31.setFont(font6)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_31)

        self.label_9 = QLabel(self.pg_sobre)
        self.label_9.setObjectName(u"label_9")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(False)
        self.label_9.setFont(font7)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_9)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_14 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_25 = QLabel(self.pg_cadastro)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font6)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_25)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font8 = QFont()
        font8.setPointSize(11)
        self.label_6.setFont(font8)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, -1, -1, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"color: rgba(211, 239, 251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 155, 155,0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_9.addWidget(self.txt_nome)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, 0, -1, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"color: rgba(211, 239, 251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 155, 155,0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")

        self.horizontalLayout_8.addWidget(self.txt_usuario)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, 0, -1, -1)
        self.label_senha = QLabel(self.pg_cadastro)
        self.label_senha.setObjectName(u"label_senha")

        self.horizontalLayout_7.addWidget(self.label_senha)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color: rgba(211, 239, 251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 155, 155,0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_14.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(50, -1, -1, -1)
        self.label_15 = QLabel(self.pg_cadastro)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_6.addWidget(self.label_15)

        self.txt_senha2 = QLineEdit(self.pg_cadastro)
        self.txt_senha2.setObjectName(u"txt_senha2")
        self.txt_senha2.setStyleSheet(u"color: rgba(211, 239, 251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 155, 155,0.1);\n"
"font-family: Trebuchet MS;\n"
"font-size:21px;")
        self.txt_senha2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(50, -1, -1, -1)
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setFont(font4)
        self.cb_perfil.setStyleSheet(u"color: rgb(75, 63, 114);")

        self.horizontalLayout_10.addWidget(self.cb_perfil)


        self.verticalLayout_14.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_19.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.horizontalLayout_19.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_19.addWidget(self.label_13)


        self.verticalLayout_14.addLayout(self.horizontalLayout_19)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_6 = QVBoxLayout(self.pg_table)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tb_base = QTabWidget(self.pg_table)
        self.tb_base.setObjectName(u"tb_base")
        self.tb_base.setTabBarAutoHide(True)
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.horizontalLayout_4 = QHBoxLayout(self.tables)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_2.addWidget(self.tw_estoque)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_gerar = QPushButton(self.tables)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(100, 27))
        self.btn_gerar.setFont(font1)
        self.btn_gerar.setStyleSheet(u"QPushButton {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #6A4EE8;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_gerar)

        self.btn_estorno = QPushButton(self.tables)
        self.btn_estorno.setObjectName(u"btn_estorno")
        self.btn_estorno.setSizeIncrement(QSize(100, 27))
        self.btn_estorno.setFont(font1)
        self.btn_estorno.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #D6CFF2;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_estorno)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")

        self.verticalLayout_3.addWidget(self.tw_saida)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(2, 2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.tb_base.addTab(self.tables, "")
        self.Tab2 = QWidget()
        self.Tab2.setObjectName(u"Tab2")
        self.verticalLayout_18 = QVBoxLayout(self.Tab2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_30 = QLabel(self.Tab2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font6)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_30)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_chart = QPushButton(self.Tab2)
        self.btn_chart.setObjectName(u"btn_chart")
        self.btn_chart.setFont(font5)
        self.btn_chart.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_chart)

        self.btn_excel = QPushButton(self.Tab2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setFont(font5)
        self.btn_excel.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6E1F2;\n"
"    color: #3D355A;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #7C5CFA;\n"
"    color: white;\n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_excel)


        self.verticalLayout_18.addLayout(self.horizontalLayout_18)

        self.txt_filtro = QLineEdit(self.Tab2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setMinimumSize(QSize(0, 28))
        self.txt_filtro.setFont(font3)
        self.txt_filtro.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.txt_filtro)

        self.tb_estoque = QTableView(self.Tab2)
        self.tb_estoque.setObjectName(u"tb_estoque")

        self.verticalLayout_18.addWidget(self.tb_estoque)

        self.tb_base.addTab(self.Tab2, "")

        self.verticalLayout_6.addWidget(self.tb_base)

        self.Pages.addWidget(self.pg_table)

        self.verticalLayout_8.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)
        self.tb_base.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.btn_table.setText(QCoreApplication.translate("MainWindow", u"TABLES", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7c5cfa;\">DASHFY</span></p></body></html>", None))
        self.lbl_logo.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#6b5ca5;\">Veja. Controle. Decida.</span></p></body></html>", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USU\u00c1RIO", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4b3f72;\">Importar XML</span></p></body></html>", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione as pastas com os arquivos XML", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_28.setText("")
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_29.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4b3f72;\">Contato</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">Desenvolvedora: Maria Eduarda</span></p></body></html>", None))
        self.label_39.setText("")
        self.label_37.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#4b3f72;\">eduardadesampaio.maria@hotmail.com</span></p></body></html>", None))
        self.label_40.setText("")
        self.label_41.setText("")
        self.label_36.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">(11) 98432-8959</span></p></body></html>", None))
        self.label_42.setText("")
        self.label_43.setText("")
        self.label_35.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">Dashfy</span></p></body></html>", None))
        self.label_44.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4b3f72;\">Sobre</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#4b3f72;\">O Dashfy \u00e9 um sistema de gerenciamento desenvolvido em Python, projetado para facilitar o controle de estoque por meio da importa\u00e7\u00e3o de arquivos XML de notas fiscais.</span></p><p align=\"center\"><span style=\" font-size:14pt; color:#4b3f72;\">A partir da entrada das notas, o sistema organiza e registra automaticamente os produtos no estoque, permitindo ao usu\u00e1rio acompanhar movimenta\u00e7\u00f5es, realizar sa\u00eddas, estornos e manter o hist\u00f3rico de opera\u00e7\u00f5es de forma clara e segura.</span></p><p align=\"center\"><span style=\" font-size:14pt; color:#4b3f72;\">O Dashfy oferece uma interface intuitiva, focada em agilidade, confiabilidade e apoio \u00e0 tomada de decis\u00f5es no dia a dia.</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4b3f72;\">Tela de Cadastro</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"img/cadastro.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#4b3f72;\">Nome:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#4b3f72;\">Usu\u00e1rio:</span></p></body></html>", None))
        self.label_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#4b3f72;\">Senha:</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#4b3f72;\">Confirmar senha:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#4b3f72;\">Perfil:</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#4b3f72;\">ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Valor Nfe", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Especie", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"UN", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Cod Item", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar sa\u00edda", None))
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#4b3f72;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data Importa", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"S\u00e9rio", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"NFe", None));
        self.tb_base.setTabText(self.tb_base.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4b3f72;\">Estoque</span></p></body></html>", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.Tab2), QCoreApplication.translate("MainWindow", u"Estoque", None))
    # retranslateUi

