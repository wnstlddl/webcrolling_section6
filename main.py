import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import  pyqtSlot, pyqtSignal
from lib.YouViewerLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
import re
import datetime

# form_class = uic.loadUiType("C:/python_Webcroling/section6/ui/you_viewer_v1.0.ui")[0]
#cmd 창에 해당 루트 가서 이렇게 입력 pyuic5 -x you_viewer_v1.0.ui -o you_viewer_layout.py

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAuthLock()
        self.initSignal()

        #Logine valua
        self.user_id = None
        self.user_pw = None


    # 기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamComboBox.setEnabled(False)
        self.startButtom.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')

    # 기본 UI 비활성화
    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamComboBox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증완료')

    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)

    def initSignal(self):
        self.logineButton.clicked.connect(self.authCheck)

    @pyqtSlot()
    def authCheck(self):
        dig = AuthDialog()
        dig.exec_()
        self.user_id = dig.user_id
        self.user_pw = dig.user_pw
        if True:
            self.initAuthActive()
            self.logineButton.setText("인증완료")
            self.logineButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)
        else:
            QMessageBox.about(self,"인증오류","ID 또는 PW 오류")

if __name__=="__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
