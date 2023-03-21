import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from UI_ImageEditor import Ui_MainWindow

class MainWindow(object):
    def __init__(self) -> None:
        self.main_win = QMainWindow()
        self.Ui =  Ui_MainWindow()
        self.Ui.setupUi(self.main_win)

        self.Ui.stackedWidget.setCurrentWidget(self.Ui.imageInfo)

        self.Ui.info_button.clicked.connect(self.showInfo)
        self.Ui.adjustment_button.clicked.connect(self.showAdjustment)
        self.Ui.editImage_button.clicked.connect(self.showEditImage)
        self.Ui.text_button.clicked.connect(self.showAddText)

    def show(self):
        self.main_win.show()

    def showAdjustment(self):
        self.Ui.stackedWidget.setCurrentWidget(self.Ui.adjustment)

    def showEditImage(self):
        self.Ui.stackedWidget.setCurrentWidget(self.Ui.edit)

    def showAddText(self):
        self.Ui.stackedWidget.setCurrentWidget(self.Ui.addText)

    def showInfo(self):
        self.Ui.stackedWidget.setCurrentWidget(self.Ui.imageInfo)

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
