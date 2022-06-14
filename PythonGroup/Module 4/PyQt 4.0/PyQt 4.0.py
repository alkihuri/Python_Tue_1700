#PyQt 4.0 
#work with files READ and WRITE
#presentation link https://docs.google.com/presentation/d/1bdxF5J2j9vmLCPbtVkgYI_0DsI1r05Yv_gwBHwv0ypk/edit?usp=sharing


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QComboBox 
import sys
import os 

class ReaderView(QMainWindow):
    def  init  (self,myViewModel):
        super(ReaderView,self).__init__()
        self.myViewModel = myViewModel
        self.setGeometry(0,0,600,600)
        self.setWindowTitle("Poem reader")
        self.poemSelectField = self.CreateComboBox("Poem:",   150,25)
        self.poemSelectField.addItems(["WILLIAM SHAKESPEAR","RUDYARD KIPLING"])
        sdlf.poemField = self.CreateLabel("POEM NOT LOADED",150,100)

def RequestPoem(self):
    self.poemString = self.myViewModel.SetPath(self.poemSelectField.currentText())
    self.UpdateUI()

def CreateLabel(self,text,x,y):
    newLabel = QtWidgets.QLabel(self)
    newLabel.setText(text)
    newLabel.move(x,y)
    return newLabel

def 

