# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:blue")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tests_20 = QtWidgets.QRadioButton(self.groupBox)
        self.tests_20.setChecked(True)
        self.tests_20.setObjectName("tests_20")
        self.horizontalLayout.addWidget(self.tests_20)
        self.tests_30 = QtWidgets.QRadioButton(self.groupBox)
        self.tests_30.setObjectName("tests_30")
        self.horizontalLayout.addWidget(self.tests_30)
        self.tests_40 = QtWidgets.QRadioButton(self.groupBox)
        self.tests_40.setObjectName("tests_40")
        self.horizontalLayout.addWidget(self.tests_40)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.dom_I = QtWidgets.QRadioButton(self.groupBox_2)
        self.dom_I.setChecked(True)
        self.dom_I.setAutoExclusive(False)
        self.dom_I.setObjectName("dom_I")
        self.gridLayout.addWidget(self.dom_I, 0, 0, 1, 1)
        self.dom_II = QtWidgets.QRadioButton(self.groupBox_2)
        self.dom_II.setAutoExclusive(False)
        self.dom_II.setObjectName("dom_II")
        self.gridLayout.addWidget(self.dom_II, 0, 1, 1, 1)
        self.dom_III = QtWidgets.QRadioButton(self.groupBox_2)
        self.dom_III.setAutoExclusive(False)
        self.dom_III.setObjectName("dom_III")
        self.gridLayout.addWidget(self.dom_III, 1, 0, 1, 1)
        self.dom_IV = QtWidgets.QRadioButton(self.groupBox_2)
        self.dom_IV.setAutoExclusive(False)
        self.dom_IV.setObjectName("dom_IV")
        self.gridLayout.addWidget(self.dom_IV, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.generate.setFont(font)
        self.generate.setObjectName("generate")
        self.verticalLayout.addWidget(self.generate)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.last_test_accuracy = QtWidgets.QLabel(self.groupBox_3)
        self.last_test_accuracy.setObjectName("last_test_accuracy")
        self.gridLayout_2.addWidget(self.last_test_accuracy, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)
        self.last_test_datetime = QtWidgets.QDateTimeEdit(self.groupBox_3)
        self.last_test_datetime.setReadOnly(True)
        self.last_test_datetime.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.last_test_datetime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.last_test_datetime.setTime(QtCore.QTime(12, 0, 0))
        self.last_test_datetime.setObjectName("last_test_datetime")
        self.gridLayout_2.addWidget(self.last_test_datetime, 0, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 2, 1, 1)
        self.last_test_right_answers = QtWidgets.QLabel(self.groupBox_3)
        self.last_test_right_answers.setObjectName("last_test_right_answers")
        self.gridLayout_2.addWidget(self.last_test_right_answers, 1, 1, 1, 1)
        self.last_test_wrong_answers = QtWidgets.QLabel(self.groupBox_3)
        self.last_test_wrong_answers.setObjectName("last_test_wrong_answers")
        self.gridLayout_2.addWidget(self.last_test_wrong_answers, 3, 1, 1, 1)
        self.last_test_duration = QtWidgets.QLabel(self.groupBox_3)
        self.last_test_duration.setObjectName("last_test_duration")
        self.gridLayout_2.addWidget(self.last_test_duration, 3, 3, 1, 1)
        self.show_statistics = QtWidgets.QPushButton(self.groupBox_3)
        self.show_statistics.setMinimumSize(QtCore.QSize(0, 50))
        self.show_statistics.setObjectName("show_statistics")
        self.gridLayout_2.addWidget(self.show_statistics, 4, 0, 1, 4)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Generator"))
        self.label.setText(_translate("MainWindow", "Generator de Teste"))
        self.groupBox.setTitle(_translate("MainWindow", "Numarul de teste"))
        self.tests_20.setText(_translate("MainWindow", "20 teste"))
        self.tests_30.setText(_translate("MainWindow", "30 teste"))
        self.tests_40.setText(_translate("MainWindow", "40 teste"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Domenii"))
        self.dom_I.setText(_translate("MainWindow", "Domeniul I"))
        self.dom_II.setText(_translate("MainWindow", "Domeniul II"))
        self.dom_III.setText(_translate("MainWindow", "Domeniul III"))
        self.dom_IV.setText(_translate("MainWindow", "Domeniul IV"))
        self.generate.setText(_translate("MainWindow", "Generare"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Rezultatele ultimului test"))
        self.last_test_accuracy.setText(_translate("MainWindow", "No Data"))
        self.label_2.setText(_translate("MainWindow", "Data efectuării:"))
        self.label_5.setText(_translate("MainWindow", "Acuratețe:"))
        self.last_test_datetime.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy hh:mm"))
        self.label_3.setText(_translate("MainWindow", "Răspunsuri corecte:"))
        self.label_4.setText(_translate("MainWindow", "Răspunsuri gresite:"))
        self.label_6.setText(_translate("MainWindow", "Durata:"))
        self.last_test_right_answers.setText(_translate("MainWindow", "No Data"))
        self.last_test_wrong_answers.setText(_translate("MainWindow", "No Data"))
        self.last_test_duration.setText(_translate("MainWindow", "No Data"))
        self.show_statistics.setText(_translate("MainWindow", "Arata statistica totală"))
