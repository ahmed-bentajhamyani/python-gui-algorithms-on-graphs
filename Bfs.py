import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx


class Ui_Bfs(QWidget):
    def setupUi(self, MainWindow, nodesNumber, matrix, graphType):
        print(matrix)
        self.matrix = matrix
        self.graphType = graphType
        self.nodesNumber = nodesNumber
        self.details = " "
        self.source = "A"
        self.MainWindow = MainWindow
        self.setWindowTitle('Bfs')

        # recuperer le sommet
        self.display()
        # afficher le chemain

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Bfs')

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

        G = nx.from_numpy_array(mat, create_using=nx.DiGraph)

        mapping = {}
        for i in range(int(self.nodesNumber)):
            mapping[i] = chr(65 + i)

        nx.relabel_nodes(G, mapping, copy=False)

        # affichage d'arbre BFS si le graphe est direct
        tree = nx.bfs_tree(G, source=self.source)
        print(tree.edges())

        # create table of nodes BFS
        self.tab = []
        flag = 0
        for edg in tree.edges():
            if (flag == 0):
                self.tab.append(edg[0])
            flag = 1
            self.tab.append(edg[1])

        nx.relabel_nodes(tree, mapping, copy=False)

        nx.draw(tree, with_labels=True)

    def display(self):
        src, pressed = QInputDialog.getText(self.MainWindow, "Sommet Depart", "Entrer un Sommet : ")
        if pressed:
            print(str(src))
            self.source = src

    def showPath(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Parcours en Profondeur")
        msg.setInformativeText("Bfs:  " + str(self.tab))
        msg.setWindowTitle("Bfs")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = Ui_Bfs()
    sys.exit(app.exec_())
