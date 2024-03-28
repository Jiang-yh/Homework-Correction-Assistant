import time

from PyQt5 import QtCore
from questionset import Ui_Form

class Thread_Showtime(QtCore.QThread):
    def __init__(self, textbar, refer):
        super().__init__()
        self.textbar = textbar
        self.refer = refer

    def run(self):
        while True:
            # print(time.localtime())
            format_time = time.strftime('%Y{y}%m{m}%d{d} %H:%M:%S').format(y='年', m='月', d='日')
            # format_time = time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime())
            self.textbar.setText("欢迎您，{:s}，现在是 {:s}".format(self.refer, format_time))
            time.sleep(1)

class Thread_Changequestion(QtCore.QThread):
    def __init__(self, question_id):
        pass

    def run(self):
        pass