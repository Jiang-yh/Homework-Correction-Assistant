import os
from shutil import copyfile

from PyQt5 import QtCore, QtGui, QtWidgets

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

class UploadButton(QtWidgets.QPushButton):
    def __init__(self, parent, savepath):
        super().__init__(parent)
        self.filepath = None
        self.savepath = savepath
        if not os.path.exists(self.savepath):
            os.makedirs(self.savepath)

        self.clicked.connect(self.showDialog)

        qss = """
            font: 75 10pt "Microsoft YaHei UI";
            font-weight: bold;
            color: blue;
            border-style: solid;
            border-radius:21px;
        """
        self.setStyleSheet(qss)
        self.setText('点击提交作业')

    def showDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '.')
        if fname[0]:
            self.filepath = fname[0]
            self.savename = os.path.join(self.savepath, str(len(os.listdir(self.savepath))+1) + os.path.splitext(fname[0])[-1])
            # print(self.filepath, self.savename, os.getcwd())
            copyfile(self.filepath, self.savename)

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