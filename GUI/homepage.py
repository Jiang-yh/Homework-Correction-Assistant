import os, sys
sys.path.append(os.path.dirname(os.getcwd()))

from PyQt5 import QtWidgets, QtCore

from student import Ui_MainWindow as Student_window
from administrator import Ui_MainWindow as Administrator_window
from teacher import Ui_MainWindow as Teacher_window

class Homepage(QtCore.QObject):
    activate_login = QtCore.pyqtSignal()
    def __init__(self, database, load_model_obj):
        super(Homepage, self).__init__()
        self.db, self.load_model_obj = database, load_model_obj
        # self.pushButton_4 = QtWidgets.QPushButton(None)
        # self.pushButton_4.clicked.connect(self.return_to_login)

    def return_to_login(self):
        self.activate_login.emit()

    def show(self, account):
        if account.identity == '学生':
            self.hmpg = Student_window(account, self.db, self.load_model_obj)
        elif account.identity == '教师':
            self.hmpg = Teacher_window(account, self.db)
        elif account.identity == '管理员':
            self.hmpg = Administrator_window(account, self.db)
        self.hmpg.pushButton_4.clicked.connect(self.return_to_login)
        self.hmpg.show()

if __name__ == '__main__':
    from db import Mydatabase
    database = Mydatabase('localhost', 'root', '10290293', 'homework_view')

    # database.save_question(5, 1, 'what are you talking about?', 'piaochanghao is SB', 0)
    # database.save_question(5, 2, '懂得都懂', 'piaochanghao is SB', 0)

    class Account:
        def __init__(self,):
            # self.id, self.name, self.identity, self.group, self.refer = 'xushaoyang', '徐邵洋', '学生', '人工智能实验班', '同学'
            self.id, self.name, self.identity, self.group, self.refer = 'piaochanghao', '嫖娼浩', '教师', '人工智能实验班', '老师'


    app = QtWidgets.QApplication(sys.argv)
    ui = Homepage(database, [])
    ui.show(Account())
    sys.exit(app.exec_())
