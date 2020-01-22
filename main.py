import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from lib.YouViewerLayout import Ui_MainWindow
import re
import datetime

# form_class = uic.loadUiType("C:/python_Webcroling/section6/ui/you_viewer_v1.0.ui")[0]
#cmd 창에 해당 루트 가서 이렇게 입력 pyuic5 -x you_viewer_v1.0.ui -o you_viewer_layout.py

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__=="__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
