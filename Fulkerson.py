from PyQt5 import QtCore, QtGui, QtWidgets
import networkx as nx
import numpy as np
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QMessageBox


class Ui_Fulkerson(object):

    def setupUi(self, Mainwindow_dij, nodesNumber, matrix, graphType):
  
        self.Mainwindow_dij = Mainwindow_dij
        self.nodesNumber = nodesNumber
        self.matrix = matrix
        self.graphType = graphType
        self.nodes = {}
        self.flux=0
        self.edges = list()
        print("matrix :  "+str(self.matrix))
        self.graph = {}
        Mainwindow_dij.setObjectName("Mainwindow_dij")
        Mainwindow_dij.resize(653, 396)

        self.display()

        self.label = QtWidgets.QLabel(Mainwindow_dij)
        self.label.setGeometry(QtCore.QRect(150, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_somet_depart = QtWidgets.QLabel(Mainwindow_dij)
        self.label_somet_depart.setGeometry(QtCore.QRect(40, 70, 231, 16))
        self.label_somet_depart.setObjectName("label_somet_depart")

        self.sommet_dpart_valu = QtWidgets.QLabel(Mainwindow_dij)
        self.sommet_dpart_valu.setGeometry(QtCore.QRect(190, 70, 107, 14))
        self.sommet_dpart_valu.setObjectName("sommet_dpart_valu")

        self.label_somet_puit = QtWidgets.QLabel(Mainwindow_dij)
        self.label_somet_puit.setGeometry(QtCore.QRect(40, 110, 231, 16))
        self.label_somet_puit.setObjectName("label_somet_puit")

        self.label_somet_puit_value = QtWidgets.QLabel(Mainwindow_dij)
        self.label_somet_puit_value.setGeometry(QtCore.QRect(190, 110, 131, 16))
        self.label_somet_puit_value.setObjectName("label_somet_puit_value")

        self.Resultats = QtWidgets.QLabel(Mainwindow_dij)
        self.Resultats.setGeometry(QtCore.QRect(40, 150, 107, 14))
        self.Resultats.setObjectName("Resultats")

        self.Resultats_value = QtWidgets.QLabel(Mainwindow_dij)
        self.Resultats_value.setGeometry(QtCore.QRect(190, 150, 107, 14))
        self.Resultats_value.setObjectName("Resultats_value")       

        self.label_2 = QtWidgets.QLabel(Mainwindow_dij)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 141, 20))
        self.label_2.setObjectName("label_2")
        
        QtCore.QMetaObject.connectSlotsByName(Mainwindow_dij)

        # liste des nodes
        
        for i in range(self.nodesNumber):
            self.nodes[i] = chr(ord('A') + i)
        print("nodes :  "+str(self.nodes))
        mat = np.array(self.matrix)
        if self.graphType in ("up", "dn", "un"):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error le graphe doit etre  oriente !")
            msg.setWindowTitle("Error")
            msg.exec_()

        G = nx.from_numpy_array(mat, create_using=nx.Graph)
        nx.relabel_nodes(G, self.nodes, copy=False)

        # labels est un dicionnaire cntient l'arret et son wieght
        self.labels = nx.get_edge_attributes(G, 'weight')
        print("labels:  "+str(self.labels))

        # liste des areets

        for i in range(self.nodesNumber):
            for j in range(self.nodesNumber):
                if matrix[i][j] != 0:
                    self.edges.append((self.nodes[j], self.nodes[i]))

        # transformer ces resulat en un graph facile a manipuler

        for i in self.nodes.values():
            tmp = {}
            for j in self.nodes.values():
                if ((i, j) in self.edges) or ((j, i) in self.edges):
                    if ((i, j)) in self.labels.keys():
                        tmp[j] = self.labels[(i, j)]  # get le cout
                    else:
                        tmp[j] = self.labels[(j, i)]  # get le cout
            self.graph[i] = tmp

        # create a list of weight
        self.weight=list()
        for l in self.labels.values():
                self.weight.append(l)
        print(self.weight)
        # nouveau graph
        G1 = nx.DiGraph()
        i=0
        for ed in self.edges:
            G1.add_edge(ed[1],ed[0],capacity=float(self.weight[i])) 
            i+=1            
        print("G1 edges  : "+str(G1.edges()))
       
        
        flow_value, flow_dict = nx.maximum_flow(G1, self.smt, self.pt)
        self.flux=flow_value

        self.retranslateUi(Mainwindow_dij)
    def display(self):
        smt , pressed = QInputDialog.getText(self.Mainwindow_dij, "Input Text", "Depart: ")
        if pressed:
            print(str(smt))
            self.smt=smt
            pt , pressed = QInputDialog.getText(self.Mainwindow_dij, "Input Text", "Arrive: ")
            if pressed:
                    print(str(pt))
                    self.pt=pt

    def retranslateUi(self, Mainwindow_dij):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow_dij.setWindowTitle(_translate("Mainwindow_dij", "Ford-Fulkerson"))
        self.label.setText(_translate("Mainwindow_dij", "Algorithme de ford fulkerson"))
        self.label_somet_depart.setText(_translate("Mainwindow_dij", "Sommet de depart  :"))
        self.label_somet_puit.setText(_translate("Mainwindow_dij", "Sommet  d'arrivée  :"))
        self.Resultats.setText(_translate("Mainwindow_dij", "flux Max : "))

        self.sommet_dpart_valu.setText(_translate("Mainwindow_",str(self.smt)))
        self.label_somet_puit_value.setText(_translate("Mainwindow_",str(self.pt)))
        self.Resultats_value.setText(_translate("Mainwindow_",str(self.flux)))
        
        Mainwindow_dij.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow_dij = QtWidgets.QWidget()
    ui = Ui_Fulkerson()
    ui.setupUi(Mainwindow_dij)
    Mainwindow_dij.show()
    sys.exit(app.exec_())
