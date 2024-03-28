# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/questionset.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from gui_utils import ChangequestionButton, AdminTableButton

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, parent, db, question, dex, for_create=False):
        super(Ui_Form,self).__init__()
        self.parent, self.question, self.dex = parent, question, dex
        self.db = db

        self.setupUi(self)
        self.retranslateUi(self)

        if self.question is None:
            self.question = [None, None, None, None, 0]
        self.textEdit.setText(self.question[2])
        self.textEdit_2.setText(self.question[3])
        self.comboBox.setCurrentIndex(self.question[-1])

        if not for_create:
            self.pushButton.clicked.connect(self.confirm_change)
            self.pushButton_2.clicked.connect(self.confirm_delete)
            self.pushButton_3.clicked.connect(self.close)
        else:
            self.pushButton_3.hide()
            self.pushButton_2.clicked.connect(self.close)
            self.pushButton_2.setText('取消')
            self.pushButton.setText('确认')
            self.pushButton.clicked.connect(self.confirm_add)

    def confirm_change(self):
        user_id, question_id, question, answer, question_type = \
            self.question[0], self.question[1], self.textEdit.toPlainText(), self.textEdit_2.toPlainText(), self.comboBox.currentIndex()
        self.db.modify_question(user_id, question_id, question, answer, question_type)
        self.parent.question_page_lst[self.dex][2], self.parent.question_page_lst[self.dex][3], self.parent.question_page_lst[self.dex][4] = \
            question, answer, question_type
        self.parent.tableWidget_3.setItem(self.dex, 0, QtWidgets.QTableWidgetItem(question))
        self.parent.tableWidget_3.setItem(self.dex, 1, QtWidgets.QTableWidgetItem('客观题' if question_type else '主观题'))
        self.parent.tableWidget_3.setItem(self.dex, 2, QtWidgets.QTableWidgetItem(answer))

        self.close()

    def confirm_delete(self):
        self.db.del_question(self.question[0], self.question[1])
        self.parent.tableWidget_3.removeRow(self.dex)
        del self.parent.question_page_lst[self.dex]
        del self.parent.line_dexes[self.dex]
        self.close()

    def confirm_add(self):
        question, answer, question_type = \
            self.textEdit.toPlainText(), self.textEdit_2.toPlainText(), self.comboBox.currentIndex()
        uid, qid = self.db.save_question(self.db.account2userid(self.parent.account.id), None, question, answer, question_type)
        dex = self.parent.tableWidget_3.rowCount()
        self.parent.tableWidget_3.insertRow(dex)
        self.parent.tableWidget_3.setItem(dex, 0, QtWidgets.QTableWidgetItem(question))
        if question_type:
            self.parent.tableWidget_3.setItem(dex, 1, QtWidgets.QTableWidgetItem("客观题"))
        else:
            self.parent.tableWidget_3.setItem(dex, 1, QtWidgets.QTableWidgetItem("主观题"))
        self.parent.tableWidget_3.setItem(dex, 2, QtWidgets.QTableWidgetItem(answer))

        self.parent.buttons.append(AdminTableButton(self.parent.tableWidget_3, text='点击修改该题'))
        self.parent.buttons[-1].clicked.connect(self.parent.create_change_question_page)
        self.parent.tableWidget_3.setCellWidget(dex, 3, self.parent.buttons[-1])
        self.parent.checkboxes.append(QtWidgets.QCheckBox('点击添加至作业'))
        self.parent.checkboxes[-1].setChecked(False)
        self.parent.tableWidget_3.setCellWidget(dex, 4, self.parent.checkboxes[-1])

        self.parent.question_page_lst.append([uid, qid, question, answer, question_type])

        self.parent.button_cnt += 1
        self.parent.line_dexes.append(self.parent.button_cnt)
        self.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(654, 519)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 160, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 160, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 160, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(221, 160, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        Form.setStyleSheet("Qwidget{\n"
"    background-color: #DA70D6;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 70, 51, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 250, 51, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(170, 70, 381, 101))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(170, 190, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('主观题')
        self.comboBox.addItem('客观题')
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(170, 250, 381, 101))
        self.textEdit_2.setObjectName("textEdit_2")
        # self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton = ChangequestionButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 380, 121, 41))
        self.pushButton.setObjectName("pushButton")
        # self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2 = ChangequestionButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 380, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3 = ChangequestionButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 440, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "题目:"))
        self.label_2.setText(_translate("Form", "题型:"))
        self.label_3.setText(_translate("Form", "答案:"))
        self.pushButton.setText(_translate("Form", "确认修改"))
        self.pushButton_2.setText(_translate("Form", "确认移除"))
        self.pushButton_3.setText(_translate("Form", "取消"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_Form()
    ui.show()

    sys.exit(app.exec_())