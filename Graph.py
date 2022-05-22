import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx

class Ui_Graph(QWidget):
    def setupUi(self, nodesNumber, matrix, graphType):
        print(matrix)
        self.matrix = matrix
        self.graphType = graphType
        self.nodesNumber = nodesNumber

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Graph')

        grid = QGridLayout()
        self.setLayout(grid)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 0, 1, 9, 9)

        self.plot()
        self.show()

    def plot(self):
        global G

        mat = np.array(self.matrix)
        if self.graphType == "dn":
            G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
        if self.graphType == "un":
            G = nx.from_numpy_array(mat, create_using=nx.Graph)
        if self.graphType == "dp":
            G = nx.from_numpy_array(mat, create_using=nx.DiGraph)
        if self.graphType == "up":
            G = nx.from_numpy_array(mat, create_using=nx.Graph)

        mapping = {}
        for i in range(int(self.nodesNumber)):
            mapping[i] = chr(65 + i)

        nx.relabel_nodes(G, mapping, copy=False)

        if self.graphType == "dp" or self.graphType == "up":
            layout = nx.spring_layout(G)
            nx.draw(G, layout, with_labels=True)
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)

        if self.graphType == "dn" or self.graphType == "un":
            nx.draw(G, with_labels=True)
            self.canvas.draw_idle()

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = Ui_Graph()
    sys.exit(app.exec_())
