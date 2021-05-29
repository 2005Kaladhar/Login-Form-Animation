# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_designGjuiwS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(336, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BaseFrame = QFrame(self.centralwidget)
        self.BaseFrame.setObjectName(u"BaseFrame")
        self.BaseFrame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(2, 18, 42);\n"
"border-radius:15px;\n"
"\n"
"\n"
"}")
        self.BaseFrame.setFrameShape(QFrame.StyledPanel)
        self.BaseFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.BaseFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.TitleBar_2 = QFrame(self.BaseFrame)
        self.TitleBar_2.setObjectName(u"TitleBar_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleBar_2.sizePolicy().hasHeightForWidth())
        self.TitleBar_2.setSizePolicy(sizePolicy)
        self.TitleBar_2.setMinimumSize(QSize(0, 0))
        self.TitleBar_2.setMaximumSize(QSize(16777215, 30))
        self.TitleBar_2.setStyleSheet(u"QFrame{\n"
"\n"
"	border-image:none;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.488, y2:0.556818, stop:0 rgba(0, 0, 0, 255), stop:0.363636 rgba(132, 132, 132, 123), stop:0.619318 rgba(165, 165, 165, 90), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius:12px;\n"
"\n"
"\n"
"}")
        self.TitleBar_2.setFrameShape(QFrame.StyledPanel)
        self.TitleBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.TitleBar_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.TitleBar_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setCursor(QCursor(Qt.SizeAllCursor))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.TitleBar_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 25))
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setStyleSheet(u"border-image:none;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.Minimizebtn = QPushButton(self.frame_3)
        self.Minimizebtn.setObjectName(u"Minimizebtn")
        sizePolicy1.setHeightForWidth(self.Minimizebtn.sizePolicy().hasHeightForWidth())
        self.Minimizebtn.setSizePolicy(sizePolicy1)
        self.Minimizebtn.setMaximumSize(QSize(15, 15))
        self.Minimizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Minimizebtn)

        self.Maximizebtn = QPushButton(self.frame_3)
        self.Maximizebtn.setObjectName(u"Maximizebtn")
        sizePolicy1.setHeightForWidth(self.Maximizebtn.sizePolicy().hasHeightForWidth())
        self.Maximizebtn.setSizePolicy(sizePolicy1)
        self.Maximizebtn.setMaximumSize(QSize(15, 15))
        self.Maximizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(85, 170, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Maximizebtn)

        self.CloseButton = QPushButton(self.frame_3)
        self.CloseButton.setObjectName(u"CloseButton")
        sizePolicy1.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy1)
        self.CloseButton.setMaximumSize(QSize(15, 15))
        self.CloseButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 0, 16);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.CloseButton)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.TitleBar_2, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.BaseFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"background-color: rgb(51, 63, 79);\n"
"\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.Page1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalLayout_4 = QHBoxLayout(self.Page1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.StackedContent = QFrame(self.Page1)
        self.StackedContent.setObjectName(u"StackedContent")
        self.StackedContent.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0))\n"
";\n"
"	background-color: rgb(2, 18, 42);\n"
"\n"
"}")
        self.StackedContent.setFrameShape(QFrame.StyledPanel)
        self.StackedContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.StackedContent)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_8 = QFrame(self.StackedContent)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainContentFrame = QFrame(self.frame_8)
        self.mainContentFrame.setObjectName(u"mainContentFrame")
        sizePolicy1.setHeightForWidth(self.mainContentFrame.sizePolicy().hasHeightForWidth())
        self.mainContentFrame.setSizePolicy(sizePolicy1)
        self.mainContentFrame.setMinimumSize(QSize(291, 451))
        self.mainContentFrame.setFrameShape(QFrame.StyledPanel)
        self.mainContentFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.mainContentFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, -1, -1, -1)
        self.frame_4 = QFrame(self.mainContentFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 200))
        self.frame_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LogoFrame = QFrame(self.frame_4)
        self.LogoFrame.setObjectName(u"LogoFrame")
        sizePolicy1.setHeightForWidth(self.LogoFrame.sizePolicy().hasHeightForWidth())
        self.LogoFrame.setSizePolicy(sizePolicy1)
        self.LogoFrame.setMinimumSize(QSize(250, 250))
        self.LogoFrame.setStyleSheet(u"\n"
"border-image: url(:/newPrefix/TreeLogo.png);")
        self.LogoFrame.setFrameShape(QFrame.StyledPanel)
        self.LogoFrame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.LogoFrame)


        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 2)

        self.frame_6 = QFrame(self.mainContentFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Box_name = QLineEdit(self.frame_6)
        self.Box_name.setObjectName(u"Box_name")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Box_name.setFont(font)
        self.Box_name.setTabletTracking(True)
        self.Box_name.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.591045, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0), stop:1 rgba(59, 241, 0, 90));\n"
"border-radius:11px;\n"
"margin-top:20px;\n"
"\n"
"text-align:left;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.574, y1:0.301136, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0), stop:1 rgba(27, 109, 0, 135));\n"
"\n"
"	color: rgb(241, 241, 241);\n"
"\n"
"}\n"
"")
        self.Box_name.setAlignment(Qt.AlignCenter)
        self.Box_name.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.Box_name, 0, 0, 1, 2)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_3.addWidget(self.frame, 2, 1, 1, 1)

        self.Box_password = QLineEdit(self.frame_6)
        self.Box_password.setObjectName(u"Box_password")
        sizePolicy.setHeightForWidth(self.Box_password.sizePolicy().hasHeightForWidth())
        self.Box_password.setSizePolicy(sizePolicy)
        self.Box_password.setMinimumSize(QSize(205, 0))
        self.Box_password.setFont(font)
        self.Box_password.setTabletTracking(True)
        self.Box_password.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.591045, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0), stop:1 rgba(59, 241, 0, 90));\n"
"border-radius:11px;\n"
"margin-top:20px;\n"
"text-align:left;\n"
"\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.574, y1:0.301136, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0), stop:1 rgba(27, 109, 0, 135));\n"
"color: rgb(241, 241, 241);\n"
"}\n"
"")
        self.Box_password.setEchoMode(QLineEdit.Password)
        self.Box_password.setAlignment(Qt.AlignCenter)
        self.Box_password.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.Box_password, 2, 0, 1, 1)

        self.Box_email = QLineEdit(self.frame_6)
        self.Box_email.setObjectName(u"Box_email")
        self.Box_email.setFont(font)
        self.Box_email.setTabletTracking(True)
        self.Box_email.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.591045, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0), stop:1 rgba(59, 241, 0, 90));\n"
"border-radius:11px;\n"
"margin-top:20px;\n"
"\n"
"text-align:left;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0.574, y1:0.301136, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0), stop:1 rgba(27, 109, 0, 135));\n"
"\n"
"	color: rgb(241, 241, 241);\n"
"\n"
"}\n"
"")
        self.Box_email.setAlignment(Qt.AlignCenter)
        self.Box_email.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.Box_email, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout_3)


        self.gridLayout_2.addWidget(self.frame_6, 1, 0, 1, 2)


        self.horizontalLayout_7.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.mainContentFrame)

        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(296, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.LoginButton = QPushButton(self.frame_7)
        self.LoginButton.setObjectName(u"LoginButton")
        sizePolicy1.setHeightForWidth(self.LoginButton.sizePolicy().hasHeightForWidth())
        self.LoginButton.setSizePolicy(sizePolicy1)
        self.LoginButton.setMinimumSize(QSize(97, 40))
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(14)
        self.LoginButton.setFont(font1)
        self.LoginButton.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"	background-color: rgb(99, 192, 81);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(99, 192, 81,200);\n"
"\n"
"\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.LoginButton)


        self.verticalLayout.addWidget(self.frame_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout)


        self.horizontalLayout_12.addWidget(self.frame_8)


        self.horizontalLayout_4.addWidget(self.StackedContent)

        self.stackedWidget.addWidget(self.Page1)
        self.SucessLoginPage = QWidget()
        self.SucessLoginPage.setObjectName(u"SucessLoginPage")
        self.SucessLoginPage.setStyleSheet(u"border-radius:10px;")
        self.horizontalLayout_13 = QHBoxLayout(self.SucessLoginPage)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(30)
        self.gridLayout_4.setContentsMargins(20, -1, 1, -1)
        self.frame_5 = QFrame(self.SucessLoginPage)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(228, 225))
        self.frame_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"border-image: url(:/newPrefix/happyTree.png);\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_5, 0, 0, 1, 1)

        self.label = QLabel(self.SucessLoginPage)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 143))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")

        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)

        self.frame_9 = QFrame(self.SucessLoginPage)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, 22, 23)
        self.pushButton = QPushButton(self.frame_9)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(50, 50))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-image: url(:/newPrefix/proceedicon.png);\n"
"\n"
"border-radius:25px;\n"
"}\n"
"\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 0, 200);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_14.addWidget(self.pushButton)


        self.gridLayout_4.addWidget(self.frame_9, 3, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_4)

        self.stackedWidget.addWidget(self.SucessLoginPage)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.BaseFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Box_name, self.Box_email)
        QWidget.setTabOrder(self.Box_email, self.Box_password)
        QWidget.setTabOrder(self.Box_password, self.LoginButton)
        QWidget.setTabOrder(self.LoginButton, self.CloseButton)
        QWidget.setTabOrder(self.CloseButton, self.Maximizebtn)
        QWidget.setTabOrder(self.Maximizebtn, self.Minimizebtn)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.Minimizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Minimizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.Maximizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Maximizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.CloseButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CloseButton.setText("")
        self.Box_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Name", None))
        self.Box_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Box_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
#if QT_CONFIG(shortcut)
        self.LoginButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Successful Login</span><span style=\" font-weight:600;\"/><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:18pt; color:#308b20;\">\u2713</span></p><p align=\"center\"><span style=\" font-weight:600;\">&quot;</span><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">They recklessly cut me,</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">but you care about me</span><span style=\" font-weight:600;\">&quot;</span></p><p align=\"center\"><span style=\" font-weight:600; color:#ff00ff;\">THank You!</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton.setText("")
    # retranslateUi

