import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox


class Ui_Bellman(object):
    def setupUi(self, MainWindow, nodesNumber, matrix, graphType):
        self.nodesNumber = nodesNumber
        self.graphType = graphType
        self.matrix = matrix
        self.MainWindow = MainWindow
        self.source = ''
        self.absrbant = False


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 70, 601, 421))
        self.tableWidget.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(self.nodesNumber)
        self.tableWidget.setRowCount(3)

        # Statique
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)

        # Dynamique
        for i in range(self.nodesNumber):
            item = QtWidgets.QTableWidgetItem()
            item.setBackground(QtGui.QColor(240, 240, 240))
            self.tableWidget.setHorizontalHeaderItem(i, item)

        for i in range(self.nodesNumber):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(0, i, item)

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(1, i, item)

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(2, i, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)

        self.display()

        # Matrix to dict
        self.graph = {}
        for i in range(self.nodesNumber):
            edges = []
            for j in range(self.nodesNumber):
                if self.matrix[i][j] != 0:
                    edges.append((chr(65 + j), matrix[i][j]))
            self.graph[chr(65 + i)] = edges

        # Bellman-Ford
        self.distances = {}
        self.predecesseurs = {}
        for n in self.graph:
            self.distances[n] = np.inf
            self.predecesseurs[n] = None
        self.distances[self.source] = 0

        for i in range(len(self.graph) - 1):
            for n in self.graph:
                for j in range(len(self.graph[n])):
                    for m in self.graph[n][j][0]:
                        if self.distances[m] > (self.distances[n] + self.graph[n][j][1]):
                            self.distances[m] = (self.distances[n] + self.graph[n][j][1])
                            self.predecesseurs[m] = n
        print(self.graph)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bellman-Ford"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sommets"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Distance"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Predecesseur"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for n in self.graph:
            for j in range(len(self.graph[n])):
                for m in self.graph[n][j][0]:
                    if self.distances[m] > (self.distances[n] + self.graph[n][j][1]):
                        self.attention()
                    else:
                        for i in range(self.nodesNumber):
                            item = self.tableWidget.item(0, i)
                            item.setText(_translate("MainWindow", chr(65 + i)))

                        for i in range(self.nodesNumber):
                            item = self.tableWidget.item(1, i)
                            dist = self.distances[chr(65 + i)]
                            item.setText(_translate("MainWindow", str(dist)))

                        for i in range(self.nodesNumber):
                            item = self.tableWidget.item(2, i)
                            pred = self.predecesseurs[chr(65 + i)]
                            item.setText(_translate("MainWindow", str(pred)))


        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def display(self):
        src, pressed = QInputDialog.getText(self.MainWindow, "Sommet Depart", "Entrer un Sommet : ")
        if pressed:
            self.source = src

    def attention(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Parcours en Profondeur")
        msg.setInformativeText("Circuit Absorbant!")
        msg.setWindowTitle("Attention")
        msg.setStandardButtons(QMessageBox.Cancel)
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Bellman()
    MainWindow.show()
    sys.exit(app.exec_())
