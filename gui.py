# Form implementation generated from reading ui file 'voting.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 300)
        MainWindow.setMinimumSize(QtCore.QSize(200, 300))
        MainWindow.setMaximumSize(QtCore.QSize(200, 300))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id = QtWidgets.QLabel(parent=self.centralwidget)
        self.id.setGeometry(QtCore.QRect(30, 44, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.input_id = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_id.setGeometry(QtCore.QRect(56, 60, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(11)
        self.input_id.setFont(font)
        self.input_id.setObjectName("input_id")
        self.candidate1 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.candidate1.setGeometry(QtCore.QRect(70, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.candidate1.setFont(font)
        self.candidate1.setObjectName("candidate1")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.candidate1)
        self.candidate2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.candidate2.setGeometry(QtCore.QRect(70, 155, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(13)
        self.candidate2.setFont(font)
        self.candidate2.setObjectName("candidate2")
        self.buttonGroup.addButton(self.candidate2)
        self.candidates = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidates.setGeometry(QtCore.QRect(50, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(15)
        self.candidates.setFont(font)
        self.candidates.setObjectName("candidates")
        self.submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(30, 180, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(38, 120, 118, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(50, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.error = QtWidgets.QLabel(parent=self.centralwidget)
        self.error.setGeometry(QtCore.QRect(20, 220, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        self.error.setFont(font)
        self.error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error.setWordWrap(True)
        self.error.setObjectName("error")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.id.setText(_translate("MainWindow", "ID"))
        self.input_id.setPlaceholderText(_translate("MainWindow", "8-digit ID"))
        self.candidate1.setText(_translate("MainWindow", "Jane"))
        self.candidate2.setText(_translate("MainWindow", "John"))
        self.candidates.setText(_translate("MainWindow", "CANDIDATES"))
        self.submit.setText(_translate("MainWindow", "SUBMIT VOTE"))
        self.title.setText(_translate("MainWindow", "VOTE!"))
        self.error.setText(_translate("MainWindow", "Error: ID must be 8 digits"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
