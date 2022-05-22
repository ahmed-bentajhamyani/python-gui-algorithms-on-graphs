from PyQt5 import QtCore, QtWidgets
from Caracteristique import Ui_Charac

class Ui_Matrix(object):
    def openWindow(self, Ui_Window, matrix, nodesNumber, graphType):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window
        self.ui.setupUi(self.window, nodesNumber, matrix, graphType)
        self.window.show()

    def setupUi(self, MainWindow, nodesNumber, graphType):
        print(nodesNumber, graphType)
        self.nodesNumber = nodesNumber
        self.graphType = graphType

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 60, 441, 311))
        self.tableWidget.setStyleSheet("font: 12pt \"Calibri\";")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("background-color: rgb(240, 240, 240);")

        self.tableWidget.setColumnCount(nodesNumber)
        self.tableWidget.setRowCount(nodesNumber)

        for i in range(nodesNumber):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setVerticalHeaderItem(i, item)

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setHorizontalHeaderItem(i, item)

            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, i, item)
            for j in range(nodesNumber):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)

        self.makeGraphBtn = QtWidgets.QPushButton(self.centralwidget)
        self.makeGraphBtn.setGeometry(QtCore.QRect(354, 502, 131, 41))
        self.makeGraphBtn.setObjectName("makeGraphBtn")
        self.makeGraphBtn.setStyleSheet("background-color: rgb(234, 204, 80);")

        self.makeGraphBtn.clicked.connect(self.buildGraph)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Matrice"))

        self.makeGraphBtn.setText(_translate("MainWindow", "Ok"))

        for i in range(self.nodesNumber):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", chr(65 + i)))

            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", chr(65 + i)))

            item = self.tableWidget.item(i, i)
            item.setText(_translate("MainWindow", "0"))

    def buildGraph(self):
        matrix = []
        for i in range(self.nodesNumber):
            m = []
            for j in range(self.nodesNumber):
                m.append(int(self.tableWidget.item(i, j).text()))
            matrix.append(m)
        self.openWindow(Ui_Charac(), matrix, self.nodesNumber, self.graphType)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Matrix = QtWidgets.QMainWindow()
    ui = Ui_Matrix()
    ui.setupUi(Matrix)
    Matrix.show()
    sys.exit(app.exec_())
