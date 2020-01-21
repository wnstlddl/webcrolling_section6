import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
# print(sys.argv) #이 파일이 진행되고 있는 경로를 가져온다
label = QLabel("PyQT First Test")
label.show()

print("Before Loop")
app.exec_()
print("After Loop")
