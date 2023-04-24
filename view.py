# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GradeCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(450, 550)
        mainWindow.setMinimumSize(QtCore.QSize(450, 550))
        mainWindow.setMaximumSize(QtCore.QSize(450, 550))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.student_number_input = QtWidgets.QLineEdit(self.centralwidget)
        self.student_number_input.setGeometry(QtCore.QRect(230, 100, 171, 31))
        self.student_number_input.setObjectName("student_number_input")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(96, 22, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.student_number_label = QtWidgets.QLabel(self.centralwidget)
        self.student_number_label.setGeometry(QtCore.QRect(40, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.student_number_label.setFont(font)
        self.student_number_label.setAlignment(QtCore.Qt.AlignCenter)
        self.student_number_label.setObjectName("student_number_label")
        self.student_score_input = QtWidgets.QLineEdit(self.centralwidget)
        self.student_score_input.setGeometry(QtCore.QRect(232, 169, 171, 31))
        self.student_score_input.setObjectName("student_score_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(46, 169, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.score_enter_button = QtWidgets.QPushButton(self.centralwidget)
        self.score_enter_button.setGeometry(QtCore.QRect(100, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.score_enter_button.setFont(font)
        self.score_enter_button.setObjectName("score_enter_button")
        self.score_clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.score_clear_button.setGeometry(QtCore.QRect(230, 220, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.score_clear_button.setFont(font)
        self.score_clear_button.setObjectName("score_clear_button")
        self.score_table = QtWidgets.QTableView(self.centralwidget)
        self.score_table.setGeometry(QtCore.QRect(40, 260, 361, 181))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.score_table.setFont(font)
        self.score_table.setObjectName("score_table")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 450, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Grade Calculator"))
        self.title_label.setText(_translate("mainWindow", "Grade Calculator"))
        self.student_number_label.setText(_translate("mainWindow", "Number of Students"))
        self.label.setText(_translate("mainWindow", "Student Scores"))
        self.score_enter_button.setText(_translate("mainWindow", "Enter Score"))
        self.score_clear_button.setText(_translate("mainWindow", "Clear Scores"))
        self.pushButton.setText(_translate("mainWindow", "Calculate Grades"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())