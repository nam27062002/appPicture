from PyQt5 import QtCore, QtGui, QtWidgets
import  processFile,pyautogui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        width, height = pyautogui.size()
        MainWindow.setGeometry((width - 600)/2,(height - 400)/2,600,400)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "    background:rgb(76, 76, 76);\n"
                                 "}")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 95, 400, 210))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(29, 15, 341, 80))
        self.frame_2.setStyleSheet("QFrame{\n"
                                   "    background:rgb(129, 129, 129);\n"
                                   "    border-radius:10px;\n"          
                                   "}\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 15, 81, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/form/folder.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(100, 20, 201, 41))
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(29, 120, 341, 80))
        self.frame_3.setStyleSheet("QFrame{\n"
                                   "    background:rgb(129, 129, 129);\n"
                                   "    border-radius:10px;\n"
                                   "}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 5, 81, 70))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/form/icons8-add-folder-64.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(100, 20, 221, 41))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Open a local folder</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Create a new project</span></p></body></html>"))
        self.frame_2.enterEvent = self.eventHoverOpenFolder
        self.frame_2.leaveEvent = self.eventLeaveOpenFolder
        self.frame_3.enterEvent = self.eventHoverNewFolder
        self.frame_3.leaveEvent = self.eventLeaveNewFolder


    def eventHoverOpenFolder(self,e):
        self.frame_2.setStyleSheet("QFrame{\n"
                                   "    background:rgb(41, 137, 75);\n"
                                   "    border-radius:10px;\n"
                                   "    border: 3px solid rgb(255, 255, 255);\n"
                                   "}\n"
                                   "")
        self.label.setStyleSheet("QFrame{\n"
                                   "    border: 3px solid rgb(41, 137, 75);\n"
                                   "}\n"
                                   "")
        self.label_3.setStyleSheet("QFrame{\n"
                                 "    border: 3px solid rgb(41, 137, 75);\n"
                                 "}\n"
                                 "")
    def eventLeaveOpenFolder(self,e):
        self.frame_2.setStyleSheet("QFrame{\n"
                                   "    background:rgb(129, 129, 129);\n"
                                   "    border-radius:10px;\n"
                                   "}\n"
                                   "")
        self.label.setStyleSheet("QFrame{\n"
                                 "    border: 3px solid rgb(129, 129, 129);\n"
                                 "}\n"
                                 "")
        self.label_3.setStyleSheet("QFrame{\n"
                                   "    border: 3px solid rgb(129, 129, 129);\n"
                                   "}\n"
                                   "")
    def eventHoverNewFolder(self,e):
        self.frame_3.setStyleSheet("QFrame{\n"
                                   "    background:rgb(41, 137, 75);\n"
                                   "    border-radius:10px;\n"
                                   "    border: 3px solid rgb(255, 255, 255);\n"
                                   "}\n"
                                   "")
        self.label_4.setStyleSheet("QFrame{\n"
                                   "    border: 3px solid rgb(41, 137, 75);\n"
                                   "}\n"
                                   "")
        self.label_5.setStyleSheet("QFrame{\n"
                                 "    border: 3px solid rgb(41, 137, 75);\n"
                                 "}\n"
                                 "")
    def eventLeaveNewFolder(self,e):
        self.frame_3.setStyleSheet("QFrame{\n"
                                   "    background:rgb(129, 129, 129);\n"
                                   "    border-radius:10px;\n"
                                   "}\n"
                                   "")
        self.label_4.setStyleSheet("QFrame{\n"
                                 "    border: 3px solid rgb(129, 129, 129);\n"
                                 "}\n"
                                 "")
        self.label_5.setStyleSheet("QFrame{\n"
                                   "    border: 3px solid rgb(129, 129, 129);\n"
                                   "}\n"
                                   "")