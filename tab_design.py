# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(854, 552)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RB_1 = QtWidgets.QRadioButton(Form)
        self.RB_1.setChecked(True)
        self.RB_1.setObjectName("RB_1")
        self.RBG = QtWidgets.QButtonGroup(Form)
        self.RBG.setObjectName("RBG")
        self.RBG.addButton(self.RB_1)
        self.horizontalLayout.addWidget(self.RB_1)
        self.RB_2 = QtWidgets.QRadioButton(Form)
        self.RB_2.setChecked(False)
        self.RB_2.setObjectName("RB_2")
        self.RBG.addButton(self.RB_2)
        self.horizontalLayout.addWidget(self.RB_2)
        self.RB_3 = QtWidgets.QRadioButton(Form)
        self.RB_3.setObjectName("RB_3")
        self.RBG.addButton(self.RB_3)
        self.horizontalLayout.addWidget(self.RB_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.add_var = QtWidgets.QPushButton(Form)
        self.add_var.setEnabled(True)
        self.add_var.setObjectName("add_var")
        self.horizontalLayout_2.addWidget(self.add_var)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.RB_1.setText(_translate("Form", "Один правильный вариант"))
        self.RB_2.setText(_translate("Form", "Несколько правильных вариантов"))
        self.RB_3.setText(_translate("Form", "Без вариантов"))
        self.add_var.setText(_translate("Form", "Добавить вариант"))

