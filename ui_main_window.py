from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_Main_Window(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(400, 400) #設定視窗大小
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

    #VideoCapture_menu
        self.VideoCapture_menu = QMenu(self.Top_menubar)
        self.VideoCapture_menu.setTitle("Video Capture")
        self.VideoCapture_action = QAction(MainWindow)
        self.VideoCapture_action.setText("OPEN")
        self.VideoCapture_action.setShortcut("Ctrl+V")
        self.VideoCapture_menu.addAction(self.VideoCapture_action)
        self.Top_menubar.addAction(self.VideoCapture_menu.menuAction())
    #VideoCapture_menu

    #HandDetection_menu
        self.HandDetection_menu = QMenu(self.Top_menubar)
        self.HandDetection_menu.setTitle("Hand Detection")
        self.HandDetection_action = QAction(MainWindow)
        self.HandDetection_action.setText("OPEN")
        self.HandDetection_action.setShortcut("Ctrl+H")
        self.HandDetection_menu.addAction(self.HandDetection_action)
        self.Top_menubar.addAction(self.HandDetection_menu.menuAction())
    #HandDetection_menu

    #FaceDetection_menu
        self.FaceDetection_menu = QMenu(self.Top_menubar)
        self.FaceDetection_menu.setTitle("Face Detection")
        self.FaceDetection_action = QAction(MainWindow)
        self.FaceDetection_action.setText("OPEN")
        self.FaceDetection_action.setShortcut("Ctrl+F")
        self.FaceDetection_menu.addAction(self.FaceDetection_action)
        self.Top_menubar.addAction(self.FaceDetection_menu.menuAction())
    #FaceDetection_menu

    #PoseDetection_menu
        self.PoseDetection_menu = QMenu(self.Top_menubar)
        self.PoseDetection_menu.setTitle("Pose Detection")
        self.PoseDetection_action = QAction(MainWindow)
        self.PoseDetection_action.setText("OPEN")
        self.PoseDetection_action.setShortcut("Ctrl+P")
        self.PoseDetection_menu.addAction(self.PoseDetection_action)
        self.Top_menubar.addAction(self.PoseDetection_menu.menuAction())
    #PoseDetection_menu

        MainWindow.setMenuBar(self.Top_menubar)
    #MenuBar#

    #StatusBar#
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
    #StatusBar#
        QMetaObject.connectSlotsByName(MainWindow)