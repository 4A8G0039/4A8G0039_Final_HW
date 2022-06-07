import sys

from controller import MainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())