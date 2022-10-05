from PyQt5 import QtGui, QtWidgets, QtCore
import sys, os
import UIStart,UIMain,UIChooseFile
import processFile
import pyautogui
class UI:
    def __init__(self):
        self.ui = ""
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.URL = ""
    def __UIStart(self,e):
        self.ui = UIStart.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.frame_3.mousePressEvent = self.newFolder
        self.ui.frame_2.mousePressEvent = self.__UIChooseFile
        self.MainWindow.show()
    def __UIChooseFile(self,e):
        self.ui = UIChooseFile.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.pushButton.mousePressEvent = self.__UIStart
        self.ui.pushButton_2.mousePressEvent = self.__loadUIMain
        self.MainWindow.show()
    def __loadUIMain(self,event):
        self.__UIMain(self.ui.getUrl())
    def newFolder(self,e):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        if directory != "":
            processFile.saveNewProject(directory)
            s = directory + "/images.txt"
            f = open(s, 'w')
            f.write("Sailormiu")
            f.close()
            self.__UIMain(directory)
    def __UIMain(self,URL):
        self.ui = UIMain.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow,URL)
        self.MainWindow.show()
    def loop(self):
        self.__UIStart(self)
        sys.exit(self.app.exec_())
