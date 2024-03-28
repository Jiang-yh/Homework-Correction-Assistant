import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from gui_utils import TeacherHomeworkButton

class Problem_widget(QtWidgets.QWidget):

    def __init__(self, parent, dex, widgetbar):

        super(Problem_widget,self).__init__()
        self.dex = dex
        self.widgetbar = widgetbar
        self.parent = parent
        self.setupUi(self)
        self.retranslateUi(self)
        self.label.setText("题目:{:3d}".format(dex+1))
        self.textBrowser.setText('Loading....')
        self.textBrowser_2.setText('Loading....')
        self.textBrowser.textChanged.connect(self.adjust_bbox_width)
        self.textBrowser_2.textChanged.connect(self.adjust_bbox_width)

    def adjust_bbox_width(self):
        height = self.textBrowser.document().size().height() + self.textBrowser.contentsMargins().top() + self.textBrowser.contentsMargins().bottom()
        self.textBrowser.setFixedHeight(height)

        height2 =self.textBrowser_2.document().size().height() + self.textBrowser_2.contentsMargins().top() + self.textBrowser_2.contentsMargins().bottom()
        self.textBrowser_2.setFixedHeight(height2)

        # widget origin: 40, 160, 381, 131
        # text_browse origin: 50, 60, 351, 91

        self.widget.adjustSize()
        self.widget.setGeometry(QtCore.QRect(40, 60 + self.textBrowser.size().height(), self.widget.size().width(), self.widget.size().height()))
        # self.widgetbar.adjustSize()
        self.adjustSize()
        self.widgetbar.setSizeHint(self.size())

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(467, 299)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 9, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 9, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(50, 60, 351, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 160, 381, 131))
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 50, 351, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "题目"))
        self.label_2.setText(_translate("Form", "得分:{:3d}/{:3d}".format(0, 0)))
        self.label_3.setText(_translate("Form", "作答："))


class Stu_Ui_Form(QtWidgets.QWidget):
    def __init__(self, parent, questions):
        super(Stu_Ui_Form,self).__init__()
        self.parent = parent
        self.questions = questions
        self.total_score = 0

        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 534)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(90, 50, 471, 401))
        self.listWidget.setObjectName("listWidget")

        # self.label_2 = QtWidgets.QLabel(Form)
        # self.label_2.setGeometry(QtCore.QRect(200, 9, 181, 31))
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI Black")
        # font.setPointSize(15)
        # self.label_2.setFont(font)
        # self.label_2.setObjectName("label_2")
        self.label =QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 480, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 =QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 480, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label")

        self.question_widgets, self.question_frames = [], []
        for i in range(len(self.questions)):
            self.question_frames.append(QtWidgets.QListWidgetItem())
            self.question_widgets.append(Problem_widget(self, i, self.question_frames[-1]))
            self.listWidget.addItem(self.question_frames[-1])
            self.listWidget.setItemWidget(self.question_frames[-1], self.question_widgets[-1])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "总分: {:3d}/{:3d}".format(0,0)))
        self.label_2.setText(_translate("Form", "排名: {:3d}/{:3d}".format(0,0)))