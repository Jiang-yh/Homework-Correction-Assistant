import time
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from gui_utils import UploadButton

from paddleocr import PaddleOCR
from ekphrasis.classes.spellcorrect import SpellCorrector
from DBNet.dbnet.dbnet_infer import DBNET
from ase.ase_inference import Build_ase_model


class Student_homepage_load_item:
    def __init__(self, parent, name, create_date, deadline, submitbutton_text):
        self.sbmtbtn = UploadButton()
        pass

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

class Thread_Student_homepage_load(QtCore.QThread):
    def __init__(self, db, id, parent):
        super().__init__()
        self.db, self.id, self.parent = db, id, parent

    def run(self):
        # self.show_res = []
        query_res = self.db.student_inquire_homework(self.id)
        print(query_res)
        self.parent.query_res = query_res
        current_time = datetime.datetime.now()
        quit()

        for i in range(len(query_res)):
            if (current_time - query_res[i][3]).total_seconds() < 0:
                # self.show_res.append()
                rowPosition = self.parent.tableWidget.rowCount()
                self.parent.tableWidget.insertRow(rowPosition)
                self.parent.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(query_res[i][1]))
                self.parent.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(query_res[i][2].strftime('%Y-%m-%d %H:%M:%S')))
                self.parent.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(query_res[i][3].strftime('%Y-%m-%d %H:%M:%S')))
                self.parent.tableWidget.setCellWidget(rowPosition, 4, UploadButton(self.parent.tableWidget, query_res[i][4]))


class Thread_Admin_page_show_number(QtCore.QThread):
    def __init__(self, db, textbar):
        super().__init__()
        self.db, self.textbar = db, textbar

    def run(self):
        query_res = self.db.admin_homepage()
        showtext = "截止目前系统已注册账号有{:4d}个，其中有{:4d}个学生账号，{:4d}个教师账号，{:4d}个管理员账号。\n\n截止目前系统已上传题目{:4d}道，其中主观题{:4d}道，客观题{:4d}道。".format(
            query_res[0], query_res[1]['学生'], query_res[1]['教师'], query_res[1]['管理员'], query_res[2], query_res[3]['主观题'], query_res[3]['客观题']
        )
        self.textbar.setText(showtext)

class Thread_load_ocr(QtCore.QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
    def run(self):
        self.parent.ocr = PaddleOCR(use_angle_cls=True, lang="ch",
                        cls_model_dir='D:\code\homework_viewer\mycode\PaddleOCR\weights\ch_ppocr_mobile_v2.0_cls_train',
                        det_model_dir=r'D:\code\homework_viewer\mycode\PaddleOCR\weights\det\ch_ppocr_server_v2.0_det_train',
                        rec_model_dir=r'D:\code\homework_viewer\mycode\PaddleOCR\weights\rec\en_number_mobile_v2.0_rec_slim_train')
class Thread_load_sp(QtCore.QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
    def run(self):
        self.parent.sp = SpellCorrector(corpus="coca", corpus_path='D:\code\homework_viewer\mycode\coca')
class Thread_load_dbnet(QtCore.QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
    def run(self):
        self.parent.dbnet = DBNET(MODEL_PATH="D:\code\homework_viewer\mycode\DBNet\models\dbnet.onnx")
class Thread_load_ase(QtCore.QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
    def run(self):
        self.parent.ase = Build_ase_model(r"D:\code\homework_viewer\mycode\ase\saved_model\saved_weight")


class Load_models(QtCore.QObject):
    def __init__(self):
        super(Load_models, self).__init__()
        self.ocr, self.sp, self.dbnet, self.ase = None, None, None, None
        self.load_threads = [Thread_load_sp(self), Thread_load_ocr(self), Thread_load_dbnet(self), Thread_load_ase(self)]
        for t in self.load_threads:
            t.start()

