from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_ui_design import Ui_MainWindow


import sys, threading

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.reverse_opacity = 1
        self.opacity = 0
        self.logoFrameopacity = 0

        self.screenGeo = QApplication.desktop().screenGeometry()
        self.default_geometry = self.geometry()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Page1)

        self.ui.CloseButton.clicked.connect(self.closer)
        self.ui.Minimizebtn.clicked.connect(self.mini_button)
        self.ui.Maximizebtn.clicked.connect(self.maxi_button)
        self.ui.LoginButton.clicked.connect(self.loginer)

        def moveWindow(e):
            FRAME = QApplication.desktop().screenGeometry()
            if not (FRAME == self.geometry()):
                if e.buttons() == Qt.LeftButton:
                    if not (self.geometry() == self.screenGeo):
                        self.move(self.pos() + e.globalPos() - self.clickPosition)
                        self.clickPosition = e.globalPos()
                        e.accept()
                    else:
                        self.setGeometry(self.default_geometry)

        self.ui.TitleBar_2.mouseMoveEvent = moveWindow

        self.show()


        self.windowAnimation()




    def windowOpacityAnimation(self):
        self.setWindowOpacity(0)
        self.ui.stackedWidget.setCurrentWidget(self.ui.SucessLoginPage)
        while self.opacity!=1:
            QApplication.processEvents()
            loop = QEventLoop()
            QTimer.singleShot(100,loop.quit)
            loop.exec_()
            self.setWindowOpacity(self.opacity)
            self.opacity +=0.05

    def reverse_windowOpacityAnimation(self):
        self.setWindowOpacity(1)
        while self.reverse_opacity!=0:
            QApplication.processEvents()
            # loop = QEventLoop()
            # QTimer.singleShot(1,loop.quit)
            # loop.exec_()
            self.setWindowOpacity(self.opacity)
            self.opacity -=0.3

    def windowAnimation(self,change_page=False,pageNameobj=None,animationType=QEasingCurve.InOutQuad):

        if change_page:
            self.ui.stackedWidget.setCurrentWidget(self.ui.SucessLoginPage)

        self.anim = QPropertyAnimation(self.ui.BaseFrame, b"geometry")
        self.anim.setDuration(500)

        self.anim.setEasingCurve(animationType)
        self.anim.setStartValue(QRect(12, 12, 200, 100))
        # self.anim.setStartValue(QRect(0,0,300,500))
        self.anim.setEndValue(QRect(0,0,336,586))
        self.anim.start()



    def loginer(self):
        name = self.ui.Box_name.text()
        email = self.ui.Box_email.text()
        password = self.ui.Box_password.text()

        realpass = 'KaladharGopal'
        email_check = False

        if name.lstrip().rstrip() == '':
            name_check = False
            self.error(self.ui.Box_name)


        elif email[-10:] == '@gmail.com' and (len(email.split(' ')) == 1) :
            email_check = True

        else:
            self.error(self.ui.Box_email)
            email_check = False

        if  email_check and not password == '':
            self.error(self.ui.Box_password)
        elif password == realpass:
            self.ui.LoginButton.setText("Login✓")
            # self.windowOpacityAnimation()

            self.windowAnimation(change_page=True,pageNameobj=self.ui.SucessLoginPage)

            # self.ui.stackedWidget.setCurrentWidget(self.ui.SucessLoginPage)
            # loop = QEventLoop()
            # QTimer.singleShot(1000,loop.quit)
            # loop.exec_()
            # self.windowOpacityAnimation()





    def error(self,obj):
        self.ui.LoginButton.hide()
        placeholder = obj.text()
        self.anim = QPropertyAnimation(self.ui.BaseFrame, b"geometry")
        self.anim.setDuration(500)

        obj.setText('❌')
        obj.setEchoMode(QLineEdit.Normal)

        self.anim.setEasingCurve(QEasingCurve.InOutBounce)
        # self.anim.setStartValue(QRect(12, 12, 330, 580))
        self.anim.setStartValue(QRect(0,0,300,500))
        self.anim.setEndValue(QRect(0,0,336,586))
        self.anim.start()

        obj.setStyleSheet('''

         QLineEdit{
        color: rgb(255, 255, 255);
        background-color: qlineargradient(spread:pad, x1:0.591045,
         y1:0, x2:0.5, y2:1, stop:0 rgba(0, 93, 73, 0), stop:1 rgba(241, 0, 0, 108));
        border-radius:11px;
        margin-top:20px;
        text-align:left;}''')

        loop = QEventLoop()
        QTimer.singleShot(500,loop.quit)
        loop.exec_()

        obj.setStyleSheet('''

        QLineEdit{
        color: rgb(255, 255, 255);
        background-color: qlineargradient(spread:pad, x1:0.591045, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0), stop:1 rgba(59, 241, 0, 90));
        border-radius:11px;
        margin-top:20px;
        text-align:left;}
        QLineEdit::hover{
            background-color: qlineargradient(spread:pad, x1:0.574, y1:0.301136, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0),
        stop:1 rgba(27, 109, 0, 135));
        color: rgb(241, 241, 241); } ''')

        obj.setText(placeholder)

        self.ui.LoginButton.show()
        if obj == self.ui.Box_password:
            obj.setEchoMode(QLineEdit.Password)
            obj.clear()




    def mousePressEvent(self, event) -> None:
        self.clickPosition = event.globalPos()

    def closer(self):
        self.close()
        quit()

    def mini_button(self):
        if self.isMinimized():
            self.setGeometry(self.default_geometry)
        else:
            self.showMinimized()

    def maxi_button(self):
        fullscreen = self.screenGeo == self.geometry()
        print("is it in full screen ?:",fullscreen)
        print("screen geometry is ",self.screenGeo)
        if fullscreen:
            self.setGeometry(self.default_geometry)
        elif not fullscreen:
            self.setGeometry(self.screenGeo)



if __name__ == '__main__':
    app = QApplication()
    window = MainApp()
    sys.exit(app.exec_())
