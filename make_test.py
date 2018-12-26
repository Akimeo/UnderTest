# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'make_test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setObjectName("tab")
        self.horizontalLayout.addWidget(self.tab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_open = QtWidgets.QAction(MainWindow)
        self.act_open.setObjectName("act_open")
        self.act_save = QtWidgets.QAction(MainWindow)
        self.act_save.setEnabled(False)
        self.act_save.setObjectName("act_save")
        self.act_saveAs = QtWidgets.QAction(MainWindow)
        self.act_saveAs.setObjectName("act_saveAs")
        self.act_close = QtWidgets.QAction(MainWindow)
        self.act_close.setObjectName("act_close")
        self.act_run = QtWidgets.QAction(MainWindow)
        self.act_run.setObjectName("act_run")
        self.act_del_question = QtWidgets.QAction(MainWindow)
        self.act_del_question.setObjectName("act_del_question")
        self.act_add_question = QtWidgets.QAction(MainWindow)
        self.act_add_question.setObjectName("act_add_question")
        self.act_add_ans = QtWidgets.QAction(MainWindow)
        self.act_add_ans.setObjectName("act_add_ans")
        self.menu.addAction(self.act_open)
        self.menu.addAction(self.act_run)
        self.menu.addSeparator()
        self.menu.addAction(self.act_save)
        self.menu.addAction(self.act_saveAs)
        self.menu.addSeparator()
        self.menu.addAction(self.act_close)
        self.menu_2.addAction(self.act_add_question)
        self.menu_2.addAction(self.act_del_question)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.act_add_ans)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Формат"))
        self.act_open.setText(_translate("MainWindow", "Открыть"))
        self.act_save.setText(_translate("MainWindow", "Сохранить"))
        self.act_saveAs.setText(_translate("MainWindow", "Сохранить как"))
        self.act_close.setText(_translate("MainWindow", "Закрыть"))
        self.act_run.setText(_translate("MainWindow", "Запустить"))
        self.act_del_question.setText(_translate("MainWindow", "Удалить вопрос"))
        self.act_add_question.setText(_translate("MainWindow", "Добавить вопрос"))
        self.act_add_ans.setText(_translate("MainWindow", "Добавить вариант ответа"))

