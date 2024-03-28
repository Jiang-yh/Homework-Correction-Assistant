import os
from shutil import copyfile

from PyQt5 import QtCore, QtGui, QtWidgets
from question_segment_match import convertimg2problemanswer, lcs
from ase.ase_inference import Score_essay
from paddleocr import draw_ocr

class LoginButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(60, 60)

        self.color1 = QtGui.QColor(240, 53, 218)
        self.color2 = QtGui.QColor(61, 217, 245)

        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0.00001,
            endValue=0.9999,
            duration=250
        )

    def _animate(self, value):
        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: rgb(255, 255, 255);
            border-style: solid;
            border-radius:21px;
        """
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        qss += grad
        self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

class ChangequestionButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(60, 60)

        # self.color1 = QtGui.QColor(240, 53, 218)
        # self.color2 = QtGui.QColor(61, 217, 245)
        self.color1 = QtGui.QColor(176, 23, 31)
        self.color2 = QtGui.QColor(255, 99, 71)

        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0.00001,
            endValue=0.9999,
            duration=250
        )

    def _animate(self, value):
        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: rgb(255, 255, 255);
            border-style: solid;
            border-radius:21px;
        """
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        qss += grad
        self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

class ChangeaccountButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(60, 60)

        # self.color1 = QtGui.QColor(240, 53, 218)
        # self.color2 = QtGui.QColor(61, 217, 245)
        self.color1 = QtGui.QColor(218, 112, 214)
        self.color2 = QtGui.QColor(3, 168, 158)

        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0.00001,
            endValue=0.9999,
            duration=250
        )

    def _animate(self, value):
        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: rgb(255, 255, 255);
            border-style: solid;
            border-radius:21px;
        """
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        qss += grad
        self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

class TeacherHomepageButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(60, 60)

        # self.color1 = QtGui.QColor(240, 53, 218)
        # self.color2 = QtGui.QColor(61, 217, 245)
        self.color1 = QtGui.QColor(51, 161, 201)
        self.color2 = QtGui.QColor(0, 199, 140)

        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0.00001,
            endValue=0.9999,
            duration=250
        )

    def _animate(self, value):
        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: rgb(255, 255, 255);
            border-style: solid;
            border-radius:21px;
        """
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        qss += grad
        self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

class TeacherHomeworkButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(60, 60)

        # self.color1 = QtGui.QColor(240, 53, 218)
        # self.color2 = QtGui.QColor(61, 217, 245)
        self.color1 = QtGui.QColor(64, 224, 208)
        self.color2 = QtGui.QColor(112, 128, 105)

        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0.00001,
            endValue=0.9999,
            duration=250
        )

    def _animate(self, value):
        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: rgb(255, 255, 255);
            border-style: solid;
            border-radius:21px;
        """
        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
            color1=self.color1.name(), color2=self.color2.name(), value=value
        )
        qss += grad
        self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

class AdminTableButton(QtWidgets.QPushButton):
    def __init__(self, parent, text='点击修改该题'):
        super().__init__(parent)
        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: blue;
            border-style: solid;
            border-radius:21px;
        """
        self.setStyleSheet(qss)
        self.setText(text)

class UploadButton(QtWidgets.QPushButton):
    def __init__(self, parent, submited, load_model_obj):
        super().__init__(parent)
        self.load_model_obj, self.parent = load_model_obj, parent
        # self.questions, self.answers = questions, answers
        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: blue;
            border-style: solid;
            border-radius:21px;
        """
        self.setStyleSheet(qss)
        if not submited:
            self.setText('点击提交作业')
        else:
            self.setText('已提交')
        self.clicked.connect(self.showDialog)

    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '.')
        if fname[0] and os.path.splitext(fname[0])[-1] in ['.jpg', '.png', '.jpeg', '.bmp']:
            for t in self.load_model_obj.load_threads:
                if not t.isFinished():
                    QtWidgets.QMessageBox.information(self, '提交失败', '系统尚未加载完成，请稍等后提交', QtWidgets.QMessageBox.Yes)
                    return

            sender = self.sender()
            for i in range(len(self.parent.uploadbuttons)):
                if sender == self.parent.uploadbuttons[i]:
                    self.question_ids = self.parent.homepage_lst[i][4]
                    self.homework_id = self.parent.homepage_lst[i][0]
                    self.lst_dex = i
                    break
            query_res, self.questions = [], []
            for qid in self.question_ids:
                # question, answer, question_type, point, student_answer
                question, answer, question_type, point, _ = self.parent.db.inquire_homework(
                    self.parent.db.account2userid(self.parent.account.id), self.parent.homepage_lst[i][0], qid)
                query_res.append([question, answer, question_type, point])
                self.questions.append(question)
            # self.ocr, self.sp, self.dbnet, self.ase = None, None, None, None
            d_res = self.load_model_obj.ocr.ocr(fname[0], cls=True, db_model=self.load_model_obj.dbnet)
            result = []
            for line in d_res:
                # print(' '.join([sp_model.correct(w) for w in line[1][0].split(' ')]), line[1][1])
                line[1] = (' '.join([self.load_model_obj.sp.correct(w) for w in line[1][0].split(' ')]), line[1][1])
                result.append(line)

            # from PIL import Image
            # image = Image.open(fname[0]).convert('RGB')
            # boxes = [line[0] for line in result]
            # txts = [line[1][0] for line in result]
            # scores = [line[1][1] for line in result]
            # im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf', drop_score=0.0)
            # im_show = Image.fromarray(im_show)
            # im_show.save('test.jpg')

            detected_question_answer = convertimg2problemanswer(result, self.questions)
            print(detected_question_answer)
            all_matched_ids = sorted([dqa[1] for dqa in detected_question_answer])
            if all_matched_ids != sorted(list(set(all_matched_ids))):
                QtWidgets.QMessageBox.information(self, '提交失败', '部分题目缺失，请重新上传', QtWidgets.QMessageBox.Yes)
                return
            detected_question_answer = sorted(detected_question_answer, key=lambda x: x[1])
            for i in range(len(detected_question_answer)):
                if query_res[i][2]:
                    score = 2*lcs(query_res[i][1], detected_question_answer[i][0])/(len(query_res[i][1])+len(detected_question_answer[i][0]))
                    score = score > 0.6
                else:
                    score = Score_essay(self.load_model_obj.ase[0], self.load_model_obj.ase[1], self.load_model_obj.ase[2], detected_question_answer[i][0])['score']/100
                    same_ques = self.parent.db.inquire_student_answer(self.homework_id, self.question_ids[i])
                    for idx, ans in same_ques:
                        if idx == self.parent.db.account2userid(self.parent.account.id):
                            continue
                        if lcs(ans, detected_question_answer[i][0]) > 0.7:
                            score = -1
                            # save_score(self, homework_id, user_id, question_id, score, question_type, student_answer):
                            self.parent.db.save_score(self.homework_id, idx, self.question_ids[i], -1, 0, ans)
                score = round(score*query_res[i][3]) if score > 0 else score
                detected_question_answer[i][0] = detected_question_answer[i][0].replace("'", '')
                # print(self.homework_id, self.parent.db.account2userid(self.parent.account.id), self.question_ids[i], score, query_res[i][2], detected_question_answer[i][0])
                self.parent.db.save_score(self.homework_id, self.parent.db.account2userid(self.parent.account.id), self.question_ids[i], score, query_res[i][2], detected_question_answer[i][0])
            QtWidgets.QMessageBox.information(self, '提交成功', '作业 {:s} 提交成功'.format(self.parent.homepage_lst[self.lst_dex][1]), QtWidgets.QMessageBox.Yes)
                # scores.append(round(score * query_res[i][3]))
            # print('upload homework {:s}'.format(fname[0]))

        else:
            QtWidgets.QMessageBox.information(self, '提交失败', '无效文件，请提交图片', QtWidgets.QMessageBox.Yes)

    # def alert_repeat_submit(self):
    #     QtWidgets.QMessageBox.information(self, '提交失败', '请勿重复提交', QtWidgets.QMessageBox.Yes)

class DownloadButton(QtWidgets.QPushButton):
    def __init__(self, parent, savepath):
        super().__init__(parent)
        self.savepath = savepath
        self.clicked.connect(self.download_file)

        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: blue;
            border-style: solid;
            border-radius:21px;
        """
        self.setStyleSheet(qss)
        self.setText('点击下载文档')

    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '.')
        if fname[0]:
            self.filepath = fname[0]
            self.savename = os.path.join(self.savepath, str(len(os.listdir(self.savepath))+1) + os.path.splitext(fname[0])[-1])
            # print(self.filepath, self.savename, os.getcwd())
            copyfile(self.savepath, self.savename)
