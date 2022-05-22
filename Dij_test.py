from PyQt5 import QtCore, QtGui, QtWidgets
import networkx as nx
import numpy as np
from PyQt5.QtWidgets import QInputDialog

class Ui_Dijikstra(object):


    def setupUi(self, Mainwindow_dij, nodesNumber, matrix, graphType):

        self.Mainwindow_dij = Mainwindow_dij
        self.nodesNumber = nodesNumber
        self.matrix = matrix
        self.node ='A'
        self.graphType = graphType
        self.nodes = {}
        print("matrix :  "+str(self.matrix))
        self.graph = {}
        Mainwindow_dij.setObjectName("Mainwindow_dij")
        Mainwindow_dij.resize(653, 396)

        self.display()

        self.tableWidget = QtWidgets.QTableWidget(Mainwindow_dij)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 621, 101))
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(nodesNumber)
        self.tableWidget.setRowCount(2)

        for i in range(nodesNumber):
            
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



        # L
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        # P 
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)

       
        

        self.label = QtWidgets.QLabel(Mainwindow_dij)
        self.label.setGeometry(QtCore.QRect(150, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_somet_depart = QtWidgets.QLabel(Mainwindow_dij)
        self.label_somet_depart.setGeometry(QtCore.QRect(40, 70, 131, 16))
        self.label_somet_depart.setObjectName("label_somet_depart")
        self.sommet_dpart_valu = QtWidgets.QLabel(Mainwindow_dij)
        self.sommet_dpart_valu.setGeometry(QtCore.QRect(190, 70, 47, 14))
        self.sommet_dpart_valu.setText(str(self.node))
        self.sommet_dpart_valu.setObjectName("sommet_dpart_valu")

        self.Resultats = QtWidgets.QLabel(Mainwindow_dij)
        self.Resultats.setGeometry(QtCore.QRect(40, 100, 47, 14))
        self.Resultats.setObjectName("Resultats")




        

        self.label_2 = QtWidgets.QLabel(Mainwindow_dij)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 141, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Mainwindow_dij)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow_dij)

        
        # ###############

        # liste des nodes
        
        for i in range(self.nodesNumber):
            self.nodes[i] = chr(ord('A') + i)
        print("nodes :  "+str(self.nodes))
        mat = np.array(self.matrix)
        if self.graphType =="up" :
             G = nx.from_numpy_array(mat, create_using=nx.Graph)
        if self.graphType =="dp" :
             G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
        nx.relabel_nodes(G, self.nodes, copy=False)

        # labels est un dicionnaire cntient l'arret et son wieght
        labels = nx.get_edge_attributes(G, 'weight')
        print("labels:  "+str(labels))

        # liste des areets
        edges = list()

        for i in range(self.nodesNumber):
            for j in range(self.nodesNumber):
                if matrix[i][j] != 0 and ((self.nodes[j], self.nodes[i]) not in edges):
                    edges.append((self.nodes[j], self.nodes[i]))

        print("listes des edges :  "+str(edges))

        # transformer ces resulat en un graph facile a manipuler

        for i in self.nodes.values():
            tmp = {}
            for j in self.nodes.values():
                if ((i, j) in edges) or ((j, i) in edges):
                    if ((i, j)) in labels.keys():
                        tmp[j] = labels[(i, j)]  # get le cout
                    else:
                        tmp[j] = labels[(j, i)]  # get le cout
            self.graph[i] = tmp

        print("graph est  :  "+str(self.graph))

          # - - - - -  - - - - matrice- - - - - - - -- - -
        self.distance, self.precedent = self.dijkstra(self.graph,self.node)
        print('Distances minimum :', self.distance)
        print('Liste des précédents :', self.precedent)
        # remplissage des donnees :  tes
          # 1 - les distance
        j = 0
        for i in self.nodes.values() :
             self.tableWidget.setItem(0, j, QtWidgets.QTableWidgetItem(str(self.distance[i])))
             j+=1
         # 2- les predecessors
        k = 0
        for i in self.nodes.values() :
             self.tableWidget.setItem(1, k, QtWidgets.QTableWidgetItem(self.precedent[i]))
             k+=1
        # algorithme de dijekstra

    def dijkstra(self, village, source):
        assert all(village[u][v] >= 0 for u in village.keys() for v in village[u].keys())
        precedent = {x: 'None' for x in village.keys()}
        dejaTraite = {x: False for x in village.keys()}
        distance = {x: float('inf') for x in village.keys()}
        distance[source] = 0
        a_traiter = [(0, source)]
        while a_traiter:
            dist_noeud, noeud = a_traiter.pop()
            if not dejaTraite[noeud]:
                dejaTraite[noeud] = True
                for voisin in village[noeud].keys():
                    dist_voisin = dist_noeud + village[noeud][voisin]
                    if dist_voisin < distance[voisin]:
                        distance[voisin] = dist_voisin
                        precedent[voisin] = noeud
                        a_traiter.append((dist_voisin, voisin))
            a_traiter.sort(reverse=True)
        return distance, precedent


    def display(self):
        nd , pressed = QInputDialog.getText(self.Mainwindow_dij, "Input Text", "Entrer un Sommet : ")
        if pressed:
            print(str(nd))
            self.node=nd
    

    def retranslateUi(self, Mainwindow_dij):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow_dij.setWindowTitle(_translate("Mainwindow_dij", "Form"))
        # L P
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Mainwindow_dij", "L"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Mainwindow_dij", "P"))


        for i in range(self.nodesNumber):
                item = self.tableWidget.horizontalHeaderItem(i)
                item.setText(_translate("MainWindow", chr(65 + i)))
            

        self.label.setText(_translate("Mainwindow_dij", "Algorithme de Dijkstra"))
        self.label_somet_depart.setText(_translate("Mainwindow_dij", "Sommet de depart  :"))
        self.Resultats.setText(_translate("Mainwindow_dij", "Resultats"))

        Mainwindow_dij.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow_dij = QtWidgets.QWidget()
    ui = Ui_Mainwindow_dij()
    ui.setupUi(Mainwindow_dij)
    Mainwindow_dij.show()
    sys.exit(app.exec_())
