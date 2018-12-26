# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radio_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 313)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.ans = QtWidgets.QLineEdit(Form)
        self.ans.setReadOnly(False)
        self.ans.setObjectName("ans")
        self.horizontalLayout_2.addWidget(self.ans)
        self.delete_btn = QtWidgets.QPushButton(Form)
        self.delete_btn.setMaximumSize(QtCore.QSize(22, 22))
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_2.addWidget(self.delete_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.delete_btn.setText(_translate("Form", "X"))

