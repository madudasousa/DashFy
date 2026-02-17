# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableView,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 802)
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
        self.frame.setStyleSheet(u"background-color: rgb(108, 74, 182);")
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
"    background: transparent;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255,255,255,0.15);\n"
"	border-radius: 6px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_home)

        self.btn_import = QPushButton(self.frame)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(0, 35))
        self.btn_import.setFont(font)
        self.btn_import.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_import.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255,255,255,0.15);\n"
"	border-radius: 6px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_import)

        self.btn_table = QPushButton(self.frame)
        self.btn_table.setObjectName(u"btn_table")
        self.btn_table.setMinimumSize(QSize(0, 35))
        self.btn_table.setFont(font)
        self.btn_table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_table.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255,255,255,0.15);\n"
"	border-radius: 6px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_table)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 35))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255,255,255,0.15);\n"
"	border-radius: 6px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 35))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton {\n"
"	background-color: #5E3F9C;\n"
"    background: transparent;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #4B2E8A;\n"
"    background: rgba(255,255,255,0.15);\n"
"	border-radius: 6px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_contato)


        self.verticalLayout_8.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        font1 = QFont()
        font1.setPointSize(18)
        self.Pages.setFont(font1)
        self.Pages.setStyleSheet(u"background-color: rgb(244, 241, 251);\n"
"")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_11 = QVBoxLayout(self.pg_home)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.pg_home)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"    background-color: white;\n"
"    border-radius: 14px;\n"
"    padding: 20px;\n"
"	 border: 1px solid #E6DFF5;\n"
"}\n"
"QFrame QLabel {\n"
"    background: transparent;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 30, 40, 30)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setSizeIncrement(QSize(0, 0))
        self.label.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"background-color:rgb(108, 74, 182)\n"
"")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lbl_logo = QLabel(self.frame_6)
        self.lbl_logo.setObjectName(u"lbl_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_logo.sizePolicy().hasHeightForWidth())
        self.lbl_logo.setSizePolicy(sizePolicy)
        self.lbl_logo.setMaximumSize(QSize(16777215, 200))
        self.lbl_logo.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"background-color: rgb(244, 242, 248);\n"
"")
        self.lbl_logo.setScaledContents(False)
        self.lbl_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_logo)

        self.label_47 = QLabel(self.frame_6)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"background-color: rgb(244, 242, 248);")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_47)

        self.btn_cadastro = QPushButton(self.frame_6)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.btn_cadastro.setFont(font2)
        self.btn_cadastro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastro.setStyleSheet(u"QPushButton{\n"
"    background: #F3F0FA;\n"
"    color: #4B3F72;\n"
"    border: 1px solid #D8CFF0;\n"
"    border-radius: 12px;\n"
"    padding: 10px 18px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #E9E2FB;\n"
"    border: 1px solid #6C4BC6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #DCD3F5;\n"
"    border: 1px solid #5A3FB0;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_cadastro)


        self.verticalLayout_16.addLayout(self.verticalLayout)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.Pages.addWidget(self.pg_home)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.horizontalLayout_11 = QHBoxLayout(self.pg_import)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_2 = QFrame(self.pg_import)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 600))
        self.frame_2.setMaximumSize(QSize(16777215, 900))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"    background-color: white;\n"
"    border-radius: 14px;\n"
"    padding: 20px;\n"
"	 border: 1px solid #E6DFF5;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_27 = QLabel(self.frame_2)
        self.label_27.setObjectName(u"label_27")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy2)
        self.label_27.setMaximumSize(QSize(16777215, 100))
        font3 = QFont()
        font3.setPointSize(30)
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_27)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(24, 18, 24, 18)
        self.txt_file = QLineEdit(self.frame_2)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setPointSize(12)
        self.txt_file.setFont(font4)
        self.txt_file.setStyleSheet(u"QLineEdit {\n"
"    background: #F6F3FD;\n"
"    border: 1px solid #E3DBF5;\n"
"    border-radius: 10px;\n"
"    padding: 8px 12px;\n"
"    color: #2E2E2E;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #6C4AB6;\n"
"    background: #FFFFFF;\n"
"}")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.frame_2)
        self.btn_open.setObjectName(u"btn_open")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy3)
        self.btn_open.setMinimumSize(QSize(120, 32))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.btn_open.setFont(font5)
        self.btn_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"	 background: #FFFFFF;\n"
"    border: 1px solid #D8CEF2;\n"
"    color: #4A3F65;\n"
"    border-radius: 12px;\n"
"    padding: 10px 18px;\n"
"    min-height: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: #F2EDFF;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_open)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.btn_importar = QPushButton(self.frame_2)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setMinimumSize(QSize(240, 44))
        self.btn_importar.setMaximumSize(QSize(240, 16777215))
        self.btn_importar.setFont(font5)
        self.btn_importar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_importar.setStyleSheet(u"QPushButton#btn_importar {\n"
"    background: #6C4BC6;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 10px 20px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btn_importar:hover {\n"
"    background: #5A3FA3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #4E368E; \n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_importar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: #E4DAF7;\n"
"    text-align: center;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 8px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #7B5CF0,\n"
"        stop:1 #9F7AEA\n"
"    );\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_9.addWidget(self.progressBar)


        self.horizontalLayout_11.addWidget(self.frame_2)

        self.Pages.addWidget(self.pg_import)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_4 = QFrame(self.pg_contato)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"    background-color: white;\n"
"    border-radius: 14px;\n"
"    padding: 20px;\n"
"	 border: 1px solid #E6DFF5;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_32 = QLabel(self.frame_4)
        self.label_32.setObjectName(u"label_32")
        font6 = QFont()
        font6.setPointSize(20)
        self.label_32.setFont(font6)
        self.label_32.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_32)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_14)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(16)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_40 = QLabel(self.frame_4)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_21.addWidget(self.label_40)

        self.label_37 = QLabel(self.frame_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(80, 80))
        self.label_37.setStyleSheet(u"QLabel {\n"
"    background-color: #5E3F9C;\n"
"    border-radius: 30px;\n"
"	padding: 10px;\n"
"}")
        self.label_37.setPixmap(QPixmap(u"img/email.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_37)

        self.label_33 = QLabel(self.frame_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_21.addWidget(self.label_33)

        self.label_39 = QLabel(self.frame_4)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_21.addWidget(self.label_39)


        self.verticalLayout_7.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_41 = QLabel(self.frame_4)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_25.addWidget(self.label_41)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(16)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_36 = QLabel(self.frame_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(80, 80))
        self.label_36.setStyleSheet(u"QLabel {\n"
"    background-color: #5E3F9C;\n"
"    border-radius: 30px;\n"
"	padding: 10px;\n"
"}")
        self.label_36.setPixmap(QPixmap(u"img/linkedin.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_36)

        self.label_34 = QLabel(self.frame_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.label_34.setWordWrap(False)

        self.horizontalLayout_22.addWidget(self.label_34)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_22)

        self.label_42 = QLabel(self.frame_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_25.addWidget(self.label_42)


        self.verticalLayout_7.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_43 = QLabel(self.frame_4)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_24.addWidget(self.label_43)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(16)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_35 = QLabel(self.frame_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(80, 80))
        self.label_35.setStyleSheet(u"QLabel {\n"
"    background-color: #5E3F9C;\n"
"    border-radius: 30px;\n"
"	padding: 10px;\n"
"}")
        self.label_35.setPixmap(QPixmap(u"img/github.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_35)

        self.label_38 = QLabel(self.frame_4)
        self.label_38.setObjectName(u"label_38")
        sizePolicy1.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy1)
        self.label_38.setMaximumSize(QSize(16777215, 90))
        font7 = QFont()
        font7.setPointSize(4)
        self.label_38.setFont(font7)
        self.label_38.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.label_38.setScaledContents(False)
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_38.setWordWrap(False)
        self.label_38.setMargin(-6)
        self.label_38.setIndent(-4)
        self.label_38.setOpenExternalLinks(False)

        self.horizontalLayout_23.addWidget(self.label_38)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_23)

        self.label_44 = QLabel(self.frame_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_24.addWidget(self.label_44)


        self.verticalLayout_7.addLayout(self.horizontalLayout_24)


        self.verticalLayout_12.addWidget(self.frame_4)

        self.Pages.addWidget(self.pg_contato)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.horizontalLayout_4 = QHBoxLayout(self.pg_sobre)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.pg_sobre)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"    background-color: white;\n"
"    border-radius: 14px;\n"
"    padding: 20px;\n"
"	 border: 1px solid #E6DFF5;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.about_container = QWidget(self.frame_3)
        self.about_container.setObjectName(u"about_container")
        self.about_container.setMaximumSize(QSize(760, 16777215))
        font8 = QFont()
        font8.setPointSize(3)
        self.about_container.setFont(font8)
        self.about_container.setStyleSheet(u"    background: transparent;")
        self.verticalLayout_5 = QVBoxLayout(self.about_container)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(24, 24, 24, 24)
        self.label_31 = QLabel(self.about_container)
        self.label_31.setObjectName(u"label_31")
        sizePolicy2.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy2)
        self.label_31.setMinimumSize(QSize(0, 40))
        self.label_31.setMaximumSize(QSize(16777215, 50))
        font9 = QFont()
        font9.setBold(True)
        self.label_31.setFont(font9)
        self.label_31.setStyleSheet(u"QLabel {\n"
"	font-size: 22px;\n"
"    font-weight: 700;\n"
"    padding: 6px 0;\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_31.setWordWrap(False)

        self.verticalLayout_5.addWidget(self.label_31)

        self.label_9 = QLabel(self.about_container)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(750, 16777215))
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(False)
        self.label_9.setFont(font10)
        self.label_9.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"\n"
"}")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_9.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_4 = QLabel(self.about_container)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: #4b3f72;\n"
"    background: transparent;\n"
"    border: none;\n"
"	padding: 10px;\n"
"}")
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setIndent(0)

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.about_container)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: #4b3f72;\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.label_5.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_5.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_5)


        self.horizontalLayout_5.addWidget(self.about_container)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_13 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_5 = QFrame(self.pg_cadastro)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"    background-color: white;\n"
"    border-radius: 14px;\n"
"    padding: 20px;\n"
"	 border: 1px solid #E6DFF5;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy4)
        self.label_25.setFont(font6)
        self.label_25.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_25)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(140, 140))
        self.label_6.setMaximumSize(QSize(140, 140))
        font11 = QFont()
        font11.setPointSize(11)
        self.label_6.setFont(font11)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    background-color: #5E3F9C;\n"
"    border-radius: 30px;\n"
"	padding: 10px;\n"
"}")
        self.label_6.setPixmap(QPixmap(u"img/cadastro.png"))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(8, -1, 8, -1)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.frame_5)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(0, 38))
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    background: #F6F3FD;\n"
"    border: 1px solid #E3DBF5;\n"
"    border-radius: 10px;\n"
"    padding: 8px 12px;\n"
"    color: #2E2E2E;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #6C4AB6;\n"
"    background: #FFFFFF;\n"
"}")

        self.horizontalLayout_9.addWidget(self.txt_nome)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(8, 0, 8, -1)
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.frame_5)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setMinimumSize(QSize(0, 38))
        self.txt_usuario.setStyleSheet(u"QLineEdit {\n"
"    background: #F6F3FD;\n"
"    border: 1px solid #E3DBF5;\n"
"    border-radius: 10px;\n"
"    padding: 8px 12px;\n"
"    color: #2E2E2E;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #6C4AB6;\n"
"    background: #FFFFFF;\n"
"}")

        self.horizontalLayout_8.addWidget(self.txt_usuario)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(8, 0, 8, -1)
        self.label_senha = QLabel(self.frame_5)
        self.label_senha.setObjectName(u"label_senha")
        self.label_senha.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_senha)

        self.txt_senha = QLineEdit(self.frame_5)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(0, 38))
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"    background: #F6F3FD;\n"
"    border: 1px solid #E3DBF5;\n"
"    border-radius: 10px;\n"
"    padding: 8px 12px;\n"
"    color: #2E2E2E;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #6C4AB6;\n"
"    background: #FFFFFF;\n"
"}")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(8, -1, 8, -1)
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_15)

        self.txt_senha2 = QLineEdit(self.frame_5)
        self.txt_senha2.setObjectName(u"txt_senha2")
        self.txt_senha2.setMinimumSize(QSize(0, 38))
        self.txt_senha2.setStyleSheet(u"QLineEdit {\n"
"    background: #F6F3FD;\n"
"    border: 1px solid #E3DBF5;\n"
"    border-radius: 10px;\n"
"    padding: 8px 12px;\n"
"    color: #2E2E2E;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #6C4AB6;\n"
"    background: #FFFFFF;\n"
"}")
        self.txt_senha2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(50, -1, -1, -1)
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.frame_5)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setMinimumSize(QSize(0, 38))
        self.cb_perfil.setFont(font5)
        self.cb_perfil.setStyleSheet(u"QComboBox {\n"
"    background-color: #EAE6F5;\n"
"    border: 1px solid #B8A9E3;\n"
"    border-radius: 12px;\n"
"    padding: 6px 30px 6px 12px; \n"
"    color: #2E1A6D;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 25px;\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 6px solid #6C4AB6; \n"
"    margin-right: 8px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F6F3FF; \n"
"    color: #2E1A6D;\n"
"    border: 1px solid #B8A9E3;\n"
"    selection-background-color: #6C4AB6;\n"
"    selection-color: white;\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.cb_perfil)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_19.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.frame_5)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font5)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"    background: #6C4AB6;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 10px 20px;\n"
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
"    background: #4E368E;  \n"
"}")

        self.horizontalLayout_19.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_19.addWidget(self.label_13)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)


        self.verticalLayout_13.addWidget(self.frame_5)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_6 = QVBoxLayout(self.pg_table)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tb_base = QTabWidget(self.pg_table)
        self.tb_base.setObjectName(u"tb_base")
        self.tb_base.setFont(font)
        self.tb_base.setAutoFillBackground(False)
        self.tb_base.setStyleSheet(u"QTabWidget::pane {\n"
"    background: white;\n"
"    border: 1px solid #E6DFF5;\n"
"    border-radius: 16px;\n"
"    padding: 18px;\n"
"}\n"
"QTabBar::tab {\n"
"    background: #F3F0FA;\n"
"    color: #4B3F72;\n"
"    font-weight: 600;\n"
"\n"
"    padding: 3px 6px;     \n"
"    min-width: 50px;       \n"
"    min-height: 20px;    \n"
"\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    margin-right: 6px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background: #6C4BC6;\n"
"    color: white;\n"
"}\n"
"")
        self.tb_base.setIconSize(QSize(25, 25))
        self.tb_base.setTabBarAutoHide(True)
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.tables.setStyleSheet(u"QWidget#tables {\n"
"    background: white;\n"
"\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.tables)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #4B3F72;\n"
"    font-weight: 700;\n"
"    letter-spacing: 1px;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_3)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setStyleSheet(u"QTreeWidget {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #E6DFF5;\n"
"    border-radius: 5px;\n"
"    gridline-color: #EDE7FA;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background: #EDE7FA;\n"
"    color: #2D2546;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #F6F3FD;\n"
"    color: #4B3F72;\n"
"    font-weight: 600;\n"
"    padding: 4px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #E6DFF5;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.tw_estoque)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_gerar = QPushButton(self.tables)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setMinimumSize(QSize(100, 27))
        self.btn_gerar.setFont(font5)
        self.btn_gerar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_gerar.setStyleSheet(u"QPushButton{\n"
"    background: #6C4AB6;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 10px 20px;\n"
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

        self.horizontalLayout_3.addWidget(self.btn_gerar)

        self.btn_estorno = QPushButton(self.tables)
        self.btn_estorno.setObjectName(u"btn_estorno")
        self.btn_estorno.setSizeIncrement(QSize(100, 27))
        self.btn_estorno.setFont(font5)
        self.btn_estorno.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_estorno.setStyleSheet(u"QPushButton {\n"
"    background: #F3F0FA;\n"
"    color: #4B3F72;\n"
"    border: 1px solid #D8CFF0;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton:hover {\n"
"    background: #E9E2FB;\n"
"    border: 1px solid #6C4BC6;\n"
"    color: #4B3F72;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: #DDD4F7;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_estorno)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #4B3F72;\n"
"    font-weight: 700;\n"
"    letter-spacing: 1px;\n"
"}")

        self.verticalLayout_3.addWidget(self.label_2)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")
        self.tw_saida.setStyleSheet(u"QTreeWidget {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #E6DFF5;\n"
"    border-radius: 12px;\n"
"    gridline-color: #EDE7FA;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background: #EDE7FA;\n"
"    color: #2D2546;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #F6F3FD;\n"
"    color: #4B3F72;\n"
"    font-weight: 600;\n"
"    padding: 4px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #E6DFF5;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.tw_saida)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(2, 2)

        self.verticalLayout_14.addLayout(self.verticalLayout_4)

        self.tb_base.addTab(self.tables, "")
        self.Tab2 = QWidget()
        self.Tab2.setObjectName(u"Tab2")
        self.Tab2.setStyleSheet(u"QWidget {\n"
"    background: white;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.Tab2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_30 = QLabel(self.Tab2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font6)
        self.label_30.setStyleSheet(u"")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_30)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_chart = QPushButton(self.Tab2)
        self.btn_chart.setObjectName(u"btn_chart")
        self.btn_chart.setFont(font5)
        self.btn_chart.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_chart.setStyleSheet(u"QPushButton#btn_chart {\n"
"    background: #6C4BC6;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton#btn_chart:hover {\n"
"    background: #5A3FA3;\n"
"}\n"
"QPushButton#btn_chart:pressed {\n"
"    background: #4E368E;  \n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_chart)

        self.btn_excel = QPushButton(self.Tab2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setFont(font5)
        self.btn_excel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton#btn_excel {\n"
"    background: #F3F0FA;\n"
"    color: #4B3F72;\n"
"    border: 1px solid #D8CFF0;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton#btn_excel:hover {\n"
"    background: #E9E2FB;\n"
"    border: 1px solid #6C4BC6;\n"
"    color: #4B3F72;\n"
"}\n"
"\n"
"QPushButton#btn_excel:pressed {\n"
"    background: #DDD4F7;\n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_excel)


        self.verticalLayout_15.addLayout(self.horizontalLayout_18)

        self.txt_filtro = QLineEdit(self.Tab2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setMinimumSize(QSize(0, 28))
        self.txt_filtro.setFont(font4)
        self.txt_filtro.setStyleSheet(u"color: rgb(107, 95, 143);\n"
"")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.txt_filtro)

        self.tb_geral = QTableView(self.Tab2)
        self.tb_geral.setObjectName(u"tb_geral")
        self.tb_geral.setStyleSheet(u"QTableView {\n"
"    background: #FFFFFF;\n"
"    border: 1px solid #E6DFF5;\n"
"    border-radius: 10px;\n"
"    gridline-color: #EDE7FA;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #F6F3FD;\n"
"    color: #4B3F72;\n"
"    font-weight: 600;\n"
"    padding: 6px;\n"
"    border: none;\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.tb_geral)

        self.tb_base.addTab(self.Tab2, "")

        self.verticalLayout_6.addWidget(self.tb_base)

        self.Pages.addWidget(self.pg_table)

        self.verticalLayout_8.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tb_base.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"IN\u00cdCIO", None))
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.btn_table.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#4c1d95;\">DASHFY</span></p></body></html>", None))
        self.lbl_logo.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#6b5ca5;\">Veja. Controle. Decida.</span></p></body></html>", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USU\u00c1RIO", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4b3f72;\">Importar XML</span></p></body></html>", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione as pastas com os arquivos XML", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4b3f72;\">Contato</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">Entre em contato ou acesse meus projetos.</span></p></body></html>", None))
        self.label_40.setText("")
        self.label_37.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; opacity: 0.75; color:#4b3f72;\">Email</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">eduardadesampaio.maria@hotmail.com</span></p></body></html>", None))
        self.label_39.setText("")
        self.label_41.setText("")
        self.label_36.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#4b3f72; opacity: 0.75;\">LinkedIn</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">linkedin.com/in/mariaeduardasousa-sampaio</span></p></body></html>", None))
        self.label_42.setText("")
        self.label_43.setText("")
        self.label_35.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#4b3f72; opacity: 0.75;\">GitHub</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">github.com/madudasousa</span></p></body></html>", None))
        self.label_44.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#4b3f72;\">Sobre</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#4b3f72;\">O </span><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">Dashfy</span><span style=\" font-size:14pt; color:#4b3f72;\"> \u00e9 um sistema de gerenciamento de estoque desenvolvido em </span><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">Python</span><span style=\" font-size:14pt; color:#4b3f72;\">, projetado para facilitar o controle de entradas e sa\u00eddas por meio da </span><span style=\" font-size:14pt; font-weight:600; color:#4b3f72;\">importa\u00e7\u00e3o de arquivos XML de NF-e</span><span style=\" font-size:14pt; color:#4b3f72;\">.</span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Principais funcionalidades</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"font-size:12pt; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Importa\u00e7\u00e3o de XML e registro autom\u00e1tico dos itens no banco de dados</li><li style=\"font-size:12pt; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Controle de estoque com <span style=\"font-size:12pt; font-weight:600;\">sa\u00eddas</span> e <span style=\"font-size:12pt; font-weight:600;\">estornos</span></li><li style=\"font-size:12pt; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hist\u00f3rico de movimenta\u00e7\u00f5es por <span style=\"font-size:12pt; font-weight:600;\">usu\u00e1rio</span> e <span style=\"font-size:"
                        "12pt; font-weight:600;\">data</span></li><li style=\"font-size:12pt; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Consulta e organiza\u00e7\u00e3o das informa\u00e7\u00f5es em tabelas para apoio \u00e0 decis\u00e3o</li></ul><p><br/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"  <head/>\n"
"  <body>\n"
"    <p>\n"
"      <span style=\" font-size:12pt; font-weight:600;\">Tecnologias</span>\n"
"    </p>\n"
"    <ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"      <li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"        <span style=\" font-size:12pt;\">Python \u2022 PySide6 \u2022 Qt Designer</span>\n"
"      </li>\n"
"      <li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"        <span style=\" font-size:12pt;\">SQLite (armazenamento)</span>\n"
"      </li>\n"
"      <li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"        <span style=\" font-size:12pt;\">PyInstaller (empacotamento do execut\u00e1vel)</span>\n"
"      </li>\n"
"    </ul>\n"
"  </body>\n"
"</html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#4b3f72;\">Cadastro de Usu\u00e1rio</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#4b3f72;\">Preencha os dados para criar um novo usu\u00e1rio no sistema.</span></p></body></html>", None))
        self.label_6.setText("")
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
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Data Saida", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Usuario ", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"S\u00e9rie", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"NFe", None));
        self.tb_base.setTabText(self.tb_base.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#4b3f72;\">Geral</span></p></body></html>", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_filtro.setText(QCoreApplication.translate("MainWindow", u"\U0001f50d  Filtrar por usu\U000000e1rio, data ou NFe...", None))
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.tb_base.setTabText(self.tb_base.indexOf(self.Tab2), QCoreApplication.translate("MainWindow", u"Geral", None))
    # retranslateUi

