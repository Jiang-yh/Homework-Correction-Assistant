import os, sys
sys.path.append(os.path.dirname(os.getcwd()))

from PyQt5 import QtWidgets

from login import Ui_MainWindow as Login_window
from register import Ui_MainWindow as Register_window
from homepage import Homepage
from db import Mydatabase
from gui_threads import Load_models

database = Mydatabase('localhost','root','10290293','homework_view')

def login2register(lgn, rgst):
    lgn.hide()
    rgst.show()

def register2login(lgn, rgst):
    rgst.hide()
    lgn.show()

def homepage2login(lgn, hmpg):
    hmpg.close()
    lgn.show()

def login2homepage(lgn, hmpg):
    lgn.hide()
    hmpg.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # person = Account()
    load_model_obj = Load_models()
    # model_threads = load_model_obj.load_threads
    login, register, homepage = Login_window(database), Register_window(database), Homepage(database, load_model_obj)
    login.pushButton_3.clicked.connect(lambda :login2register(login, register))
    register.pushButton_2.clicked.connect(lambda :register2login(login, register))
    login.activate_homepage.connect(lambda : homepage.show(login.account))
    homepage.activate_login.connect(lambda :homepage2login(login, homepage.hmpg))
    login.show()

    # homepage = Student_window()
    # login.pushButton.clicked.connect(lambda :login2homepage(login, homepage))
    # homepage.pushButton_4.clicked.connect(lambda :homepage2login(login, homepage))

    sys.exit(app.exec_())