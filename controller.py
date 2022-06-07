import cv2

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_main_window import Ui_Main_Window

import qimage2ndarray
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._window = Ui_Main_Window()
        self._window.setupUi(self)
        self.setup_camera()

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        ret, frame = self.capture.read()
        if ret:
            height, width = frame.shape[0], frame.shape[1]
            scale = 1.0
            frame = cv2.resize(frame, (int(width * scale), int(height * scale)), interpolation=cv2.INTER_NEAREST)

            self._window.Img_Lable.setFixedSize(frame.shape[1], frame.shape[0])
            self.setFixedSize(frame.shape[1], frame.shape[0] + 45)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame, 1)


            image = qimage2ndarray.array2qimage(frame)  #SOLUTION FOR MEMORY LEAK
            self._window.Img_Lable.setPixmap(QPixmap.fromImage(image))

    def Statusbar_Message(self, message):
        self._window.statusbar.showMessage(message)



