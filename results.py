# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(473, 523)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.right_questions_nr = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.right_questions_nr.setFont(font)
        self.right_questions_nr.setObjectName("right_questions_nr")
        self.horizontalLayout.addWidget(self.right_questions_nr)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.wrong_questions_nr = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wrong_questions_nr.setFont(font)
        self.wrong_questions_nr.setObjectName("wrong_questions_nr")
        self.horizontalLayout_2.addWidget(self.wrong_questions_nr)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.accuracy = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.accuracy.setFont(font)
        self.accuracy.setAlignment(QtCore.Qt.AlignCenter)
        self.accuracy.setObjectName("accuracy")
        self.horizontalLayout_3.addWidget(self.accuracy)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.elapsed_time = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.elapsed_time.setFont(font)
        self.elapsed_time.setAlignment(QtCore.Qt.AlignCenter)
        self.elapsed_time.setObjectName("elapsed_time")
        self.verticalLayout.addWidget(self.elapsed_time)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_4.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Rezultatele testului"))
        self.right_questions_nr.setText(_translate("Dialog", "NR"))
        self.label_3.setText(_translate("Dialog", "Răspunsuri corecte"))
        self.wrong_questions_nr.setText(_translate("Dialog", "NR"))
        self.label_4.setText(_translate("Dialog", "Răspunsuri greșite"))
        self.label_2.setText(_translate("Dialog", "Însușirea materialului:"))
        self.accuracy.setText(_translate("Dialog", "TextLabel"))
        self.elapsed_time.setText(_translate("Dialog", "TextLabel"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
        self.cancel_btn.setText(_translate("Dialog", "Cancel"))