import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from gui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        self.ui.graphInfoBtn.clicked.connect(self.showPage2)
        self.ui.makeGraphBtn.clicked.connect(self.showPage)

    def showPage2(self):
        self.ui.action()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def showPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)


    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

