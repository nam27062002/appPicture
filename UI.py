from PyQt5 import QtGui, QtWidgets, QtCore
import sys, os
import UIstart, UIchooseFile,UIMain
import  processFile
class UI:
    def __init__(self):
        self.ui = ""
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.URL = ""
    def __UIstart(self, e):
        self.ui = UIstart.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.frame_2.mousePressEvent = self.__UIchooseFile
        self.ui.frame_3.mousePressEvent = self.newFolder
        self.MainWindow.show()
    def newFolder(self,e):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        if directory != "":
            processFile.saveNewProject(directory)
            s = directory + "/user.txt"
            f = open(s, 'w')
            f.close()
            self.__UIMain(directory)
    def __UIchooseFile(self,e):
        self.ui = UIchooseFile.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.pushButton.mousePressEvent = self.__UIstart
        self.ui.pushButton_2.mousePressEvent = self.__getURL
        self.MainWindow.show()
    def __UIMain(self,URL):
        self.URL = URL
        if URL != "":
            self.ui = UIMain.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow,self.URL)
            self.MainWindow.show()
    def __getURL(self,e):
        self.__UIMain(self.ui.getUrl())
    def loop(self):
        self.__UIstart(self)
        sys.exit(self.app.exec_())