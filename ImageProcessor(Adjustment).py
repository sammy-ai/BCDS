import sys
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QLabel, QSlider, QVBoxLayout, QWidget


class ImageProcessor(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.processed_image = self.image.copy()

        # Set up the UI
        self.image_label = QLabel(self)
        self.image_label.setPixmap(self._cvimage_to_qpixmap(self.image))

        self.tint_slider = QSlider(Qt.Horizontal)
        self.tint_slider.setMinimum(-100)
        self.tint_slider.setMaximum(100)
        self.tint_slider.setTickInterval(10)
        self.tint_slider.setValue(0)

        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setMinimum(-100)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setTickInterval(10)
        self.brightness_slider.setValue(0)

        self.saturation_slider = QSlider(Qt.Horizontal)
        self.saturation_slider.setMinimum(-100)
        self.saturation_slider.setMaximum(100)
        self.saturation_slider.setTickInterval(10)
        self.saturation_slider.setValue(0)

        self.tint_slider.valueChanged.connect(self.update_image)
        self.brightness_slider.valueChanged.connect(self.update_image)
        self.saturation_slider.valueChanged.connect(self.update_image)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.tint_slider)
        layout.addWidget(self.brightness_slider)
        layout.addWidget(self.saturation_slider)

        self.setLayout(layout)

    def update_image(self, value):
        self.processed_image = self._adjust_tint(
            self.image, self.tint_slider.value())
        self.processed_image = self._adjust_brightness(
            self.processed_image, self.brightness_slider.value())
        self.processed_image = self._adjust_saturation(
            self.processed_image, self.saturation_slider.value())
        self.image_label.setPixmap(
            self._cvimage_to_qpixmap(self.processed_image))

    def _adjust_tint(self, image, value):
        h, s, v = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
        h = h + value
        h[h < 0] = 0
        h[h > 179] = 179
        hsv = cv2.merge((h, s, v))
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    def _adjust_brightness(self, image, value):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        v = cv2.add(v, value)
        v[v < 0] = 0
        v[v > 255] = 255
        hsv = cv2.merge((h, s, v))
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    def _adjust_saturation(self, image, value):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        s = cv2.add(s, value)
        s[s < 0] = 0
        s[s > 255] = 255
        hsv = cv2.merge((h, s, v))
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    def _cvimage_to_qpixmap(self, image):
        h, w = image.shape[:2]
        # Create QImage from OpenCV image
        qimage = QImage(image.data, w, h, 3 * w, QImage.Format_BGR888)
        # Convert QImage to QPixmap
        qpixmap = QPixmap.fromImage(qimage)
        return qpixmap


if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    window.show()

    # Run the application
    sys.exit(app.exec_())
