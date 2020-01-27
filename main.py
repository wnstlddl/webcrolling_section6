import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import  pyqtSlot, pyqtSignal, QUrl
from lib.YouViewerLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
import re
import datetime
import pytube

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

        #재생여부
        self.is_play = False

        #유튜브 관련 작업
        self.youtb = None
        self.yoytbFileSize = 0

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


        #시그널 초기화
    def initSignal(self):
        self.logineButton.clicked.connect(self.authCheck)
        self.previewButton.clicked.connect(self.load_url)
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.webEngineView.loadProgress.connect(self.showProgressBrowserLoading)
        self.fileNavButton.clicked.connect(self.selectDownPath)
        self.calendarWidget.clicked.connect(self.append_data)
        self.startButtom.clicked.connect(self.downloadYoutb)


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
            self.append_log_msg("Log in Success")
        else:
            QMessageBox.about(self,"인증오류","ID 또는 PW 오류")


    def load_url(self):
        url = self.urlTextEdit.text().strip() # strip 는 공백 없애기
        v = re.compile('^https://www.youtube.com/?')
        if self.is_play:
            self.append_log_msg('Stop Click')
            self.webEngineView.load(QUrl('about:blank'))
            self.previewButton.setText("재생")
            self.is_play = True
            self.urlTextEdit.clear()
            self.urlTextEdit.setFocus(True)
            self.startButtom.setEnabled(False)
            self.streamComboBox.clear()
            self.progressBar_2.setValue(0)
            self.showStatusMsg("인증완료")

        else:
            if v.match(url) is not None:
                self.append_log_msg('Play Click')
                self.webEngineView.load(QUrl(url))
                self.showStatusMsg(url + "  재생 중")
                self.previewButton.setText("중지")
                self.is_play = True
                self.startButtom.setEnabled(True)
                self.initialYouWork(url)

            else:
                QMessageBox.about(self,"URL 형식오류","Youtube 주소 형식이 아닙니다.")
                self.urlTextEdit.clear()
                self.urlTextEdit.setFocus(True)


    def initialYouWork(self,url):
        video_list = pytube.YouTube(url)
        #로딩바 계산
        video_list.register_on_progress_callback(self.showProgressDownLoading)
        self.youtb = video_list.streams.all()
        self.streamComboBox.clear()
        for q in self.youtb:
            tmp_list, str_list = [], []
            tmp_list.append(str(q.mime_type or ''))
            tmp_list.append(str(q.res or ''))
            tmp_list.append(str(q.fps or ''))
            tmp_list.append(str(q.abr or ''))

            str_list = [x for x in tmp_list if x !='']
            self.streamComboBox.addItem(','.join(str_list))

    def append_log_msg(self,act):
        now = datetime.datetime.now()
        nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")
        app_msg = self.user_id + " : " + act + " -  (" + nowDatetime + ")"
        print(app_msg)
        self.plainTextEdit.appendPlainText(app_msg)

        #로그 저장
        #mac
        # with open("C:/python/webcrolling/section6/webcrolling_section6/log/log.txt",'a') as f:
        #     f.write(app_msg + '\n')
        #Desktop
        with open("C:/python_Webcroling/section6/log/log.txt",'a') as f:
            f.write(app_msg + '\n')

    @pyqtSlot(int)
    def showProgressBrowserLoading(self, v):
        self.progressBar.setValue(v)

    @pyqtSlot()
    def selectDownPath(self):
        #파일선택
        # fname = QFileDialog.getOpenFileName(self)
        # self.pathTextEdit.setText(fname[0])

        #경로선택
        fpath = QFileDialog.getExistingDirectory(self,'Select Directory')
        self.pathTextEdit.setText(fpath)

    @pyqtSlot()
    def append_data(self):
        cur_date = self.calendarWidget.selectedDate()
        log_append_day_msg = str(cur_date.year())+'-'+str(cur_date.month())+'-'+str(cur_date.day())
        self.append_log_msg('Calender Click ')
        self.append_log_msg(log_append_day_msg)

    @pyqtSlot()
    def downloadYoutb(self):
        down_dir = self.pathTextEdit.text().strip()
        if down_dir is None or down_dir =="" or not down_dir:
            QMessageBox.about(self,'경로 선택','다운로드 받을 경로를 선택 하세요')
            return None

        self.yoytbFileSize = self.youtb[self.streamComboBox.currentIndex()].filesize
        # print(self.yoytbFileSize)
        self.youtb[self.streamComboBox.currentIndex()].download(down_dir)
        self.append_log_msg('Download Click')

    def showProgressDownLoading(self,stream,chunk,file_handle,bytes_remaining):
        self.progressBar_2.setValue(int(((self.yoytbFileSize-bytes_remaining)/self.yoytbFileSize)*100))

if __name__=="__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
