from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx

class Ui_Prim(QWidget):
    def setupUi(self, MainWindow, nodesNumber, matrix, graphType):
        self.graphType = graphType
        self.nodesNumber = nodesNumber
        self.MainWindow = MainWindow
        self.source = ''

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Prim')

        grid = QGridLayout()
        self.setLayout(grid)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 0, 1, 9, 9)

        self.display()

        sommetDepart = ord(self.source) - 65

        INF = 100000
        selected_node = [0, 0, 0, 0, 0, 0]
        no_edge = 0
        selected_node[sommetDepart] = True
        new_graph = {}

        # printing for edge and weight
        while (no_edge < self.nodesNumber - 1):
            edges = []
            minimum = INF
            a = 0
            b = 0
            for m in range(self.nodesNumber):
                if selected_node[m]:
                    for n in range(self.nodesNumber):
                        if ((not selected_node[n]) and matrix[m][n]):
                            # not in selected and there is an edge
                            if minimum > matrix[m][n]:
                                minimum = matrix[m][n]
                                a = m
                                b = n
            if chr(65 + a) in new_graph:
                edges = new_graph[chr(65 + a)]

            edges.append((chr(65 + b), matrix[a][b]))
            new_graph[chr(65 + a)] = edges

            selected_node[b] = True
            no_edge += 1

        # Convert to array
        self.graph = []
        for n in new_graph:
            node = new_graph[n]
            for l in node:
                edge = (n, l[0], l[1])
                self.graph.append(edge)

        self.plot()
        self.show()

    def plot(self):
        global G

        if self.graphType == "dp":
            G = nx.DiGraph()
        if self.graphType == "up":
            G = nx.Graph()

        mapping = {}
        for i in range(int(self.nodesNumber)):
            mapping[i] = chr(65 + i)
        nx.relabel_nodes(G, mapping, copy=False)

        G.add_weighted_edges_from(self.graph)
        layout = nx.spring_layout(G)
        nx.draw(G, layout, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)

    def display(self):
        src, pressed = QInputDialog.getText(self.MainWindow, "Sommet Depart", "Entrer un Sommet : ")
        if pressed:
            self.source = src

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = Ui_Prim()
    sys.exit(app.exec_())
