from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx

class Ui_Warshall(QWidget):
    def setupUi(self, nodesNumber, matrix, graphType):
        self.graphType = graphType
        self.nodesNumber = nodesNumber

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Warshall')

        grid = QGridLayout()
        self.setLayout(grid)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 0, 1, 9, 9)

        # Convert to dict
        graph = {}
        for i in range(self.nodesNumber):
            edges = []
            for j in range(self.nodesNumber):
                if matrix[i][j] != 0:
                    edges.append(chr(65 + j))
            graph[chr(65 + i)] = edges

        # Warshall
        new_graph = graph
        pre = 0
        suc = 0
        for n in graph:
            suc = graph[n]
            for m in graph:
                if n in graph[m]:
                    pre = m
                    for s in suc:
                        if s not in graph[pre]:
                            new_graph[pre].append(s)

        # Convert to array
        self.graph = []
        for n in new_graph:
            node = new_graph[n]
            for nodeList in node:
                edge = (n, nodeList[0])
                self.graph.append(edge)

        self.plot()
        self.show()

    def plot(self):
        global G

        if self.graphType == "dp" or self.graphType == "dn":
            G = nx.DiGraph()
        if self.graphType == "up" or self.graphType == "un":
            G = nx.Graph()

        mapping = {}
        for i in range(int(self.nodesNumber)):
            mapping[i] = chr(65 + i)
        nx.relabel_nodes(G, mapping, copy=False)

        G.add_edges_from(self.graph)
        nx.draw(G, with_labels=True)
        self.canvas.draw_idle()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = Ui_Warshall()
    sys.exit(app.exec_())
