from PyQt5 import QtCore, QtGui, QtWidgets
from Matrix import Ui_Matrix

class Ui_WelcomePage(object):
    def openWindow(self, Ui_Window, nodesNumber, graphType):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window
        self.ui.setupUi(self.window, nodesNumber, graphType)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Welcome Page")
        MainWindow.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 480, 131, 21))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 340, 181, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.rbUP = QtWidgets.QRadioButton(self.centralwidget)
        self.rbUP.setGeometry(QtCore.QRect(470, 380, 171, 17))
        self.rbUP.setFont(font)
        self.rbUP.setObjectName("rbUP")

        self.rbUN = QtWidgets.QRadioButton(self.centralwidget)
        self.rbUN.setGeometry(QtCore.QRect(210, 380, 211, 17))
        self.rbUN.setFont(font)
        self.rbUN.setObjectName("rbUN")

        self.rbDN = QtWidgets.QRadioButton(self.centralwidget)
        self.rbDN.setGeometry(QtCore.QRect(210, 430, 181, 17))
        self.rbDN.setFont(font)
        self.rbDN.setObjectName("rbDN")

        self.rbDP = QtWidgets.QRadioButton(self.centralwidget)
        self.rbDP.setGeometry(QtCore.QRect(470, 430, 151, 17))
        self.rbDP.setFont(font)
        self.rbDP.setObjectName("rbDP")

        self.nodesNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.nodesNumber.setGeometry(QtCore.QRect(430, 480, 113, 20))
        self.nodesNumber.setObjectName("nodesNumber")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, -110, 1181, 421))
        self.label.setStyleSheet("background-image: url(images/networkx.webp);")
        self.label.setObjectName("label")

        self.graphInfoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.graphInfoBtn.setGeometry(QtCore.QRect(370, 540, 101, 31))
        self.graphInfoBtn.setObjectName("graphInfoBtn")
        self.graphInfoBtn.setStyleSheet("background-color: rgb(234, 204, 80);")

        self.graphInfoBtn.clicked.connect(self.openMatrix)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Accueil"))
        self.label_4.setText(_translate("MainWindow", "L\'ordre du graphe :"))
        self.label_2.setText(_translate("MainWindow", "Choisir le type de graphe ?"))
        self.graphInfoBtn.setText(_translate("MainWindow", "OK"))
        self.rbUP.setText(_translate("MainWindow", "Non orienté et pondéré"))
        self.rbUN.setText(_translate("MainWindow", "Non orienté et non pondéré"))
        self.rbDN.setText(_translate("MainWindow", "Orienté et non pondéré"))
        self.rbDP.setText(_translate("MainWindow", "Orienté et pondéré"))

    def openMatrix(self):
        global graphType
        nodesNumber = int(self.nodesNumber.text())
        if self.rbDP.isChecked():
            graphType = "dp"
        if self.rbDN.isChecked():
            graphType = "dn"
        if self.rbUP.isChecked():
            graphType = "up"
        if self.rbUN.isChecked():
            graphType = "un"

        self.openWindow(Ui_Matrix(), nodesNumber, graphType)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomePage = QtWidgets.QMainWindow()
    ui = Ui_WelcomePage()
    ui.setupUi(WelcomePage)
    WelcomePage.show()
    sys.exit(app.exec_())
