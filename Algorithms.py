from PyQt5 import QtCore, QtGui, QtWidgets
from Bellman import Ui_Bellman
from Prim import Ui_Prim
from Warshall import Ui_Warshall
from Bfs import Ui_Bfs
from Dfs import Ui_Dfs
from Dij_test import Ui_Dijikstra
from Fulkerson import Ui_Fulkerson
from Kruskal import Ui_Kruskal


class Ui_Algorithms(object):
    def openWindow(self, Ui_Window):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window
        self.ui.setupUi(self.window, self.nodesNumber, self.matrix, self.graphType)
        self.window.show()

    def setupUi(self, MainWindow, nodesNumber, matrix, graphType):
        self.nodesNumber = nodesNumber
        self.graphType = graphType
        self.matrix = matrix

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)

        self.graphCaraFrame = QtWidgets.QFrame(self.centralwidget)
        self.graphCaraFrame.setGeometry(QtCore.QRect(80, 70, 651, 481))
        self.graphCaraFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphCaraFrame.setObjectName("graphCaraFrame")

        self.fulkersonBtn = QtWidgets.QPushButton(self.graphCaraFrame)
        self.fulkersonBtn.setGeometry(QtCore.QRect(340, 410, 111, 31))
        self.fulkersonBtn.setObjectName("fulkersonBtn")
        self.fulkersonBtn.setStyleSheet("background-color: rgb(234, 204, 80);")
        if self.graphType == "dn" or self.graphType == "un":
            self.fulkersonBtn.setEnabled(False)

        self.warshallBtn = QtWidgets.QPushButton(self.graphCaraFrame)
        self.warshallBtn.setGeometry(QtCore.QRect(490, 100, 91, 31))
        self.warshallBtn.setObjectName("warshallBtn")
        self.warshallBtn.setStyleSheet("background-color: rgb(234, 204, 80);")

        self.kruskalBtn = QtWidgets.QPushButton(self.graphCaraFrame)
        self.kruskalBtn.setGeometry(QtCore.QRect(420, 200, 91, 31))
        self.kruskalBtn.setObjectName("kruskalBtn")
        self.kruskalBtn.setStyleSheet("background-color: rgb(234, 204, 80);")
        if self.graphType == "dn" or self.graphType == "un" or self.graphType == "dp":
            self.kruskalBtn.setEnabled(False)

        self.dfsBtn = QtWidgets.QPushButton(self.graphCaraFrame)
        self.dfsBtn.setGeometry(QtCore.QRect(350, 100, 91, 31))
        self.dfsBtn.setObjectName("dfsBtn")
        self.dfsBtn.setStyleSheet("background-color: rgb(234, 204, 80);")

        self.dijkstraBtn = QtWidgets.QPushButton(self.graphCaraFrame)
        self.dijkstraBtn.setGeometry(QtCore.QRect(280, 320, 91, 31))
        self.dijkstraBtn.setObjectName("dijkstraBtn")
        self.dijkstraBtn.setStyleSheet("background-color: rgb(234, 204, 80);")
        if self.graphType == "dn" or self.graphType == "un":
            self.dijkstraBtn.setEnabled(False)
        for i in range(self.nodesNumber):
            for j in range(self.nodesNumber):
                if self.matrix[i][j] < 0:
                    self.dijkstraBtn.setEnabled(False)


        self.bellmanBtn = QtWidgets.QPushButton(self.graphCaraFrame)
        self.bellmanBtn.setGeometry(QtCore.QRect(420, 320, 91, 31))
        self.bellmanBtn.setObjectName("bellmanBtn")
        self.bellmanBtn.setStyleSheet("background-color: rgb(234, 204, 80);")
        if self.graphType == "dn" or self.graphType == "un":
            self.bellmanBtn.setEnabled(False)


        self.primBtn = QtWidgets.QPushButton(self.graphCaraFrame)
        self.primBtn.setGeometry(QtCore.QRect(280, 200, 91, 31))
        self.primBtn.setObjectName("primBtn")
        self.primBtn.setStyleSheet("background-color: rgb(234, 204, 80);")
        if self.graphType == "dn" or self.graphType == "un" or self.graphType == "dp":
            self.primBtn.setEnabled(False)

        self.bfsBtn = QtWidgets.QPushButton(self.graphCaraFrame)
        self.bfsBtn.setGeometry(QtCore.QRect(220, 100, 91, 31))
        self.bfsBtn.setObjectName("bfsBtn")
        self.bfsBtn.setStyleSheet("background-color: rgb(234, 204, 80);")

        self.label = QtWidgets.QLabel(self.graphCaraFrame)
        self.label.setGeometry(QtCore.QRect(30, 70, 161, 21))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(self.graphCaraFrame)
        self.label_4.setGeometry(QtCore.QRect(30, 380, 171, 21))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_3 = QtWidgets.QLabel(self.graphCaraFrame)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 161, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(self.graphCaraFrame)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 201, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_5.setObjectName("label_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.bfsBtn.clicked.connect(self.bfs)
        self.bellmanBtn.clicked.connect(self.bellman)
        self.primBtn.clicked.connect(self.prim)
        self.warshallBtn.clicked.connect(self.warshall)
        self.dfsBtn.clicked.connect(self.dfs)
        self.kruskalBtn.clicked.connect(self.kruskal)
        self.dijkstraBtn.clicked.connect(self.dijkstra)
        self.fulkersonBtn.clicked.connect(self.fulkerson)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algorithmes"))
        self.label_5.setText(_translate("MainWindow", " Liste des Algorithmes"))

        self.label.setText(_translate("MainWindow", "Parcours du graphe :"))
        self.bfsBtn.setText(_translate("MainWindow", "BFS"))
        self.dfsBtn.setText(_translate("MainWindow", "DFS"))
        self.warshallBtn.setText(_translate("MainWindow", "Warshall"))

        self.label_2.setText(_translate("MainWindow", "Arbre couvrant minimal :"))
        self.primBtn.setText(_translate("MainWindow", "Prim"))
        self.kruskalBtn.setText(_translate("MainWindow", "Kruskal"))

        self.label_3.setText(_translate("MainWindow", "Plus court chemin :"))
        self.dijkstraBtn.setText(_translate("MainWindow", "Dijkstra"))
        self.bellmanBtn.setText(_translate("MainWindow", "Bellman-Ford"))

        self.label_4.setText(_translate("MainWindow", "Minimiser le coùt :"))
        self.fulkersonBtn.setText(_translate("MainWindow", "Ford-Fulkerson"))

    def bfs(self):
        self.ui = Ui_Bfs()
        self.ui.setupUi(Ui_Bfs(), self.nodesNumber, self.matrix, self.graphType)

    def bellman(self):
        self.openWindow(Ui_Bellman())

    def prim(self):
        self.ui = Ui_Prim()
        self.ui.setupUi(Ui_Prim(), self.nodesNumber, self.matrix, self.graphType)

    def warshall(self):
        self.ui = Ui_Warshall()
        self.ui.setupUi(self.nodesNumber, self.matrix, self.graphType)

    def dfs(self):
        self.ui = Ui_Dfs()
        self.ui.setupUi(Ui_Dfs(), self.nodesNumber, self.matrix, self.graphType)

    def kruskal(self):
        self.ui = Ui_Kruskal()
        self.ui.setupUi(self.nodesNumber, self.matrix, self.graphType)

    def dijkstra(self):
        self.openWindow(Ui_Dijikstra())

    def fulkerson(self):
        self.openWindow(Ui_Fulkerson())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Algorithms()
    MainWindow.show()
    sys.exit(app.exec_())
