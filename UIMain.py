from PyQt5 import QtCore, QtGui, QtWidgets
import processFile
import pyautogui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,url):
        MainWindow.setObjectName("MainWindow")
        width, height = pyautogui.size()
        MainWindow.setGeometry((width - 1200)/2,(height - 900)/2,1200,900)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    border-image : url(:/img/bg.png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(350, 50, 800, 800))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background:white;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(50, 50, 701, 711))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(-50, -60, 800, 800))
        font = QtGui.QFont()
        self.url = url
        font.setFamily("MS UI Gothic")
        self.label.setFont(font)
        self.label.setText("")
        self.A = []
        self.allUrl = processFile.getAllUrl(self.url)
        self.label.setPixmap(QtGui.QPixmap("images/form/bg.png"))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(210, 730, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"    background : none;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 500, 900))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 421, 900))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/form/ww.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/form/ccc.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(0, 480, 411, 411))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/project1/305345969_808631450337177_2857364494081896737_n.png"))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"    background : none;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(40, 170, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"    background : none;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(40, 210, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"    background : none;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(30, 250, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"    background : none;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(20, 320, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"    background : none;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.frame_3.raise_()
        self.frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 26))
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
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ff557f;\">@CAOSHEEP/han.ratt</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff557f;\">CAOSHEEP</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ff7b8f;\">NEW EMOTES</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#d5aeb5;\">twitch.tv/</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ff557f;\">Sailormiu</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ff8ba4;\">28x56x112</span></p></body></html>"))
        self.label_4.mousePressEvent = self.changeMain
        self.frame_2.mousePressEvent = self.changeMatrix
        self.change()
    def changeMain(self,e):
        directory = QtWidgets.QFileDialog.getOpenFileName(filter="Images (*.png)")
        if directory[0] != "":
            processFile.changeForLine(self.url,directory[0],0)
            self.allUrl = processFile.getAllUrl(self.url)
            self.change()
    def changeMatrix(self,e):
        directory = QtWidgets.QFileDialog.getOpenFileNames(filter="Images (*.png)")
        if len(directory[0]) != 0:
                for i in directory[0]:
                        processFile.add(self.url,i)
                self.allUrl = processFile.getAllUrl(self.url)
                self.change()
    def change(self):
        if len(self.allUrl) != 0:
                self.allUrl = processFile.getAllUrl(self.url)
                S = QtGui.QPixmap(self.allUrl[0])
                S = S.scaled(411,411)
                self.label_4.setPixmap(S)
                if len(self.allUrl) >= 2:
                        for i in range(len(self.allUrl) - 1):
                                self.A.append(QtWidgets.QLabel(self.frame_2))
        
                        self.matrix(len(self.allUrl) - 1)
    def matrix(self,index):
        A = []
        size = 0
        if index == 1:
                A = [[150,110]]
                size = 500
        elif index == 2:
                A = [[100,250],[440,250]]
                size = 270
        elif index == 3:
                A = [[100,130],[440,130],[250,450]]
                size = 270
        elif index == 4:
                A = [[100,130],[440,130],[100,450],[440,450]]
                size = 270
        elif index == 5:
                A = [[70,50],[500,50],[280,280],[70,500],[500,500]]
                size = 220
        elif index == 6:
                A = [[60,170],[295,170],[530,170],[60,390],[295,390],[530,390],]
                size = 210
        elif index == 7:
                A = [[60,40],[295,40],[530,40],[60,280],[295,280],[530,280],[295,520]]
                size = 210
        elif index == 8:
                A = [[60,40],[295,40],[530,40],[60,280],[295,280],[530,280],[170,520],[420,520]]
                size = 210
        elif index == 9:
                A = [[60,40],[295,40],[530,40],[60,280],[295,280],[530,280],[60,520],[295,520],[530,520]]
                size = 210
        elif index == 10:
                A = [[85,10],[320,10],[550,10],[85,195],[320,195],[550,195],[85,380],[320,380],[550,380],[320,560]]
                size = 170
        elif index == 11:
                A = [[85,10],[320,10],[550,10],[85,195],[320,195],[550,195],[85,380],[320,380],[550,380],[195,560],[445,560]]
                size = 170
        elif index == 12:
                A = [[85,10],[320,10],[550,10],[85,195],[320,195],[550,195],[85,380],[320,380],[550,380],[85,560],[320,560],[550,560]]
                size = 170
        elif index == 13:
                A = [[70,50],[240,50],[410,50],[580,50],[70,230],[240,230],[410,230],[580,230],[70,400],[240,400],[410,400],[580,400],[330,570]]
                size = 150
        elif index == 14:
                A = [[70,50],[240,50],[410,50],[580,50],[70,230],[240,230],[410,230],[580,230],[70,400],[240,400],[410,400],[580,400],[240,570],[410,570]]
                size = 150
        elif index == 15:
                A = [[70,50],[240,50],[410,50],[580,50],[70,230],[240,230],[410,230],[580,230],[70,400],[240,400],[410,400],[580,400],[160,570],[330,570],[500,570]]
                size = 150
        elif index == 16:
                A = [[70,50],[240,50],[410,50],[580,50],[70,230],[240,230],[410,230],[580,230],[70,400],[240,400],[410,400],[580,400],[70,570],[240,570],[410,570],[580,570]]
                size = 150
        elif index == 17:
                A = [[70,120],[205,120],[340,120],[475,120],[610,120],[70,280],[205,280],[340,280],[475,280],[610,280],[70,440],[205,440],[340,440],[475,440],[610,440],[270,580],[420,580]]
                size = 120
        elif index == 18:
                A = [[70,120],[205,120],[340,120],[475,120],[610,120],[70,280],[205,280],[340,280],[475,280],[610,280],[70,440],[205,440],[340,440],[475,440],[610,440],[205,580],[340,580],[475,580]]
                size = 120
        elif index == 19:
                A = [[70,120],[205,120],[340,120],[475,120],[610,120],[70,280],[205,280],[340,280],[475,280],[610,280],[70,440],[205,440],[340,440],[475,440],[610,440],[140,580],[270,580],[405,580],[540,580]]
                size = 120
        elif index == 20:
                A = [[70,120],[205,120],[340,120],[475,120],[610,120],[70,280],[205,280],[340,280],[475,280],[610,280],[70,440],[205,440],[340,440],[475,440],[610,440],[70,580],[205,580],[340,580],[475,580],[610,580]]
                size = 120
        for i in range(index):
                self.A[i].setGeometry(QtCore.QRect(A[i][0],A[i][1], size, size))
                self.A[i].setText("")
                S = QtGui.QPixmap(self.allUrl[i])
                S = S.scaled(size,size)
                self.A[i].setPixmap(S)
                self.A[i].setObjectName("label_4")
                self.A[i].show()
import img_rc
