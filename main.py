from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import datetime
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(426, 516)
        Form.setMinimumSize(QtCore.QSize(426, 516))
        Form.setMaximumSize(QtCore.QSize(426, 516))
        Form.setSizeIncrement(QtCore.QSize(0, 0))
        Form.setStyleSheet("background-color: rgb(185, 213, 239);")
        Form.setWindowFlags(TAP.windowFlags() | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.checkBox_Headless = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_Headless.setGeometry(QtCore.QRect(17, 9, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.checkBox_Headless.setFont(font)
        self.checkBox_Headless.setText("")
        self.checkBox_Headless.setChecked(True)
        self.checkBox_Headless.setObjectName("checkBox_Headless")
        self.spinBox = QtWidgets.QSpinBox(parent=Form)
        self.spinBox.setGeometry(QtCore.QRect(223, 9, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        self.spinBox.setFont(font)
        self.spinBox.setAutoFillBackground(False)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.spinBox.setReadOnly(False)
        self.spinBox.setAccelerated(False)
        self.spinBox.setKeyboardTracking(True)
        self.spinBox.setProperty("showGroupSeparator", False)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(25)
        self.spinBox.setObjectName("spinBox")
        self.dateEdit = QtWidgets.QDateEdit(parent=Form)
        self.dateEdit.setGeometry(QtCore.QRect(46, 9, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.dateEdit.setWrapping(False)
        self.dateEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.dateEdit.setProperty("showGroupSeparator", False)
        today = datetime.date.today()
        self.dateEdit.setMinimumDate(QtCore.QDate(today.year, today.month, today.day))
        # self.dateEdit.setMinimumDate(QtCore.QDate(2025, 2, 17))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(QtCore.Qt.TimeSpec.LocalTime)
        self.dateEdit.setObjectName("dateEdit")
        self.spinBox_2 = QtWidgets.QSpinBox(parent=Form)
        self.spinBox_2.setGeometry(QtCore.QRect(350, 10, 51, 22))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(3)
        self.spinBox_2.setProperty("value", 3)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(parent=Form)
        self.spinBox_3.setGeometry(QtCore.QRect(215, 479, 51, 22))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(123)
        self.spinBox_3.setProperty("value", 42)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(173, 9, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(126, 480, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(284, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(69, 476, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(74, 153, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(284, 476, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(74, 153, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(16, 476, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(74, 153, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(343, 476, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(74, 153, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QtCore.QRect(6, 37, 418, 431))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.East)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(parent=self.tab)
        self.textEdit.setGeometry(QtCore.QRect(2, 2, 389, 421))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.tab_3)
        self.textEdit_2.setGeometry(QtCore.QRect(49, 0, 311, 421))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(self.start_starost)
        self.pushButton_3.clicked.connect(self.start_dvn)
        self.pushButton_4.clicked.connect(self.start_dn)
        self.pushButton_5.clicked.connect(self.start_anketa)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Карт:"))
        self.label_2.setText(_translate("Form", "Диагноз:"))
        self.label_3.setText(_translate("Form", "Услуга:"))
        self.pushButton_2.setText(_translate("Form", "65+"))
        self.pushButton_3.setText(_translate("Form", "ДВН"))
        self.pushButton_4.setText(_translate("Form", "ДН"))
        self.pushButton_5.setText(_translate("Form", "Анкета"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Ссылки"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"0\">\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">1:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J12.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">31:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I05.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">62:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I25.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">93:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I45.8</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">2:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J12.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">32:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I05.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">63:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I25.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">94:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I45.9</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">3:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J41.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">33:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I05.2</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">64:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I26.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">95:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I47.0</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">4:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J41.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">34:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I06.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">65:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I34.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">96:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I47.1</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">5:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J44.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">35:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I06.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">66:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I34.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">97:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I47.2</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">6:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J44.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">36:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I08.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">67:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I34.2</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">98:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I47.9</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">7:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J44.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">37:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I08.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">68:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I34.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">99:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I48.0</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">8:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J45.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">38:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I08.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">69:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I34.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">100:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I48.1</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">9:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J45.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">39:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I08.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">70:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I35.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">101:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I48.2</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">10:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J45.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">40:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I10</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">71:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I35.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">102:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I48.3</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">11:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J45.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">41:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I11.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">72:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I35.2</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">103:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I48.9</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">12:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">J47</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">42:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I11.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">73:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I35.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">104:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I49.0</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\"></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\"></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">43:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I12.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">74:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I36.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">105:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I49.1</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">13:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">R73.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">44:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I15.2</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">75:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I37.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">106:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I49.3</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">14:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">R73.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">45:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I15.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">76:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I39.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">107:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I49.4</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">15:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">E11.7</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">46:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I15.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">77:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I40.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">108:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I49.5</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">16:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">E11.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">47:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I20.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">78:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I41.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">109:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I49.8</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">17:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">E11.6</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">48:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I20.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">79:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I42.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">110:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I49.9</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">18:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">E11.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">49:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I20.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">80:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I42.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">111:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I50.0</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">19:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">E11.4</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">50:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I20.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">81:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I42.2</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">112:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I50.1</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">20:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">E66.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">51:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I21.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">82:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I42.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">113:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I50.9</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">21:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">E66.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">52:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I21.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">83:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I42.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">114:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I65.2</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">22:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">B18.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">53:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I21.2</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">84:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I43.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">115:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I67.8</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">23:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">B18.2</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">54:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I21.4</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">85:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I44.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">116:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I69.0</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">24:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">B18.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">55:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I21.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">86:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I44.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">117:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I69.1</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">25:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">K74.3</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">56:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I22.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">87:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I44.2</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">118:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I69.2</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">26:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">K74.6</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">57:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I22.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">88:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I44.4</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">119:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I69.3</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">27:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">K86.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">58:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I25.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">89:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I44.7</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">120:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I69.4</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">28:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">K86.2</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">59:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I25.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">90:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I45.0</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">121:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I71.0</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">29:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">K86.8</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">60:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I25.2</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">91:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I45.1</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">122:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I71.2</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">30:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">K86.9</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">61:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I25.5</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">92:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I45.6</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; font-style:italic;\">123:</span></p></td>\n"
"<td style=\" vertical-align:bottom; padding-left:3; padding-right:3; padding-top:2; padding-bottom:2;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cambria\'; font-size:10pt; font-weight:600;\">I71.4</span></p></td></tr></table></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Диагнозы"))

    def process_card(self, card_url, headless_mode, date):  # Диспансеризация
        options = webdriver.ChromeOptions()
        if headless_mode:
            options.add_argument("--headless")  # Запуск в headless режиме
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--disable-blink-features=AutomationControlled")

        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

        try:
            driver.get(card_url)
            WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(("xpath", "//span[contains(text(), 'ГБУЗ МОСКОВСКОЙ ОБЛАСТИ')]")))
            WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(("xpath", "//span[text()='Осмотр, исследование, иное медицинское мероприятие']")))
            start_time = time.time()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("xpath", "//button[@mattooltip='Ввод даты выполнения мероприятия']")))
            time.sleep(0.5)
            PACIENT = driver.find_element("xpath","//html/body/app-root/ng-component/header/app-header/header/div/div[2]/div[2]/div[1]/div/span[2]").text
            print(str(PACIENT) + " - Оформление")
            WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(("xpath", "//span[text()='Дата проведения']")))
            driver.execute_script("window.scrollTo(0, 0);")
            WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(("xpath", "//span[text()='Дата проведения']")))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("xpath", "//label[text()='Все мероприятия']")))
            time.sleep(0.2)
            driver.find_element("xpath", "//label[text()='Все мероприятия']").click()

            try: #ВГД
                glaznoe_davlenie = driver.find_element("xpath", "//div[text()=' Измерение внутриглазного давления ']")
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",  glaznoe_davlenie)
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//div[text()=' Измерение внутриглазного давления ']")))
                time.sleep(0.2)
                glaznoe_davlenie.click()
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//th[text()='Значение']")))
                time.sleep(0.5)
                vgds = driver.find_elements("xpath", "//input[@formcontrolname='value']")
                for vgd in vgds:
                    vgd.clear()
                    vgd.send_keys("15")
                glaznoe_davlenie.click()
                time.sleep(1)
                # driver.execute_script("window.scrollTo(0, 0);")
            except NoSuchElementException:
                pass

            try: #Сатурация
                saturaciy = driver.find_element("xpath", "//div[text()=' Измерение насыщения крови кислородом (сатурация) в покое ']")
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });", saturaciy)
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//div[text()=' Измерение насыщения крови кислородом (сатурация) в покое ']")))
                time.sleep(0.5)
                saturaciy.click()
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//input[@formcontrolname='value']")))
                driver.find_element("xpath", "//input[@formcontrolname='value']").clear()
                driver.find_element("xpath", "//input[@formcontrolname='value']").send_keys("99")
                saturaciy.click()
                time.sleep(1)
                # driver.execute_script("window.scrollTo(0, 0);")
            except NoSuchElementException:
                pass

            try: #Д-димер
                d_dimer = driver.find_element("xpath","//div[text()=' Определение концентрации Д-димера  ']")
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });", d_dimer)
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath","//div[text()=' Определение концентрации Д-димера  ']")))
                time.sleep(1)
                d_dimer.click()
                time.sleep(1)
                vrach = driver.find_element("xpath", "//th[text()='№ Направления'][1]")
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });", vrach)
                time.sleep(0.7)
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//mat-label[text()='Врач']")))
                driver.find_element("xpath", "//mat-label[text()='Врач']").click()
                time.sleep(1)
                driver.find_element("xpath","//span[text()=' 00169 - Кадыкова Татьяна Александровна (Врач-лаборант, Клинико-диагностическая лаборатория, Стационар, филиал Центральный (Королёвская больница)) ']").click()
                time.sleep(1)
                driver.execute_script("window.scrollBy(0, -300);")
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//div[text()=' Определение концентрации Д-димера  ']")))
                d_dimer.click()
                time.sleep(0.5)
            except NoSuchElementException:
                pass

            driver.execute_script("window.scrollTo(0, 0);")
            merops = driver.find_elements("xpath", "//button[@mattooltip='Ввод даты выполнения мероприятия']")
            for merop in merops:
                try:
                    WebDriverWait(driver, 1).until(EC.element_to_be_clickable(merop))
                    merop.click()
                    time.sleep(0.5)
                    driver.find_element("xpath", "//input[contains(@id, 'mat-input-')]").clear()
                    time.sleep(0.1)
                    driver.find_element("xpath", "//input[contains(@id, 'mat-input-')]").send_keys(date)
                    time.sleep(0.1)
                    driver.find_element("xpath", "//button[@mattooltip='Подтвердить']").click()
                    time.sleep(0.1)
                    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(("xpath", "//button[@mattooltip='Подтвердить']")))
                    time.sleep(0.1)
                    driver.execute_script("window.scrollBy(0, 105);")
                except Exception as e:
                    pass

            if len(merops) > 0:
                driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(0.5)
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//h1[text()='Карта мероприятий']")))
                checkbox_ids = [
                    '//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[1]/div/app-exam/div/div[3]/div/div[4]/mat-checkbox/div/div/input',
                    '//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[2]/div/app-exam/div/div[3]/div/div[4]/mat-checkbox/div/div/input',
                    '//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[3]/div/app-exam/div/div[3]/div/div[4]/mat-checkbox/div/div/input',
                    '//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[4]/div/app-exam/div/div[3]/div/div[4]/mat-checkbox/div/div/input',
                    '//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[5]/div/app-exam/div/div[3]/div/div[4]/mat-checkbox/div/div/input',
                    '//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[6]/div/app-exam/div/div[3]/div/div[4]/mat-checkbox/div/div/input',
                    '//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[7]/div/app-exam/div/div[3]/div/div[4]/mat-checkbox/div/div/input',
                    '//html/body/app-root/ng-component/div/main/app-disp/div/disp-card-edit/card-disp/div[1]/form/app-disp-exams-map/div[2]/div[2]/div[8]/div/app-exam/div/div[3]/div/div[4]/mat-checkbox/div/div/input',]
                for checkbox_id in checkbox_ids:
                    try:
                        checkbox = driver.find_element("xpath", checkbox_id)
                        if not checkbox.is_selected():
                            checkbox.click()
                            time.sleep(0.5)
                            driver.execute_script("window.scrollBy(0, 93);")
                    except ElementClickInterceptedException:
                        pass

            try:
                time.sleep(0.15)
                driver.execute_script("window.scrollTo(0, 0);")
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//h1[text()='Карта мероприятий']")))
                # PACIENT = driver.find_element("xpath","//html/body/app-root/ng-component/header/app-header/header/div/div[2]/div[2]/div[1]/div/span[2]").text
                PROCENT = driver.find_element("xpath","(//div[contains(@class, 'mat-mdc-tooltip-trigger progress-percent ng-tns')])").text
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[text()= ' День семейного здоровья ']")))
                driver.find_element("xpath","//div[text()= ' День семейного здоровья ']").click()
                time.sleep(0.1)
                driver.find_element("xpath","//div[text()= ' Плановая диспансеризация/осмотр ']").click()

                das = driver.find_elements("xpath", "//div[text()=' Да ']")
                for da in das:
                    da.click()

                nets = driver.find_elements("xpath", "//div[text()=' Нет ']")
                for net in nets:
                    net.click()

                today_date = datetime.now().strftime("%d.%m.%Y")
                driver.find_element("xpath", "//input[contains(@class, 'mat-mdc-input-element mat-mdc-tooltip-trigger ng-tns')]").clear()
                time.sleep(0.2)
                driver.find_element("xpath", "//input[contains(@class, 'mat-mdc-input-element mat-mdc-tooltip-trigger ng-tns')]").send_keys(today_date)
                time.sleep(0.2)
            except NoSuchElementException:
                pass

            try: #ТАП
                tap = driver.find_element("xpath","//div[contains(text(), ' Прием ')]")
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });", tap)
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//div[contains(text(), ' Прием ')]")))
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[contains(text(), ' Прием ')]"))).click()
                time.sleep(1)

                  #переделать
                if driver.find_element("xpath", "//span[text()='Добавить']"):  #Диагноз
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//span[text()='Добавить']"))).click()
                    time.sleep(0.2)
                    WebDriverWait(driver, 1.5).until(EC.visibility_of_element_located(("xpath", "//mat-label[text()='Тип']")))
                    WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable(("xpath", "//mat-label[text()='Тип']"))).click()
                    time.sleep(0.2)
                    WebDriverWait(driver, 2.5).until(EC.visibility_of_element_located(("xpath", "//span[text()=' 1 - Основной ']")))
                    WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable(("xpath", "//span[text()=' 1 - Основной ']"))).click()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//mat-label[text()='Диагноз']")))
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//mat-label[text()='Диагноз']"))).click()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "(//input[contains(@id, 'mat-input-')])[4]")))
                    driver.find_element("xpath","(//input[contains(@id, 'mat-input-')])[4]").send_keys("Z00.8 - Другие общие осмотры")
                    time.sleep(0.5)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "(//input[contains(@id, 'mat-input-')])[4]"))).click()
                    time.sleep(0.5)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//button[text()='Сохранить']"))).click()
                    time.sleep(0.5)
                else:
                    print("Ошибка в диагнозе")
            except NoSuchElementException:
                pass

            try: #Осмотр
                karandashik = driver.find_element("xpath", "//button[@class='arrow ng-star-inserted']")
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",karandashik)
                time.sleep(1)

                if driver.find_element("xpath", "//button[@class='arrow ng-star-inserted']"):
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//button[@class='arrow ng-star-inserted']"))).click()
                    time.sleep(0.5)
                    iframe_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("xpath", "//iframe[@class='template ng-star-inserted']")))
                    driver.switch_to.frame(iframe_tab)
                    time.sleep(1)

                    pole1 = driver.find_element("xpath", "//div[@id='multiLineTextDiv1']")
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",pole1)
                    time.sleep(0.5)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@id='multiLineTextDiv1']"))).clear()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@id='multiLineTextDiv1']"))).send_keys(".")
                    time.sleep(0.2)

                    pole2 = driver.find_element("xpath", "//div[@id='multiLineTextDiv2']")
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",pole2)
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@id='multiLineTextDiv2']"))).clear()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@id='multiLineTextDiv2']"))).send_keys(".")
                    time.sleep(0.2)

                    pole3 = driver.find_element("xpath", "//div[@id='multiLineTextDiv3']")
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",pole3)
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@id='multiLineTextDiv3']"))).clear()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@id='multiLineTextDiv3']"))).send_keys(".")
                    time.sleep(0.2)

                    poleSD = driver.find_element("xpath", "//span[@id='singleLineText5']")
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",poleSD)
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//input[@id='singleLineTextInput13']"))).clear()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//input[@id='singleLineTextInput13']"))).send_keys("125")
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//input[@id='singleLineTextInput14']"))).clear()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//input[@id='singleLineTextInput14']"))).send_keys("85")
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//input[@id='singleLineTextInput11']"))).clear()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//input[@id='singleLineTextInput11']"))).send_keys("36.6")
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//input[@id='singleLineTextInput12']"))).clear()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//input[@id='singleLineTextInput12']"))).send_keys("98")
                    time.sleep(0.2)

                    try:
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//span[@class='select2-arrow'][1]"))).click()
                        time.sleep(0.5)
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//html/body/div[31]/ul"))).click()
                        time.sleep(0.3)
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//span[@class='select2-arrow'][1]"))).click()
                        time.sleep(1)
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//input[@id='s2id_autogen1_search']"))).send_keys("Удовлетворительное")
                        time.sleep(1.5)
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//html/body/div[31]/ul"))).click()
                        time.sleep(1.5)
                    except NoSuchElementException:
                        pass

                    pole_net = driver.find_element("xpath", "//span[@id='rcMKB2']")
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",pole_net)
                    time.sleep(0.5)

                    das = driver.find_elements("xpath", "//span[text()='да']")
                    for da in das:
                        da.click()

                    nets = driver.find_elements("xpath", "//span[text()='нет']")
                    for net in nets:
                        net.click()

                    try:
                        driver.find_element("xpath", "//input[@id='singleLineTextInput5']").clear()
                        driver.find_element("xpath", "//input[@id='singleLineTextInput5']").send_keys("0.4")
                    except NoSuchElementException:
                        pass

                    pole6 = driver.find_element("xpath", "//div[@id='multiLineTextDiv5']")
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",pole6)
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@id='multiLineTextDiv5']"))).clear()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@id='multiLineTextDiv5']"))).send_keys(".")

                    pole7 = driver.find_element("xpath", "//div[@id='multiLineTextDiv6']")
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });",pole7)
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@id='multiLineTextDiv6']"))).clear()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//div[@id='multiLineTextDiv6']"))).send_keys(".")
                    time.sleep(0.2)
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//button[text()=' Просмотреть ']"))).click()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//button[text()=' Подписать и отправить ']"))).click()
                    time.sleep(0.2)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//button[text()=' Снять подпись ']")))

                    end_time = time.time()
                    result = end_time - start_time
                    result_rounded = round(result, 1)
                    # print(PACIENT)
                    print('Карта оформлена на: ' + str(PROCENT) + ' затрачено: ' + str(result_rounded) + ' сек.')

            except Exception as e:
                PACIENT = driver.find_element("xpath","//html/body/app-root/ng-component/header/app-header/header/div/div[2]/div[2]/div[1]/div/span[2]").text
                print(PACIENT, "- ОШИБКА в осмотре!")
                pass

        except Exception as e:
            PACIENT = driver.find_element("xpath","//html/body/app-root/ng-component/header/app-header/header/div/div[2]/div[2]/div[1]/div/span[2]").text
            print(PACIENT, "- при заполнении возникла ОШИБКА!")

        finally:
            driver.quit()

    def start_dvn(self):
        card_urls_text = self.textEdit.toPlainText()
        card_urls = [card.strip() for card in card_urls_text.split(',') if card.strip()]
        headless_mode = self.checkBox_Headless.isChecked()
        date = self.dateEdit.text()
        kolvo = self.spinBox.value()
        with ThreadPoolExecutor(max_workers=kolvo) as executor:
            executor.map(lambda url: self.process_card(url, headless_mode, date), card_urls)

    def process_card2(self, card_url, headless_mode, date): # Диспансерное наблюдение
        options = webdriver.ChromeOptions()
        if headless_mode:
            options.add_argument("--headless")  # Запуск в headless режиме
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--disable-blink-features=AutomationControlled")
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        try:
            driver.get(card_url)
             # код ДН

        except NoSuchElementException:
            pass
    def start_dn(self):
        card_urls_text = self.textEdit.toPlainText()
        card_urls = [card.strip() for card in card_urls_text.split(',') if card.strip()]
        headless_mode = self.checkBox_Headless.isChecked()
        date = self.dateEdit.text()
        kolvo = self.spinBox.value()
        with ThreadPoolExecutor(max_workers=kolvo) as executor:
            executor.map(lambda url: self.process_card2(url, headless_mode, date), card_urls)

    def process_card3(self, card_url, headless_mode, date): #Старость
        options = webdriver.ChromeOptions()
        if headless_mode:
            options.add_argument("--headless")  # Запуск в headless режиме
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--disable-blink-features=AutomationControlled")
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        try:
            driver.get(card_url)
            #Код на Старость 65+
        except NoSuchElementException:
            pass

    def start_starost(self):
        card_urls_text = self.textEdit.toPlainText()
        card_urls = [card.strip() for card in card_urls_text.split(',') if card.strip()]
        headless_mode = self.checkBox_Headless.isChecked()
        date = self.dateEdit.text()
        kolvo = self.spinBox.value()
        with ThreadPoolExecutor(max_workers=kolvo) as executor:
            executor.map(lambda url: self.process_card3(url, headless_mode, date), card_urls)

    def process_card4(self, card_url, headless_mode, date): #Анкета по диспансеризации
        options = webdriver.ChromeOptions()
        if headless_mode:
            options.add_argument("--headless")  # Запуск в headless режиме
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--disable-blink-features=AutomationControlled")
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        try:
            driver.get(card_url)
            #Анкета по диспансеризации

        except NoSuchElementException:
            pass

    def start_anketa(self):
        card_urls_text = self.textEdit.toPlainText()
        card_urls = [card.strip() for card in card_urls_text.split(',') if card.strip()]
        headless_mode = self.checkBox_Headless.isChecked()
        date = self.dateEdit.text()
        kolvo = self.spinBox.value()
        with ThreadPoolExecutor(max_workers=kolvo) as executor:
            executor.map(lambda url: self.process_card4(url, headless_mode, date), card_urls)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    TAP = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(TAP)
    TAP.show()
    sys.exit(app.exec())
