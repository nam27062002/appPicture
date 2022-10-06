from PyQt5 import QtCore, QtGui, QtWidgets
from processFile import getAllProject
import pyautogui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        width, height = pyautogui.size()
        MainWindow.setGeometry((width - 800)/2,(height - 592)/2,800,592)
        MainWindow.setStyleSheet("")
        MainWindow.setWindowIcon(QtGui.QIcon('images/img.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 60, 751, 421))
        self.frame.setStyleSheet("QFrame{\n"
                                 "    background: rgb(56, 56, 56);\n"
                                 "    border-radius:20px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listFrame = []
        self.listlabel1 = []
        self.listlabel2 = []
        self.allProject = getAllProject()
        self.index = 0
        self.clicked = -1
        for i in range(len(self.allProject)):
            self.listFrame.append(QtWidgets.QFrame(self.frame))
            self.listlabel1.append(QtWidgets.QLabel(self.listFrame[i]))
            self.listlabel2.append(QtWidgets.QLabel(self.listFrame[i]))
        self.loadTable()

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 360, 121, 41))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    border: 2px solid rgb(74, 74, 74);\n"
                                        "    background: rgb(197, 197, 197);\n"
                                        "    border-radius:10px;\n"
                                        "    font-weight: 600;\n"
                                        "    font-size: 16px;\n"
                                        "color: white;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    border: 2px solid rgb(85, 255, 0);\n"
                                        "    background:white;\n"
                                        "    color: rgb(85, 255, 0);\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 360, 121, 41))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    border: 2px solid rgb(74, 74, 74);\n"
                                        "    background: rgb(255, 0, 0);\n"
                                        "    border-radius:10px;\n"
                                        "    font-weight: 600;\n"
                                        "    font-size: 16px;\n"
                                        "color:white;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    color: black;\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 121, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    border: 2px solid rgb(74, 74, 74);\n"
                                      "    border-radius:10px;\n"
                                      "    font-weight: 600;\n"
                                      "    font-size: 16px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    border: 2px solid rgb(85, 255, 0);\n"
                                      "    background:white;\n"
                                      "    color: rgb(85, 255, 0);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(652, 500, 121, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    border: 2px solid rgb(74, 74, 74);\n"
                                        "    border-radius:10px;\n"
                                        "    font-weight: 600;\n"
                                        "    font-size: 16px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    border: 2px solid rgb(85, 255, 0);\n"
                                        "    background:white;\n"
                                        "    color: rgb(85, 255, 0);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 10, 231, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    border: 2px solid  rgb(237, 51, 59);\n"
                                    "    border-radius: 10px;\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(720, 14, 21, 21))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/—Pngtree—vector search icon_3994986.png"))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "27-6 sinh nhật Nam :)"))
        self.checkStatePrev()
        self.checkStateNext()
        self.checkStateClicked()
        def hover0(e):
            if self.clicked != 0:
                self.listFrame[0 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(200, 200, 200);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def leave0(e):
            if self.clicked != 0:
                self.listFrame[0 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(113, 113, 113);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def hover1(e):
            if self.clicked != 1:
                self.listFrame[1 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(200, 200, 200);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def leave1(e):
            if self.clicked != 1:
                self.listFrame[1 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(113, 113, 113);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def hover2(e):
            if self.clicked != 2:
                self.listFrame[2 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(200, 200, 200);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def leave2(e):
            if self.clicked != 2:
                self.listFrame[2 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(113, 113, 113);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def hover3(e):
            if self.clicked != 3:
                self.listFrame[3 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(200, 200, 200);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def leave3(e):
            if self.clicked != 3 + self.index * 12:
                self.listFrame[3 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(113, 113, 113);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def hover4(e):
            if self.clicked != 4:
                self.listFrame[4 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(200, 200, 200);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def leave4(e):
            if self.clicked != 4:
                self.listFrame[4 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(113, 113, 113);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def hover5(e):
            if self.clicked != 5:
                self.listFrame[5 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(200, 200, 200);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def leave5(e):
            if self.clicked != 5:
                self.listFrame[5 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(113, 113, 113);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def hover6(e):
            if self.clicked != 6:
                self.listFrame[6 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(200, 200, 200);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def leave6(e):
            if self.clicked != 6:
                self.listFrame[6 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(113, 113, 113);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def hover7(e):
            if self.clicked != 7:
                self.listFrame[7 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(200, 200, 200);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def leave7(e):
            if self.clicked != 7:
                self.listFrame[7 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(113, 113, 113);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def hover8(e):
            if self.clicked != 8:
                self.listFrame[8 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(200, 200, 200);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def leave8(e):
            if self.clicked != 8:
                self.listFrame[8 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(113, 113, 113);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def hover9(e):
            if self.clicked != 9:
                self.listFrame[9 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(200, 200, 200);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def leave9(e):
            if self.clicked != 9:
                self.listFrame[9 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                  "    background: rgb(113, 113, 113);\n"
                                                                  "    border-radius: 5px;\n"
                                                                  "}")

        def hover10(e):
            if self.clicked != 10:
                self.listFrame[10 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                   "    background: rgb(200, 200, 200);\n"
                                                                   "    border-radius: 5px;\n"
                                                                   "}")

        def leave10(e):
            if self.clicked != 10:
                self.listFrame[10 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                   "    background: rgb(113, 113, 113);\n"
                                                                   "    border-radius: 5px;\n"
                                                                   "}")

        def hover11(e):
            if self.clicked != 11:
                self.listFrame[11 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                   "    background: rgb(200, 200, 200);\n"
                                                                   "    border-radius: 5px;\n"
                                                                   "}")

        def leave11(e):
            if self.clicked != 11:
                self.listFrame[11 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                   "    background: rgb(113, 113, 113);\n"
                                                                   "    border-radius: 5px;\n"
                                                                   "}")

        for i in range(len(self.allProject)):
            self.listlabel2[i].setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">" +
                                                  getAllProject()[i][0] + "</span></p></body></html>"))

        try:
            self.listFrame[0 + self.index * 12].enterEvent = hover0
            self.listFrame[0 + self.index * 12].leaveEvent = leave0

            self.listFrame[1 + self.index * 12].enterEvent = hover1
            self.listFrame[1 + self.index * 12].leaveEvent = leave1

            self.listFrame[2 + self.index * 12].enterEvent = hover2
            self.listFrame[2 + self.index * 12].leaveEvent = leave2

            self.listFrame[3 + self.index * 12].enterEvent = hover3
            self.listFrame[3 + self.index * 12].leaveEvent = leave3

            self.listFrame[4 + self.index * 12].enterEvent = hover4
            self.listFrame[4 + self.index * 12].leaveEvent = leave4
            self.listFrame[5 + self.index * 12].enterEvent = hover5
            self.listFrame[5 + self.index * 12].leaveEvent = leave5

            self.listFrame[6 + self.index * 12].enterEvent = hover6
            self.listFrame[6 + self.index * 12].leaveEvent = leave6

            self.listFrame[7 + self.index * 12].enterEvent = hover7
            self.listFrame[7 + self.index * 12].leaveEvent = leave7

            self.listFrame[8 + self.index * 12].enterEvent = hover8
            self.listFrame[8 + self.index * 12].leaveEvent = leave8

            self.listFrame[9 + self.index * 12].enterEvent = hover9
            self.listFrame[9 + self.index * 12].leaveEvent = leave9

            self.listFrame[10 + self.index * 12].enterEvent = hover10
            self.listFrame[10 + self.index * 12].leaveEvent = leave10

            self.listFrame[11 + self.index * 12].enterEvent = hover11
            self.listFrame[11 + self.index * 12].leaveEvent = leave11

        except:
            pass
        try:
            self.listFrame[0 + self.index * 12].mousePressEvent = self.click0
            self.listFrame[1 + self.index * 12].mousePressEvent = self.click1
            self.listFrame[2 + self.index * 12].mousePressEvent = self.click2
            self.listFrame[3 + self.index * 12].mousePressEvent = self.click3
            self.listFrame[4 + self.index * 12].mousePressEvent = self.click4
            self.listFrame[5 + self.index * 12].mousePressEvent = self.click5
            self.listFrame[6 + self.index * 12].mousePressEvent = self.click6
            self.listFrame[7 + self.index * 12].mousePressEvent = self.click7
            self.listFrame[8 + self.index * 12].mousePressEvent = self.click8
            self.listFrame[9 + self.index * 12].mousePressEvent = self.click9
            self.listFrame[10 + self.index * 12].mousePressEvent = self.click10
            self.listFrame[11 + self.index * 12].mousePressEvent = self.click11
        except:
            pass
        self.pushButton_4.mousePressEvent = self.clickNext
        self.pushButton_3.mousePressEvent = self.clickPrev
        self.pushButton_3.setText(_translate("MainWindow", "Prev"))
        self.pushButton_4.setText(_translate("MainWindow", "Next"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))

    def unRed(self):
        if self.clicked != -1:
            self.listFrame[self.clicked + self.index * 12].setStyleSheet("QFrame{\n"
                                                                         "    background: rgb(113, 113, 113);\n"
                                                                         "    border-radius: 5px;\n"
                                                                         "}")

    def click0(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 0
        self.checkStateClicked()
        self.listFrame[0 + self.index * 12].setStyleSheet("QFrame{\n"
                                                          "    background: rgb(255,0,0);\n"
                                                          "    border-radius: 5px;\n"
                                                          "}")

    def click1(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 1
        self.checkStateClicked()
        self.listFrame[1 + self.index * 12].setStyleSheet("QFrame{\n"
                                                          "    background: rgb(255,0,0);\n"
                                                          "    border-radius: 5px;\n"
                                                          "}")

    def click2(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 2
        self.checkStateClicked()
        self.listFrame[2 + self.index * 12].setStyleSheet("QFrame{\n"
                                                          "    background: rgb(255,0,0);\n"
                                                          "    border-radius: 5px;\n"
                                                          "}")

    def click3(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 3
        self.checkStateClicked()
        self.listFrame[3 + self.index * 12].setStyleSheet("QFrame{\n"
                                                          "    background: rgb(255,0,0);\n"
                                                          "    border-radius: 5px;\n"
                                                          "}")

    def click4(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 4
        self.checkStateClicked()
        self.listFrame[4 + self.index * 12].setStyleSheet("QFrame{\n"
                                                          "    background: rgb(255,0,0);\n"
                                                          "    border-radius: 5px;\n"
                                                          "}")

    def click5(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 5
        self.checkStateClicked()
        self.listFrame[5 + self.index * 12].setStyleSheet("QFrame{\n"
                                                          "    background: rgb(255,0,0);\n"
                                                          "    border-radius: 5px;\n"
                                                          "}")

    def click6(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 6
        self.checkStateClicked()
        self.listFrame[6 + self.index * 12].setStyleSheet("QFrame{\n"
                                                          "    background: rgb(255,0,0);\n"
                                                          "    border-radius: 5px;\n"
                                                          "}")

    def click7(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 7
        self.checkStateClicked()
        self.listFrame[7 + self.index * 12].setStyleSheet("QFrame{\n"
                                                          "    background: rgb(255,0,0);\n"
                                                          "    border-radius: 5px;\n"
                                                          "}")

    def click8(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 8
        self.checkStateClicked()
        self.listFrame[8 + self.index * 12].setStyleSheet("QFrame{\n"
                                                          "    background: rgb(255,0,0);\n"
                                                          "    border-radius: 5px;\n"
                                                          "}")

    def click9(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 9
        self.checkStateClicked()
        self.listFrame[9 + self.index * 12].setStyleSheet("QFrame{\n"
                                                          "    background: rgb(255,0,0);\n"
                                                          "    border-radius: 5px;\n"
                                                          "}")

    def click10(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 10
        self.checkStateClicked()
        self.listFrame[10 + self.index * 12].setStyleSheet("QFrame{\n"
                                                           "    background: rgb(255,0,0);\n"
                                                           "    border-radius: 5px;\n"
                                                           "}")

    def click11(self, e):
        try:
            self.unRed()
        except:
            pass
        self.clicked = 11
        self.checkStateClicked()
        self.listFrame[11 + self.index * 12].setStyleSheet("QFrame{\n"
                                                           "    background: rgb(255,0,0);\n"
                                                           "    border-radius: 5px;\n"
                                                           "}")

    def clickNext(self, e):
        if len(self.allProject) > 12 * (self.index + 1):
            self.hidenTable()
            self.index += 1

            def hover0(e):
                if self.clicked != 0 + self.index * 12:
                    self.listFrame[0 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover0(e):
                if self.clicked != 0:
                    self.listFrame[0 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def leave0(e):
                if self.clicked != 0:
                    self.listFrame[0 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(113, 113, 113);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover1(e):
                if self.clicked != 1:
                    self.listFrame[1 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def leave1(e):
                if self.clicked != 1:
                    self.listFrame[1 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(113, 113, 113);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover2(e):
                if self.clicked != 2:
                    self.listFrame[2 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def leave2(e):
                if self.clicked != 2:
                    self.listFrame[2 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(113, 113, 113);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover3(e):
                if self.clicked != 3:
                    self.listFrame[3 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def leave3(e):
                if self.clicked != 3 + self.index * 12:
                    self.listFrame[3 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(113, 113, 113);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover4(e):
                if self.clicked != 4:
                    self.listFrame[4 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def leave4(e):
                if self.clicked != 4:
                    self.listFrame[4 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(113, 113, 113);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover5(e):
                if self.clicked != 5:
                    self.listFrame[5 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def leave5(e):
                if self.clicked != 5:
                    self.listFrame[5 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(113, 113, 113);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover6(e):
                if self.clicked != 6:
                    self.listFrame[6 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def leave6(e):
                if self.clicked != 6:
                    self.listFrame[6 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(113, 113, 113);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover7(e):
                if self.clicked != 7:
                    self.listFrame[7 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def leave7(e):
                if self.clicked != 7:
                    self.listFrame[7 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(113, 113, 113);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover8(e):
                if self.clicked != 8:
                    self.listFrame[8 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def leave8(e):
                if self.clicked != 8:
                    self.listFrame[8 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(113, 113, 113);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover9(e):
                if self.clicked != 9:
                    self.listFrame[9 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(200, 200, 200);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def leave9(e):
                if self.clicked != 9:
                    self.listFrame[9 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                      "    background: rgb(113, 113, 113);\n"
                                                                      "    border-radius: 5px;\n"
                                                                      "}")

            def hover10(e):
                if self.clicked != 10:
                    self.listFrame[10 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                       "    background: rgb(200, 200, 200);\n"
                                                                       "    border-radius: 5px;\n"
                                                                       "}")

            def leave10(e):
                if self.clicked != 10:
                    self.listFrame[10 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                       "    background: rgb(113, 113, 113);\n"
                                                                       "    border-radius: 5px;\n"
                                                                       "}")

            def hover11(e):
                if self.clicked != 11:
                    self.listFrame[11 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                       "    background: rgb(200, 200, 200);\n"
                                                                       "    border-radius: 5px;\n"
                                                                       "}")

            def leave11(e):
                if self.clicked != 11:
                    self.listFrame[11 + self.index * 12].setStyleSheet("QFrame{\n"
                                                                       "    background: rgb(113, 113, 113);\n"
                                                                       "    border-radius: 5px;\n"
                                                                       "}")

            try:
                self.listFrame[0 + self.index * 12].enterEvent = hover0
                self.listFrame[0 + self.index * 12].leaveEvent = leave0

                self.listFrame[1 + self.index * 12].enterEvent = hover1
                self.listFrame[1 + self.index * 12].leaveEvent = leave1

                self.listFrame[2 + self.index * 12].enterEvent = hover2
                self.listFrame[2 + self.index * 12].leaveEvent = leave2

                self.listFrame[3 + self.index * 12].enterEvent = hover3
                self.listFrame[3 + self.index * 12].leaveEvent = leave3

                self.listFrame[4 + self.index * 12].enterEvent = hover4
                self.listFrame[4 + self.index * 12].leaveEvent = leave4
                self.listFrame[5 + self.index * 12].enterEvent = hover5
                self.listFrame[5 + self.index * 12].leaveEvent = leave5

                self.listFrame[6 + self.index * 12].enterEvent = hover6
                self.listFrame[6 + self.index * 12].leaveEvent = leave6

                self.listFrame[7 + self.index * 12].enterEvent = hover7
                self.listFrame[7 + self.index * 12].leaveEvent = leave7

                self.listFrame[8 + self.index * 12].enterEvent = hover8
                self.listFrame[8 + self.index * 12].leaveEvent = leave8

                self.listFrame[9 + self.index * 12].enterEvent = hover9
                self.listFrame[9 + self.index * 12].leaveEvent = leave9

                self.listFrame[10 + self.index * 12].enterEvent = hover10
                self.listFrame[10 + self.index * 12].leaveEvent = leave10

                self.listFrame[11 + self.index * 12].enterEvent = hover11
                self.listFrame[11 + self.index * 12].leaveEvent = leave11

            except:
                pass

            self.showTable()
            self.checkStatePrev()
            self.checkStateNext()
            self.loadTable()
            try:
                self.listFrame[0 + self.index * 12].mousePressEvent = self.click0
                self.listFrame[1 + self.index * 12].mousePressEvent = self.click1
                self.listFrame[2 + self.index * 12].mousePressEvent = self.click2
                self.listFrame[3 + self.index * 12].mousePressEvent = self.click3
                self.listFrame[4 + self.index * 12].mousePressEvent = self.click4
                self.listFrame[5 + self.index * 12].mousePressEvent = self.click5
                self.listFrame[6 + self.index * 12].mousePressEvent = self.click6
                self.listFrame[7 + self.index * 12].mousePressEvent = self.click7
                self.listFrame[8 + self.index * 12].mousePressEvent = self.click8
                self.listFrame[9 + self.index * 12].mousePressEvent = self.click9
                self.listFrame[10 + self.index * 12].mousePressEvent = self.click10
                self.listFrame[11 + self.index * 12].mousePressEvent = self.click11
            except:
                pass

    def clickPrev(self, e):
        if self.index != 0:
            self.hidenTable()
            self.index -= 1
            self.showTable()
            self.checkStatePrev()
            self.checkStateNext()
            self.loadTable()

    def hidenTable(self):
        for i in range(self.index * 12, self.checkNumber(), 1):
            self.listFrame[i].hide()
            self.listlabel1[i].hide()
            self.listlabel2[i].hide()

    def showTable(self):
        for i in range(self.index * 12, self.checkNumber(), 1):
            self.listFrame[i].show()
            self.listlabel1[i].show()
            self.listlabel2[i].show()

    def checkNumber(self):
        if len(self.allProject)  <= 12 * (self.index + 1):
            return len(self.allProject)
        else:
            return (self.index + 1) * 12

    def loadTable(self):
        for i in range(self.index * 12, self.checkNumber(), 1):
            x = 20 + i % 12 % 3 * 260
            y = 40 + i % 12 // 3 * 80
            self.listFrame[i].setGeometry(QtCore.QRect(x, y, 191, 51))
            self.listFrame[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.listFrame[i].setStyleSheet("QFrame{\n"
                                            "    background: rgb(113, 113, 113);\n"
                                            "    border-radius: 5px;\n"
                                            "}")
            self.listFrame[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.listFrame[i].setFrameShadow(QtWidgets.QFrame.Raised)
            self.listFrame[i].setObjectName("framel0")
            self.listlabel1[i].setGeometry(QtCore.QRect(20, 0, 55, 51))
            self.listlabel1[i].setText("")
            self.listlabel1[i].setPixmap(QtGui.QPixmap("images/folder - Copy.png"))
            self.listlabel1[i].setObjectName("label")
            self.listlabel2[i].setGeometry(QtCore.QRect(80, 10, 101, 31))
            self.listlabel2[i].setObjectName("label_2")

    def checkStatePrev(self):
        if self.index == 0:
            self.pushButton_3.setStyleSheet("QPushButton{\n"
                                            "    border: 2px solid rgb(74, 74, 74);\n"
                                            "    background: rgb(197, 197, 197);\n"
                                            "    border-radius:10px;\n"
                                            "    font-weight: 600;\n"
                                            "    font-size: 16px;\n"
                                            "color:white;\n"
                                            "}\n"
                                            "")
            self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        else:
            self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_3.setStyleSheet("QPushButton{\n"
                                            "    border: 2px solid rgb(74, 74, 74);\n"
                                            "    background: rgb(255, 0, 0);\n"
                                            "    border-radius:10px;\n"
                                            "    font-weight: 600;\n"
                                            "    font-size: 16px;\n"
                                            "color:white;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    color: black;\n"
                                            "}")

    def checkStateNext(self):
        if len(self.allProject) <= 12 * (self.index + 1):
            self.pushButton_4.setStyleSheet("QPushButton{\n"
                                            "    border: 2px solid rgb(74, 74, 74);\n"
                                            "    background: rgb(197, 197, 197);\n"
                                            "    border-radius:10px;\n"
                                            "    font-weight: 600;\n"
                                            "    font-size: 16px;\n"
                                            "color:white;\n"
                                            "}\n"
                                            "")
            self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        else:
            self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.pushButton_4.setStyleSheet("QPushButton{\n"
                                            "    border: 2px solid rgb(74, 74, 74);\n"
                                            "    background: rgb(255, 0, 0);\n"
                                            "    border-radius:10px;\n"
                                            "    font-weight: 600;\n"
                                            "    font-size: 16px;\n"
                                            "color:white;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    color: black;\n"
                                            "}")
    def checkStateClicked(self):
        if self.clicked != -1:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
    def getUrl(self):
        return self.allProject[self.clicked + self.index*12][1]