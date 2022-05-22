from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from Graph import Ui_Graph
from Algorithms import Ui_Algorithms
import networkx as nx

class Ui_Charac(object):
    def openWindow(self, Ui_Window):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window
        self.ui.setupUi(self.window, self.nodesNumber, self.matrix, self.graphType)
        self.window.show()

    def setupUi(self, MainWindow, nodesNumber, matrix, graphType):
        self.nodesNumber = nodesNumber
        self.graphType = graphType
        self.matrix = matrix
        self.num_edges = 0
        self.list_degrees = list()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(240, 240, 240);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphCaraFrame = QtWidgets.QFrame(self.centralwidget)
        self.graphCaraFrame.setGeometry(QtCore.QRect(120, 110, 591, 361))
        self.graphCaraFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphCaraFrame.setObjectName("graphCaraFrame")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        self.Label_4 = QtWidgets.QLabel(self.graphCaraFrame)
        self.Label_4.setGeometry(QtCore.QRect(40, 190, 71, 16))
        self.Label_4.setFont(font)
        self.Label_4.setObjectName("Label_4")

        self.Label_3 = QtWidgets.QLabel(self.graphCaraFrame)
        self.Label_3.setGeometry(QtCore.QRect(40, 150, 121, 21))
        self.Label_3.setFont(font)
        self.Label_3.setObjectName("Label_3")

        self.Label_2 = QtWidgets.QLabel(self.graphCaraFrame)
        self.Label_2.setGeometry(QtCore.QRect(40, 110, 161, 16))
        self.Label_2.setFont(font)
        self.Label_2.setObjectName("Label_2")

        self.Label = QtWidgets.QLabel(self.graphCaraFrame)
        self.Label.setGeometry(QtCore.QRect(40, 30, 121, 21))
        self.Label.setFont(font)
        self.Label.setObjectName("Label")

        self.Label_5 = QtWidgets.QLabel(self.graphCaraFrame)
        self.Label_5.setGeometry(QtCore.QRect(40, 230, 141, 16))
        self.Label_5.setFont(font)
        self.Label_5.setObjectName("Label_5")

        self.Label_6 = QtWidgets.QLabel(self.graphCaraFrame)
        self.Label_6.setGeometry(QtCore.QRect(40, 270, 121, 21))
        self.Label_6.setFont(font)
        self.Label_6.setObjectName("Label_6")

        self.Label_8 = QtWidgets.QLabel(self.graphCaraFrame)
        self.Label_8.setGeometry(QtCore.QRect(40, 310, 121, 21))
        self.Label_8.setFont(font)
        self.Label_8.setObjectName("Label_8")

        self.Label_9 = QtWidgets.QLabel(self.graphCaraFrame)
        self.Label_9.setGeometry(QtCore.QRect(40, 70, 81, 21))
        self.Label_9.setFont(font)
        self.Label_9.setObjectName("Label_9")

        self.Type = QtWidgets.QLabel(self.graphCaraFrame)
        self.Type.setGeometry(QtCore.QRect(270, 30, 121, 21))
        self.Type.setFont(font)
        self.Type.setText("")
        self.Type.setObjectName("Type")

        self.listeSommet = QtWidgets.QLabel(self.graphCaraFrame)
        self.listeSommet.setGeometry(QtCore.QRect(270, 230, 141, 16))
        self.listeSommet.setFont(font)
        self.listeSommet.setText("")
        self.listeSommet.setObjectName("listeSommet")

        self.pondere = QtWidgets.QLabel(self.graphCaraFrame)
        self.pondere.setGeometry(QtCore.QRect(270, 70, 81, 21))
        self.pondere.setFont(font)
        self.pondere.setText("")
        self.pondere.setObjectName("pondere")

        self.tailleGraph = QtWidgets.QLabel(self.graphCaraFrame)
        self.tailleGraph.setGeometry(QtCore.QRect(270, 150, 121, 21))
        self.tailleGraph.setFont(font)
        self.tailleGraph.setText("")
        self.tailleGraph.setObjectName("tailleGraph")

        self.graphRegulier = QtWidgets.QLabel(self.graphCaraFrame)
        self.graphRegulier.setGeometry(QtCore.QRect(270, 310, 121, 21))
        self.graphRegulier.setFont(font)
        self.graphRegulier.setText("")
        self.graphRegulier.setObjectName("graphRegulier")

        self.Densite = QtWidgets.QLabel(self.graphCaraFrame)
        self.Densite.setGeometry(QtCore.QRect(270, 190, 71, 16))
        self.Densite.setFont(font)
        self.Densite.setText("")
        self.Densite.setObjectName("Densite")

        self.nbrSommet = QtWidgets.QLabel(self.graphCaraFrame)
        self.nbrSommet.setGeometry(QtCore.QRect(270, 110, 161, 16))
        self.nbrSommet.setFont(font)
        self.nbrSommet.setText("")
        self.nbrSommet.setObjectName("nbrSommet")

        self.graphComplet = QtWidgets.QLabel(self.graphCaraFrame)
        self.graphComplet.setGeometry(QtCore.QRect(270, 270, 121, 21))
        self.graphComplet.setFont(font)
        self.graphComplet.setText("")
        self.graphComplet.setObjectName("graphComplet")

        self.showGraphBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showGraphBtn.setGeometry(QtCore.QRect(270, 530, 111, 31))
        self.showGraphBtn.setFont(font)
        self.showGraphBtn.setStyleSheet("background-color: rgb(234, 204, 80);")
        self.showGraphBtn.setObjectName("showGraphBtn")

        self.algorithms = QtWidgets.QPushButton(self.centralwidget)
        self.algorithms.setGeometry(QtCore.QRect(410, 530, 111, 31))
        self.algorithms.setFont(font)
        self.algorithms.setStyleSheet("background-color: rgb(234, 204, 80);")
        self.algorithms.setObjectName("showGraphBtn_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.showGraphBtn.clicked.connect(self.showGraph)
        self.algorithms.clicked.connect(self.algorithmsPage)

        # type de graphe------
        if self.graphType == 'dn' or self.Type == 'dp':
            self.Type.setText("Orienté")
        else:
            self.Type.setText("Non Orienté")

        # les sommets-------------
        self.nbrSommet.setText(str(self.nodesNumber))

        # Taille----------------------
        mat = np.array(self.matrix)
        if self.graphType == "dp":
            G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
            self.tailleGraph.setText(str(G.number_of_edges()))
            self.num_edges=G.number_of_edges()
            print("number of  edges  :  "+str(self.num_edges))
            print("number of  nodes  :  "+str(self.nodesNumber))
            self.list_degrees=list(G.degree())
            print("list de degre d est :  "+str(self.list_degrees))
        if self.graphType == "dn":
            G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
            self.tailleGraph.setText(str(G.number_of_edges()))
            self.num_edges = G.number_of_edges()
            self.list_degrees = list(G.degree())
            print("list de degre d est :  " + str(self.list_degrees))
            print("number of  edges  :  "+str(self.num_edges))
            print("number of  nodes  :  "+str(self.nodesNumber))
        if self.graphType == "up":
            G = nx.from_numpy_array(mat, create_using=nx.Graph)
            self.tailleGraph.setText(str(G.number_of_edges()))
            self.num_edges = G.number_of_edges()
            self.list_degrees = list(G.degree())
            print("list de degre d est :  " + str(self.list_degrees))
            print("number of  edges  :  "+str(self.num_edges))
            print("number of  nodes  :  "+str(self.nodesNumber))
        if self.graphType == "un":
            G = nx.from_numpy_array(mat, create_using=nx.Graph)
            self.tailleGraph.setText(str(G.number_of_edges()))
            self.num_edges=G.number_of_edges()
            self.list_degrees=list(G.degree())
            print("list de degre u est :  "+str(self.list_degrees))
            print("number of  edges  :  "+str(self.num_edges))
            print("number of  nodes  :  "+str(self.nodesNumber))

        # liste des nodes
        nodes = {}
        for i in range(self.nodesNumber):
            nodes[i] = chr(ord('A') + i)
        ch = ""
        for i in range(len(nodes)):
            ch += nodes[i]
            if i != len(nodes) - 1:
                ch += ", "
        self.listeSommet.setText(str(ch))

        #graphe complet ? 
        if self.num_edges == (self.nodesNumber *(self.nodesNumber - 1)/2) :
            self.graphComplet.setText(" Oui ")
        else :
            self.graphComplet.setText(" Non ")

        #graph regulier
        flag=0
        for i in range(len(self.list_degrees)):
             for j in range(len(self.list_degrees)) :
                 if self.list_degrees[i][1] != self.list_degrees[j][1]:
                     flag=1
                     break
        if flag == 0:
            self.graphRegulier.setText(" Oui ")
        else : 
            self.graphRegulier.setText(" Non ")

        # Densite
        if self.graphType == "up" or self.graphType == "un":
            self.Densite.setText(
                str(format(((2 * self.num_edges) / ((self.nodesNumber - 1) * self.nodesNumber)), ".2f")))

        # pondere ? 
        if self.graphType == "dp" or self.graphType == "up":
            self.pondere.setText("Oui ")
        else :
            self.pondere.setText("Non ")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caractéristiques"))
        self.Label_4.setText(_translate("MainWindow", "Densité :"))
        self.Label_3.setText(_translate("MainWindow", "Taille du graphe :"))
        self.Label_2.setText(_translate("MainWindow", "Nombre des sommets :"))
        self.Label.setText(_translate("MainWindow", "Type de graphe :"))
        self.Label_5.setText(_translate("MainWindow", "Liste des sommets :"))
        self.Label_6.setText(_translate("MainWindow", "Graphe Complet ?"))
        self.Label_8.setText(_translate("MainWindow", "Graphe Régulier ?"))
        self.Label_9.setText(_translate("MainWindow", "Pondéré ?"))
        self.showGraphBtn.setText(_translate("MainWindow", "Graphe"))
        self.label.setText(_translate("MainWindow", "  Caractéristique du graphe"))
        self.algorithms.setText(_translate("MainWindow", "Algorithmes"))

    def showGraph(self):
        self.ui = Ui_Graph()
        self.ui.setupUi(self.nodesNumber, self.matrix, self.graphType)

    def algorithmsPage(self):
        self.openWindow(Ui_Algorithms())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Charac()
    MainWindow.show()
    sys.exit(app.exec_())
