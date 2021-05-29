# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_designCQFMPN.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(328, 546)
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
"border-radius:10px;\n"
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
        self.stackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.horizontalLayout_4 = QHBoxLayout(self.Page1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.StackedContent = QFrame(self.Page1)
        self.StackedContent.setObjectName(u"StackedContent")
        self.StackedContent.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}")
        self.StackedContent.setFrameShape(QFrame.StyledPanel)
        self.StackedContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.StackedContent)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.mainContentFrame = QFrame(self.StackedContent)
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
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(250, 250))
        self.frame_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"border-image: url(:/newPrefix/TreeLogo.png);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_5)


        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 2)

        self.frame_6 = QFrame(self.mainContentFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setTabletTracking(True)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	color: rgb(241, 241, 241);\n"
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
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 0, 1, 2)

        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QSize(205, 0))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setTabletTracking(True)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	color: rgb(241, 241, 241);\n"
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
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.setTabletTracking(True)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	color: rgb(241, 241, 241);\n"
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
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 2)

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


        self.horizontalLayout_9.addLayout(self.gridLayout_3)


        self.gridLayout_2.addWidget(self.frame_6, 1, 0, 1, 2)


        self.horizontalLayout_7.addLayout(self.gridLayout_2)


        self.horizontalLayout_10.addWidget(self.mainContentFrame)


        self.horizontalLayout_4.addWidget(self.StackedContent)

        self.stackedWidget.addWidget(self.Page1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.BaseFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

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
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Name", None))
    # retranslateUi

