# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple-prettifier.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from cleaner.prettifier import json_prettifier, xml_prettier



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(637, 592)
        MainWindow.setFixedSize(637, 592)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(240, 490, 151, 41))
        self.pushButton1.setObjectName("pushButton1")
        self.editTextMain = QtWidgets.QTextEdit(self.centralwidget)
        self.editTextMain.setGeometry(QtCore.QRect(60, 90, 511, 371))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editTextMain.setFont(font)
        self.editTextMain.setObjectName("editTextMain")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButtonJSON = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonJSON.setGeometry(QtCore.QRect(70, 490, 95, 20))
        self.radioButtonJSON.setObjectName("radioButtonJSON")
        self.radioButtonXML = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonXML.setGeometry(QtCore.QRect(70, 520, 95, 20))
        self.radioButtonXML.setObjectName("radioButtonXML")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton1.clicked.connect(self.get_correct_prettier)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "Prettify"))
        self.label.setText(_translate("MainWindow", "Simple Prettifier"))
        self.radioButtonJSON.setText(_translate("MainWindow", "json"))
        self.radioButtonXML.setText(_translate("MainWindow", "xml"))

    def get_text(self):
        jsonText = json_prettifier(self.editTextMain.toPlainText())

        if(jsonText != None):
            self.editTextMain.setText(jsonText)


    def get_correct_prettier(self):
        text = None

        if(self.radioButtonJSON.isChecked()):
            text = json_prettifier(self.editTextMain.toPlainText())
        elif(self.radioButtonXML.isChecked()):
            text = xml_prettier(self.editTextMain.toPlainText())

        if (text != None):
            self.editTextMain.setText(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
