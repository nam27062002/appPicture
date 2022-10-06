from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui
import processFile


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, url):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('images/img.jpg'))
        width, height = pyautogui.size()
        MainWindow.setGeometry((width - 1200) / 2, (height - 900) / 2, 1200, 900)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "    border-image :url(:/img/images/bg.png); \n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labeRight = QtWidgets.QLabel(self.centralwidget)
        self.labeRight.setGeometry(QtCore.QRect(0, 30, 431, 880))
        self.labeRight.setText("")
        self.labeRight.setPixmap(QtGui.QPixmap("images/bg3.png"))
        self.labeRight.setObjectName("labeRight")
        self.imgMain = QtWidgets.QLabel(self.centralwidget)
        self.imgMain.setGeometry(QtCore.QRect(-20, 485, 440, 440))
        self.imgMain.setText("")
        self.imgMain.setObjectName("imgMain")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 30, 800, 800))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/bg1.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.url = url
        self.fileTxt = []
        self.A = []
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.imgMain.setAcceptDrops(True)
        self.imgMain.dragEnterEvent = self.DragEnter
        self.imgMain.dropEvent = self.dropEvent
        self.label.setAcceptDrops(True)
        self.label.dragEnterEvent = self.DragEnter
        self.label.dropEvent = self.dropEvent1
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "27-6 sinh nhật Nam :)"))
        self.imgMain.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ff979e;\">twitch.tv/</span></p></body></html>"))
        self.lineEdit.hide()
        self.loadFileTxt()
        self.loadText()
        self.imgMain.mousePressEvent = self.clickImgMain
        self.loadMainPicture()
        self.loadSubPicture()
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.mousePressEvent = self.addSubImage
        self.loadDropEvent()
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.mousePressEvent = self.changeText
        self.lineEdit.returnPressed.connect(self.submitText)
    def submitText(self):
        self.fileTxt[0] = self.lineEdit.text()
        self.loadText()
        processFile.saveFile(self.url, self.fileTxt)
        self.lineEdit.hide()
    def changeText(self,e):
        self.lineEdit.show()
    def loadDropEvent(self):
        try:
            self.A[0].dropEvent = self.E0
            self.A[1].dropEvent = self.E1
            self.A[2].dropEvent = self.E2
            self.A[3].dropEvent = self.E3
            self.A[4].dropEvent = self.E4
            self.A[5].dropEvent = self.E5
            self.A[6].dropEvent = self.E6
            self.A[7].dropEvent = self.E7
            self.A[8].dropEvent = self.E8
            self.A[9].dropEvent = self.E9
            self.A[10].dropEvent = self.E10
            self.A[11].dropEvent = self.E11
            self.A[12].dropEvent = self.E12
            self.A[13].dropEvent = self.E13
            self.A[14].dropEvent = self.E14
            self.A[15].dropEvent = self.E15
            self.A[16].dropEvent = self.E16
            self.A[17].dropEvent = self.E17
            self.A[18].dropEvent = self.E18
            self.A[19].dropEvent = self.E19
        except:
            pass
    def addSubImage(self,e):
        directory = QtWidgets.QFileDialog.getOpenFileNames(filter="Images (*.png)")
        if len(directory[0]) != 0:
            for i in directory[0]:
                self.fileTxt.append(i)
                self.loadSubPicture()
                processFile.saveFile(self.url, self.fileTxt)
    def clickImgMain(self, event):
        if event.button() == 1:
            directory = QtWidgets.QFileDialog.getOpenFileName(filter="Images (*.png)")
            if directory[0] != "":
                try:
                    self.fileTxt[1] = directory[0]
                except:
                    self.fileTxt.append(directory[0])
                self.loadMainPicture()
                processFile.saveFile(self.url, self.fileTxt)
        elif event.button() == 2:
            try:
                self.fileTxt[1] = ""
            except:
                pass
            self.loadMainPicture()
            processFile.saveFile(self.url, self.fileTxt)
    def clickSub(self,index):
        directory = QtWidgets.QFileDialog.getOpenFileName(filter="Images (*.png)")
        if directory[0] != "":
            try:
                self.fileTxt[index] = directory[0]
            except:
                pass
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
    def loadFileTxt(self):
        self.fileTxt = processFile.getAllUrl(self.url)
        if len(self.fileTxt) == 1:
            self.fileTxt.append("")

    def loadText(self):
        self.label_4.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ff007f;\">" +
            self.fileTxt[0] + "</span></p></body></html>")

    def loadMainPicture(self):
        try:
            self.imgMain.setPixmap(QtGui.QPixmap(self.fileTxt[1]).scaled(440, 440))
        except:
            pass

    def loadSubPicture(self):
        self.loadDropEvent()
        index = len(self.fileTxt) - 2
        try:
            for i in range(index):
                self.A.append(QtWidgets.QLabel(self.centralwidget))
            if index == 1:
                A = [[500, 160]]
                size = 500
            elif index == 2:
                A = [[470, 250], [770, 250]]
                size = 270
            elif index == 3:
                A = [[500, 190], [770, 190], [640, 450]]
                size = 230
            elif index == 4:
                A = [[500, 190], [770, 190], [500, 450], [770, 450]]
                size = 230
            elif index == 5:
                A = [[390, 180], [650, 180], [900, 180], [510, 430], [770, 430]]
                size = 230
            elif index == 6:
                A = [[390, 180], [650, 180], [900, 180], [390, 430], [650, 430], [900, 430]]
                size = 230
            elif index == 7:
                A = [[400, 60], [650, 60], [890, 60], [400, 290], [650, 290], [890, 290], [650, 530]]
                size = 220
            elif index == 8:
                A = [[400, 60], [650, 60], [890, 60], [400, 290], [650, 290], [890, 290], [530, 530], [770, 530]]
                size = 220
            elif index == 9:
                A = [[400, 60], [650, 60], [890, 60], [400, 290], [650, 290], [890, 290], [400, 530], [650, 530],
                     [890, 530]]
                size = 220
            elif index == 10:
                A = [[400, 160], [580, 160], [760, 160], [940, 160], [400, 340], [580, 340], [760, 340], [940, 340],
                     [580, 520], [760, 520]]
                size = 170
            elif index == 11:
                A = [[400, 160], [580, 160], [760, 160], [940, 160], [400, 340], [580, 340], [760, 340], [940, 340],
                     [490, 520], [680, 520], [870, 520]]
                size = 170
            elif index == 12:
                A = [[400, 160], [580, 160], [760, 160], [940, 160], [400, 340], [580, 340], [760, 340], [940, 340],
                     [400, 520], [580, 520], [760, 520], [940, 520]]
                size = 170
            elif index == 13:
                A = [[400, 55], [580, 55], [760, 55], [940, 55], [400, 230], [580, 230], [760, 230], [940, 230],
                     [400, 410], [580, 410], [760, 410], [940, 410], [680, 590]]
                size = 170
            elif index == 14:
                A = [[400, 55], [580, 55], [760, 55], [940, 55], [400, 230], [580, 230], [760, 230], [940, 230],
                     [400, 410], [580, 410], [760, 410], [940, 410], [580, 590], [760, 590]]
                size = 170
            elif index == 15:
                A = [[400, 55], [580, 55], [760, 55], [940, 55], [400, 230], [580, 230], [760, 230], [940, 230],
                     [400, 410], [580, 410], [760, 410], [940, 410], [480, 590], [665, 590],[850, 590]]
                size = 170
            elif index == 16:
                A = [[400, 55], [580, 55], [760, 55], [940, 55], [400, 230], [580, 230], [760, 230], [940, 230],
                     [400, 410], [580, 410], [760, 410], [940, 410], [400, 590], [580, 590], [760, 590], [940, 590]]
                size = 170
            elif index == 17:
                A = [[400, 100], [550, 100], [700, 100], [850, 100], [1000, 100],
                     [400, 270], [550, 270], [700, 270], [850, 270], [1000, 270],
                     [400, 440], [550, 440], [700, 440], [850, 440], [1000, 440],
                     [630, 620], [780, 620]]
                size = 130
            elif index == 18:
                A = [[400, 100], [550, 100], [700, 100], [850, 100], [1000, 100],
                     [400, 270], [550, 270], [700, 270], [850, 270], [1000, 270],
                     [400, 440], [550, 440], [700, 440], [850, 440], [1000, 440],
                     [550, 620], [700, 620], [850, 620]]
                size = 130
            elif index == 19:
                A = [[400, 100], [550, 100], [700, 100], [850, 100], [1000, 100],
                     [400, 270], [550, 270], [700, 270], [850, 270], [1000, 270],
                     [400, 440], [550, 440], [700, 440], [850, 440], [1000, 440],
                     [470, 620], [630, 620], [790, 620],[950, 620]]
                size = 130
            elif index == 20:
                A = [[400, 100], [550, 100], [700, 100], [850, 100], [1000, 100],
                     [400, 270], [550, 270], [700, 270], [850, 270], [1000, 270],
                     [400, 440], [550, 440], [700, 440], [850, 440], [1000, 440],
                     [400, 620], [550, 620], [700, 620], [850, 620], [1000, 620]]
                size = 130
            for i in range(index):
                self.A[i].setGeometry(QtCore.QRect(A[i][0], A[i][1], size, size))
                self.A[i].setText("")
                self.A[i].setPixmap(QtGui.QPixmap(self.fileTxt[i + 2]).scaled(size, size))
                self.A[i].setAcceptDrops(True)
                self.A[i].dragEnterEvent = self.DragEnter
                self.A[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.A[i].show()

            self.A[0].mousePressEvent = self.clickSubImage0
            self.A[1].mousePressEvent = self.clickSubImage1
            self.A[2].mousePressEvent = self.clickSubImage2
            self.A[3].mousePressEvent = self.clickSubImage3
            self.A[4].mousePressEvent = self.clickSubImage4
            self.A[5].mousePressEvent = self.clickSubImage5
            self.A[6].mousePressEvent = self.clickSubImage6
            self.A[7].mousePressEvent = self.clickSubImage7
            self.A[8].mousePressEvent = self.clickSubImage8
            self.A[9].mousePressEvent = self.clickSubImage9
            self.A[10].mousePressEvent = self.clickSubImage10
            self.A[11].mousePressEvent = self.clickSubImage11
            self.A[12].mousePressEvent = self.clickSubImage12
            self.A[13].mousePressEvent = self.clickSubImage13
            self.A[14].mousePressEvent = self.clickSubImage14
            self.A[15].mousePressEvent = self.clickSubImage15
            self.A[16].mousePressEvent = self.clickSubImage16
            self.A[17].mousePressEvent = self.clickSubImage17
            self.A[18].mousePressEvent = self.clickSubImage18
            self.A[19].mousePressEvent = self.clickSubImage19


        except:
            pass
    def clickSubImage0(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(2)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(2)
    def clickSubImage1(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(3)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(3)
    def clickSubImage2(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(4)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(4)
    def clickSubImage3(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(5)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(5)
    def clickSubImage4(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(6)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(6)
    def clickSubImage5(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(7)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(7)
    def clickSubImage6(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(8)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(8)
    def clickSubImage7(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(9)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(9)
    def clickSubImage8(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(10)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(10)
    def clickSubImage9(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(11)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(11)
    def clickSubImage10(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(12)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(12)
    def clickSubImage11(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(13)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(13)
    def clickSubImage12(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(14)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(14)
    def clickSubImage13(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(15)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(15)
    def clickSubImage14(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(16)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(16)
    def clickSubImage15(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(17)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(17)
    def clickSubImage16(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(18)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(18)
    def clickSubImage17(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(19)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(19)
    def clickSubImage18(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(20)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(20)
    def clickSubImage19(self,e):
        if e.button() == 2:
            self.hidenAll()
            self.fileTxt.pop(21)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        elif e.button() == 1:
            self.clickSub(21)
    def hidenAll(self):
        for i in self.A:
            i.hide()
    def DragEnter(self, event):
        x = event.mimeData().urls()[0].toLocalFile()
        s = ""
        for i in range(len(x) - 1, -1, -1):
            if x[i] != ".":
                s = x[i] + s
            else:
                break
        if s == "png":
            event.accept()
        else:
            print(x)
            event.ignore()

    def dropEvent(self, event):
        x = event.mimeData().urls()[0].toLocalFile()
        s = ""
        for i in range(len(x) - 1, -1, -1):
            if x[i] != ".":
                s = x[i] + s
            else:
                break
        if s == "png":
            event.accept()
            try:
                self.fileTxt[1] = x
            except:
                self.fileTxt.append(x)
            self.loadMainPicture()
            processFile.saveFile(self.url, self.fileTxt)
        else:
            event.ignore()

    def dropEvent1(self, event):
        x = event.mimeData().urls()[0].toLocalFile()
        s = ""
        for i in range(len(x) - 1, -1, -1):
            if x[i] != ".":
                s = x[i] + s
            else:
                break
        if s == "png":
            event.accept()
            self.fileTxt.append(x)
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        else:
            event.ignore()

    def changeForIndex(self,index,event):
        x = event.mimeData().urls()[0].toLocalFile()
        s = ""
        for i in range(len(x) - 1, -1, -1):
            if x[i] != ".":
                s = x[i] + s
            else:
                break
        if s == "png":
            event.accept()
            self.fileTxt[index + 2] = x
            self.loadSubPicture()
            processFile.saveFile(self.url, self.fileTxt)
        else:
            event.ignore()
    def E0(self,event):
        self.changeForIndex(0,event)
    def E1(self,event):
        self.changeForIndex(1,event)
    def E2(self,event):
        self.changeForIndex(2,event)
    def E3(self,event):
        self.changeForIndex(3,event)
    def E4(self,event):
        self.changeForIndex(4,event)
    def E5(self,event):
        self.changeForIndex(5,event)
    def E6(self,event):
        self.changeForIndex(6,event)
    def E7(self,event):
        self.changeForIndex(7,event)
    def E8(self,event):
        self.changeForIndex(8,event)
    def E9(self,event):
        self.changeForIndex(9,event)
    def E10(self,event):
        self.changeForIndex(10,event)
    def E11(self,event):
        self.changeForIndex(11,event)
    def E12(self,event):
        self.changeForIndex(12,event)
    def E13(self,event):
        self.changeForIndex(13,event)
    def E14(self,event):
        self.changeForIndex(14,event)
    def E15(self,event):
        self.changeForIndex(15,event)
    def E16(self,event):
        self.changeForIndex(16,event)
    def E17(self,event):
        self.changeForIndex(17,event)
    def E18(self,event):
        self.changeForIndex(18,event)
    def E19(self,event):
        self.changeForIndex(19,event)

import img_rc
