from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def action(self):
        if self.rbDirected.isChecked():
            self.type = "d"
        if self.rbUndirected.isChecked():
            self.type = "u"

        self.nodesNumber = int(self.nodesNum.text())
        return self.type, self.nodesNumber

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")

        # ------------- Page One --------------------
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(120, 0, 591, 291))
        self.label.setStyleSheet("background-image: url(:/newPrefix/social-network.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(230, 340, 411, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.rbDirected = QtWidgets.QRadioButton(self.page)
        self.rbDirected.setGeometry(QtCore.QRect(270, 380, 121, 17))
        self.rbDirected.setFont(font)
        self.rbDirected.setObjectName("rbDirected")

        self.rbUndirected = QtWidgets.QRadioButton(self.page)
        self.rbUndirected.setGeometry(QtCore.QRect(450, 380, 141, 17))
        self.rbUndirected.setFont(font)
        self.rbUndirected.setObjectName("rbUndirected")

        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(230, 420, 211, 21))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.nodesNum = QtWidgets.QLineEdit(self.page)
        self.nodesNum.setGeometry(QtCore.QRect(520, 420, 113, 20))
        self.nodesNum.setObjectName("nodesNum")

        self.graphInfoBtn = QtWidgets.QPushButton(self.page)
        self.graphInfoBtn.setGeometry(QtCore.QRect(380, 480, 101, 31))
        self.graphInfoBtn.setObjectName("graphInfoBtn")

        # ------------- Page Two --------------------
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.graphMatrix = QtWidgets.QTableWidget(self.page_2)
        self.graphMatrix.setGeometry(QtCore.QRect(150, 90, 491, 351))
        self.graphMatrix.setAutoFillBackground(False)
        self.graphMatrix.setStyleSheet("font: 12pt \"Calibri\";")
        self.graphMatrix.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphMatrix.setTabKeyNavigation(True)
        self.graphMatrix.setAlternatingRowColors(False)
        self.graphMatrix.setShowGrid(True)
        self.graphMatrix.setGridStyle(QtCore.Qt.DashLine)
        self.graphMatrix.setWordWrap(True)
        self.graphMatrix.setCornerButtonEnabled(True)

        self.type, self.nodesNumber = self.action()
        self.graphMatrix.setRowCount(self.nodesNumber)
        self.graphMatrix.setColumnCount(self.nodesNumber)
        self.graphMatrix.setObjectName("graphMatrix")

        _translate = QtCore.QCoreApplication.translate

        for i in range(self.nodesNumber):
            item = QtWidgets.QTableWidgetItem()
            self.graphMatrix.setVerticalHeaderItem(i, item)
            item = self.graphMatrix.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", chr(65 + i)))

            item = QtWidgets.QTableWidgetItem()
            self.graphMatrix.setHorizontalHeaderItem(i, item)
            item = self.graphMatrix.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", chr(65 + i)))

            item = QtWidgets.QTableWidgetItem()
            self.graphMatrix.setItem(i, i, item)

            item = self.graphMatrix.item(i, i)
            item.setText(_translate("MainWindow", "0"))

        self.graphMatrix.horizontalHeader().setVisible(True)
        self.graphMatrix.horizontalHeader().setCascadingSectionResizes(True)
        self.graphMatrix.horizontalHeader().setDefaultSectionSize(50)
        self.graphMatrix.horizontalHeader().setMinimumSectionSize(23)
        self.graphMatrix.horizontalHeader().setSortIndicatorShown(False)
        self.graphMatrix.horizontalHeader().setStretchLastSection(False)

        self.graphMatrix.verticalHeader().setVisible(True)
        self.graphMatrix.verticalHeader().setDefaultSectionSize(30)
        self.graphMatrix.verticalHeader().setSortIndicatorShown(False)
        self.graphMatrix.verticalHeader().setStretchLastSection(False)

        self.makeGraphBtn = QtWidgets.QPushButton(self.page_2)
        self.makeGraphBtn.setGeometry(QtCore.QRect(340, 520, 101, 31))
        self.makeGraphBtn.setObjectName("makeGraphBtn")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Do you want to draw a Directed Graph or a Undirected Graph?"))
        self.rbDirected.setText(_translate("MainWindow", "Directed Graph"))
        self.rbUndirected.setText(_translate("MainWindow", "Undirected Graph"))
        self.label_4.setText(_translate("MainWindow", "What is the order of your graph?"))
        self.graphInfoBtn.setText(_translate("MainWindow", "OK"))
        self.graphMatrix.setSortingEnabled(True)
        __sortingEnabled = self.graphMatrix.isSortingEnabled()
        self.graphMatrix.setSortingEnabled(False)
        self.graphMatrix.setSortingEnabled(__sortingEnabled)
        self.makeGraphBtn.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
