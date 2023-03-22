import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2
import imutils

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

        '''self.Ui.insert_new.clicked.connect(self.loadImage)
        self.Ui.open_folder.clicked.connect(self.openDirectory)
        self.Ui.actionOpen_Image.triggered.connect(self.loadImage)
        self.Ui.actionOpen_Folder.triggered.connect(self.openDirectory)'''

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

    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(
            filter="Image (*.jpg, *.png)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)

    def openDirectory(self):
        directory = str(QFileDialog.getExistingDirectory(
            None, "Select Directory"))
        self.file_list = [directory + "/" + f for f in os.listdir(
            directory) if f.endswith(".jpg") or f.endswith(".png")]
        self.file_counter = 0
        self.current_file = self.file_list[self.file_counter]
        self.setPhoto(self.current_file)

    def setPhoto(self, image):
        """This function will take image input and resize it
                only for display purpose and convert it to QImage to set at the label.
                """
        self.tmp = image
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.Ui.image_label.setPixmap(QtGui.QPixmap.fromImage(image))

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
