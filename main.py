import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_equate.setText(_translate("MainWindow", "="))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_add_sub.setText(_translate("MainWindow", "+/-"))
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
        # self.btn_add_sub.clicked.connect(lambda: self.write_number(self.btn_add_sub.text()))
        self.btn_point.clicked.connect(lambda: self.write_number(self.btn_point.text()))
        self.btn_div.clicked.connect(lambda: self.write_number(self.btn_div.text()))
        self.btn_equate.clicked.connect(self.results)
        self.btn_c.clicked.connect(self.clear)
        self.btn_add_sub.clicked.connect(self.function_btn_add_sub)


    def write_number(self, number):
        if self.label.text() == "0" or self.btn_equate:
            self.label.setText(number)
            self.btn_equate = False
        else:
            self.label.setText(self.label.text() + number)


    def results(self):
        if not self.btn_equate:
            res = eval(self.label.text())
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


    def popup_action(self, btn):
        if btn.text() == "Ok":
            print("Print ok")
        elif btn.text() == "Resert":
            self.label.setText("")
            self.btn_equate = False


    def clear(self):
        self.label.setText("0")


    def function_btn_add_sub(self, number):
        self.label.setText(-number)


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())
