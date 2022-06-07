from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_Main_Window(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(500, 500) #設定視窗大小
        MainWindow.setWindowTitle("4A8G0039") #設定視窗標題
    #CentralWidget#
        self.centralwidget = QWidget(MainWindow) #新增一個QWidget命名為centralwidget
        self.verticalLayout = QHBoxLayout(self.centralwidget) #設定centralwidget為水平Layout並命名為verticalLayout
        self.verticalLayout.setContentsMargins(0, 0, 0, 0) #設定verticalLayout的邊距
        self.Img_Lable = QLabel(self.centralwidget) #新增一個QLabel命名為Img_Lable
        self.Img_Lable.setMinimumSize(QSize(0, 0)) #設定QLabel的最小尺寸
        self.Img_Lable.setAlignment(Qt.AlignCenter) #設定QLabel裡的物件置中
        self.verticalLayout.addWidget(self.Img_Lable, 0, Qt.AlignHCenter|Qt.AlignVCenter) #把Img_Lable加進verticalLayout並設為水平置中，垂直置中
        MainWindow.setCentralWidget(self.centralwidget) #將主視窗的CentralWidget設為centralwidget
    #CentralWidget#
    #MenuBar#
        self.Top_menubar = QMenuBar(MainWindow) #新增一個QMenuBar命名為Top_menubar
        self.Top_menubar.setGeometry(QRect(0, 0, 600, 25)) #設定Top_menubar的尺寸
    #File_menu
        self.VideoCapture_menu = QMenu(self.Top_menubar)
        self.VideoCapture_menu.setTitle("VideoCapture")
        self.VideoCapture_action = QAction(MainWindow)
        self.VideoCapture_action.setText("OPEN")
        self.VideoCapture_action.setShortcut("Ctrl+V")
        self.VideoCapture_menu.addAction(self.VideoCapture_action)
        self.Top_menubar.addAction(self.VideoCapture_menu.menuAction())
    #File_menu
        MainWindow.setMenuBar(self.Top_menubar)
    #MenuBar#

    #StatusBar#
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
    #StatusBar#
        QMetaObject.connectSlotsByName(MainWindow)