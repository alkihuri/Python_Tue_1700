#pyqt 1.0 
# https://docs.google.com/presentation/d/1yKphcke3fU9ngtN5ob5EMkL-21DzqxBD5uNaZNJwhWo/edit?usp=sharing
#calculator

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel
QLineEdit
import sys
class MyWindow(QMainWindow)
def  init  (self):
    super(MyWindow,self).  init  ()
    self.setGeometry(200,200,300,300)
    self.setWindowTitle("Calculator")
    self.aField     = self.CreateInputField("a:",100,25)
    self.bField     = self.CreateInputField("b:",100,50)
    self.resultField    = self.CreateLabel("Result",50,100)
    self.plusBtn    = self.CreateButton("+",100,150,self.Plus)
    self.minusBtn   = self.CreateButton("-",100,175,self.Minus
    self.multiplyBtn    = self.CreateButton("*",100,200,self.Multiply)
    self.divideBtn  = self.CreateButton("/",100,225,self.Divide)
    self.a = 0
    self.b = 0
    self.result = 0

