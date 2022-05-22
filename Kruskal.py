import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx
from PyQt5.QtWidgets import QMessageBox

class Ui_Kruskal(QWidget):
    def setupUi(self, nodesNumber, matrix, graphType):
        print(matrix)
        self.matrix = matrix
        self.graphType = graphType
        self.nodesNumber = nodesNumber
        self.ACM=0
        # MainWindow.setObjectName("MainWindow")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Kruskal')

        grid = QGridLayout()
        self.setLayout(grid)
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 0, 1, 9, 9)

        self.plot()
        self.show()
        self.showPath()

    def plot(self):
        global G

        mat = np.array(self.matrix)

        if self.graphType == "up":
            G = nx.from_numpy_array(mat, create_using=nx.Graph)

        mapping = {}
        for i in range(int(self.nodesNumber)):
            mapping[i] = chr(65 + i)

        nx.relabel_nodes(G, mapping, copy=False)

        # kruskal tree
        krus=nx.minimum_spanning_tree(G)
        # print("krus : "+str(krus.edges()))
        layout = nx.spring_layout(krus)
        nx.draw(krus, layout, with_labels=True)
        labels = nx.get_edge_attributes(krus, 'weight')

        # get a list of value (contain all weight krus)
        list_weight=list(labels.values())
        self.ACM = sum(list_weight)
        nx.draw_networkx_edge_labels(krus, pos=layout, edge_labels=labels)
       
    def showPath(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Arbre couvrant minimum (ACM)")
        msg.setInformativeText("ACM:  "+str(self.ACM))
        msg.setWindowTitle("ACM")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = Ui_Kruskal()
    sys.exit(app.exec_())
