import re
import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
from sympy import Symbol, expand
from sympy.solvers import solve
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 472)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(161, 159, 162);\n"
                                  "color:rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 20, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 401, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.arithmetic_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arithmetic_btn.sizePolicy().hasHeightForWidth())
        self.arithmetic_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.arithmetic_btn.setFont(font)
        self.arithmetic_btn.setStyleSheet("background-color:rgb(255, 173, 93)")
        self.arithmetic_btn.setIconSize(QtCore.QSize(14, 14))
        self.arithmetic_btn.setObjectName("arithmetic_btn")
        self.verticalLayout.addWidget(self.arithmetic_btn)
        self.algebra_btn = QtWidgets.QPushButton(self.verticalLayoutWidget, clicked=lambda: self.open_alglin(True))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algebra_btn.sizePolicy().hasHeightForWidth())
        self.algebra_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.algebra_btn.setFont(font)
        self.algebra_btn.setStyleSheet("background-color:rgb(255, 173, 93)")
        self.algebra_btn.setIconSize(QtCore.QSize(67, 55))
        self.algebra_btn.setObjectName("algebra_btn")
        self.verticalLayout.addWidget(self.algebra_btn)
        self.functions_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.functions_btn.sizePolicy().hasHeightForWidth())
        self.functions_btn.setSizePolicy(sizePolicy)
        self.functions_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.functions_btn.setFont(font)
        self.functions_btn.setStyleSheet("background-color:rgb(255, 173, 93)")
        self.functions_btn.setObjectName("functions_btn")
        self.verticalLayout.addWidget(self.functions_btn)
        self.inequalities_btn = QtWidgets.QPushButton(self.verticalLayoutWidget, clicked=lambda: self.open_alglin())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inequalities_btn.sizePolicy().hasHeightForWidth())
        self.inequalities_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.inequalities_btn.setFont(font)
        self.inequalities_btn.setStyleSheet("background-color:rgb(255, 173, 93)")
        self.inequalities_btn.setObjectName("inequalities_btn")
        self.verticalLayout.addWidget(self.inequalities_btn)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMathCalcurator = QtWidgets.QAction(MainWindow)
        self.actionMathCalcurator.setObjectName("actionMathCalcurator")
        self.menu.addAction(self.actionMathCalcurator)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MathCalcurator"))
        self.label.setText(_translate("MainWindow", "Выбирите задачу для решения"))
        self.arithmetic_btn.setText(_translate("MainWindow", "Арифметика"))
        self.algebra_btn.setText(_translate("MainWindow", "Алгебра"))
        self.functions_btn.setText(_translate("MainWindow", "Функции с построением графика"))
        self.inequalities_btn.setText(_translate("MainWindow", "Неравенства"))
        self.menu.setTitle(_translate("MainWindow", "О программе"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.actionMathCalcurator.setText(
            _translate("MainWindow", "MathCalcurator - программа, которая поможет нам решать математику"))

        self.arithmetic_btn.clicked.connect(self.open_ariphmetic)
        self.functions_btn.clicked.connect(self.open_functions)

    def open_ariphmetic(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ariphmetic_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_functions(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Function_liney()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_alglin(self, al=False):
        self.window = QtWidgets.QMainWindow()
        self.ui = AlgLin()
        self.ui.setupUi(self.window, al)
        self.window.show()


class Ariphmetic_MainWindow(object):
    def __init__(self, *args):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(161, 159, 162);\n"
                                 "color:rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 400, 150, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color:rgb(255, 173, 93)")
        self.btn_0.setObjectName("btn_0")
        self.btn_equate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equate.setGeometry(QtCore.QRect(250, 400, 150, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equate.setFont(font)
        self.btn_equate.setStyleSheet("background-color:rgb(255, 130, 118)")
        self.btn_equate.setObjectName("btn_equate")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 310, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                 "")
        self.btn_1.setObjectName("btn_1")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 130, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                 "")
        self.btn_7.setObjectName("btn_7")
        self.btn_add_sub = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_sub.setGeometry(QtCore.QRect(100, 40, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_sub.setFont(font)
        self.btn_add_sub.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                       "")
        self.btn_add_sub.setObjectName("btn_add_sub")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 220, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                 "")
        self.btn_4.setObjectName("btn_4")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 310, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                 "")
        self.btn_2.setObjectName("btn_2")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 130, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                 "")
        self.btn_8.setObjectName("btn_8")
        self.btn_c = QtWidgets.QPushButton(self.centralwidget)
        self.btn_c.setGeometry(QtCore.QRect(0, 40, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_c.setFont(font)
        self.btn_c.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                 "")
        self.btn_c.setObjectName("btn_c")
        self.btn_procent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_procent.setGeometry(QtCore.QRect(200, 40, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_procent.setFont(font)
        self.btn_procent.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                       "")
        self.btn_procent.setObjectName("btn_procent")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 220, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                 "")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 220, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                 "")
        self.btn_6.setObjectName("btn_6")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 130, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                 "")
        self.btn_9.setObjectName("btn_9")
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sub.setGeometry(QtCore.QRect(300, 310, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sub.setFont(font)
        self.btn_sub.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                   "")
        self.btn_sub.setObjectName("btn_sub")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(300, 220, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                   "")
        self.btn_add.setObjectName("btn_add")
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mul.setGeometry(QtCore.QRect(300, 130, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mul.setFont(font)
        self.btn_mul.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                   "")
        self.btn_mul.setObjectName("btn_mul")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(300, 40, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                   "")
        self.btn_div.setObjectName("btn_div")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 310, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                 "")
        self.btn_3.setObjectName("btn_3")
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        self.btn_point.setGeometry(QtCore.QRect(150, 400, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_point.setFont(font)
        self.btn_point.setStyleSheet("background-color:rgb(255, 173, 93)\n"
                                     "")
        self.btn_point.setObjectName("btn_point")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

        self.btn_equate = False

        self.window = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_equate.setText(_translate("MainWindow", "="))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_add_sub.setText(_translate("MainWindow", "±"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_c.setText(_translate("MainWindow", "C"))
        self.btn_procent.setText(_translate("MainWindow", "%"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_mul.setText(_translate("MainWindow", "*"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_point.setText(_translate("MainWindow", "."))

    def add_function(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_add.clicked.connect(lambda: self.write_number(self.btn_add.text()))
        self.btn_procent.clicked.connect(lambda: self.write_number(self.btn_procent.text()))
        self.btn_mul.clicked.connect(lambda: self.write_number(self.btn_mul.text()))
        self.btn_sub.clicked.connect(lambda: self.write_number(self.btn_sub.text()))
        self.btn_add_sub.clicked.connect(lambda: self.write_number(self.btn_add_sub.text()))
        self.btn_point.clicked.connect(lambda: self.write_number(self.btn_point.text()))
        self.btn_div.clicked.connect(lambda: self.write_number(self.btn_div.text()))
        self.btn_equate.clicked.connect(self.results)
        self.btn_c.clicked.connect(self.clear)
        self.btn_add_sub.clicked.connect(self.negative)

    def write_number(self, number):
        if number == ".":
            # print('dot!')
            self.label.setText(self.label.text() + number)
        elif self.label.text() == "0" or self.btn_equate:
            self.label.setText(number)
            self.btn_equate = False
        else:
            self.label.setText(self.label.text() + number)

    def results(self):
        if not self.btn_equate:
            text = self.label.text()
            text = self.recalculate_percent(text)
            res = eval(text)
            self.label.setText("Результат:" + str(res))
            self.btn_equate = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Сейчас это действие выполнить нельзя")
            error.setIcon(QMessageBox.Warning)

            error.setStandardButtons(QMessageBox.Reset | QMessageBox.Cancel | QMessageBox.Ok)

            error.setInformativeText("Два раза действие не выполнить")
            error.setDetailedText("Детали")

            error.buttonClicked.connect(self.popup_action)
            error.exec()

    def recalculate_percent(self, example):
        result = re.findall(r"(\d*[\+\-\*\/]?\d*\%[\+\-\*\/]?\d*)", example)

        for el in result:
            perc = re.findall(r"(\d*\%)", el)
            num_perc = el.find(perc[0])
            if num_perc == 0:
                sub = re.split('\+|\-|\*|\/', el)
                to_replace = int(sub[1]) * int(sub[0][:-1]) / 100
                example = example.replace(sub[0], str(to_replace))
            else:
                sub = re.split('\+|\-|\*|\/', el)
                to_replace = int(sub[0]) * int(sub[1][:-1]) / 100
                example = example.replace(sub[1], str(to_replace))
        return example


    def popup_action(self, btn):
        if btn.text() == "Ok":
            print("Print ok")
        elif btn.text() == "Resert":
            self.label.setText("")
            self.btn_equate = False


    def clear(self):
        self.label.setText("0")


    def negative(self):
        try:
            res = eval(f'-{self.label.text()[:-1]}')
            self.label.setText(str(res))
        except SyntaxError:
            self.label.append('0')


    def procent(self):
        if not self.btn_procent:
            res = eval(self.label.text())
            self.label.setText(str(res / 100))
            self.btn_equate = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Сейчас это действие выполнить нельзя")
            error.setIcon(QMessageBox.Warning)

            error.setStandardButtons(QMessageBox.Reset | QMessageBox.Cancel | QMessageBox.Ok)

            error.setInformativeText("Два раза действие не выполнить")
            error.setDetailedText("Детали")

            error.buttonClicked.connect(self.popup_action)
            error.exec()


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Function_liney(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 472)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(161, 159, 162);\n"
                                  "color:rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 10, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget, clicked=lambda: self.draw_plot())
        self.pushButton.setGeometry(QtCore.QRect(20, 310, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(255, 173, 93)")
        self.pushButton.setObjectName("pushButton")
        self.label_y = QtWidgets.QLabel(self.widget)
        self.label_y.setGeometry(QtCore.QRect(20, 60, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_y.setFont(font)
        self.label_y.setObjectName("label_y")
        self.label_vvod = QtWidgets.QLineEdit(self.widget)
        self.label_vvod.setGeometry(QtCore.QRect(50, 50, 341, 41))
        self.label_vvod.setStyleSheet("background-color:rgb(20, 20, 20)")
        self.label_vvod.setText("")
        self.label_vvod.setObjectName("label_vvod")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(50, 110, 401, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Functions = QtWidgets.QAction(MainWindow)
        self.Functions.setObjectName("Functions")
        self.menu.addAction(self.Functions)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Решение функций"))
        self.label.setText(_translate("MainWindow", "Функция на графике"))
        self.pushButton.setText(_translate("MainWindow", "Ввести"))
        self.label_y.setText(_translate("MainWindow", "y = "))
        self.menu.setTitle(_translate("MainWindow", "О программе"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.Functions.setText(
            _translate("MainWindow", "MathCalcurator - программа, которая поможет нам решать математику"))
        self.sc = MplCanvas(self, width=5, height=2, dpi=70)
        self.sc.setParent(self.frame)

    def draw_plot(self):
        self.sc.axes.cla()
        x = np.linspace(-5, 5, 100)
        y = eval(self.label_vvod.text())
        self.sc.axes.plot(x, y)
        self.sc.draw()


class AlgLin(object):
    def setupUi(self, Form, alg):
        self.is_alg = alg
        Form.setObjectName("Form")
        Form.resize(237, 255)
        # Form.resize(237, 255)
        self.solve_example = QtWidgets.QPushButton(Form, clicked=lambda: self.solve_this())

        self.solve_example.setStyleSheet("background-color:rgb(255, 173, 93)")
        self.solve_example.setGeometry(QtCore.QRect(130, 200, 91, 40))
        self.solve_example.setObjectName("solve_example")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 100, 91, 21))
        self.label.setObjectName("label")
        self.example = QtWidgets.QTextEdit(Form)
        self.example.setGeometry(QtCore.QRect(20, 30, 201, 51))
        self.example.setObjectName("example")
        self.solved = QtWidgets.QTextEdit(Form)
        self.solved.setGeometry(QtCore.QRect(20, 120, 201, 51))
        self.solved.setObjectName("solved")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Решение задач по математике"))
        self.solve_example.setText(_translate("Form", "Решить"))
        self.label.setText(_translate("Form", "Решение:"))
        self.label_2.setText(_translate("Form", "Задача:"))

    def solve_this(self):
        txt = self.example.toPlainText()
        if self.is_alg:
            input_str = txt
            transformations = standard_transformations + (implicit_multiplication_application,)
            slv = expand(parse_expr(input_str, transformations=transformations))
            self.solved.setText(str(slv))
        else:
            if len(txt.split('=')) == 1:
                strToSolve = txt
            else:
                strToSolve = txt.split('=')
            slv = solve(strToSolve)
            self.solved.setText(str(slv))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())





