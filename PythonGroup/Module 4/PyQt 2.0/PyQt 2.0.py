#pyqt 1.0 
# https://docs.google.com/presentation/d/1yKphcke3fU9ngtN5ob5EMkL-21DzqxBD5uNaZNJwhWo/edit?usp=sharing
#calculator
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel, QLineEdit
import sys

class MyWindow(QMainWindow):
   def __init__ (self):
      super(MyWindow,self).__init__()                                         # innit super class
      self.setGeometry(400,200,400,300)                                       # size of window
      self.setWindowTitle("Calculator")
      # input fields
      self.aField         = self.CreateInputField("a:",100,25)
      self.bField         = self.CreateInputField("b:",100,50)
      self.resultField    = self.CreateLabel("Result:",50,100)
      # Math operations buttons
      self.plusBtn        = self.CreateButton("+",100,150,self.Plus)
      self.minusBtn       = self.CreateButton("-",100,175,self.Minus)
      self.multiplyBtn    = self.CreateButton("*",100,200,self.Multiply)
      self.divideBtn      = self.CreateButton("/",100,225,self.Divide)
      self.powerBtn      = self.CreateButton("**",100,250,self.Power)

   
      self.OneBtn      = self.CreateButton("1",200,250,self.OneBtnFunc)
      self.TwoBtn      = self.CreateButton("2",200,225,self.TwoBtnFunc)


      # resetting of start values
      self.a = 0                                                             
      self.b = 0
      self.result = 0

   def CreateLabel(self,text,x,y):
        newLabel = QtWidgets.QLabel(self)
        newLabel.setText(text)
        newLabel.move(x,y)
        return newLabel

   def CreateInputField(self,label,x,y):
       self.CreateLabel(label,x-50,y)
       line = QLineEdit(self)
       line.move(x, y)
       line.resize(200, 32)
       return line

   def CreateButton(self,text,x,y,fun):
       newButton = QtWidgets.QPushButton(self)
       newButton.setText(text)
       newButton.move(x,y)
       newButton.clicked.connect(fun)
       return newButton

   def UpdateInput(self):
      try:
         self.a =  float(self.aField.text())
      except:
         self.a = 0
      try:
         self.b =  float(self.bField.text())
      except:
         self.b = 0

   def UpdateOutput(self):   
      self.resultField.setText("Result : " + str(self.result))

   def Plus(self):
      self.UpdateInput()
      self.result =  self.a + self.b
      self.UpdateOutput()

   def Minus(self):
      self.UpdateInput()
      self.result =  self.a - self.b
      self.UpdateOutput()

   def Multiply(self):
      self.UpdateInput()
      self.result =  self.a * self.b
      self.UpdateOutput()

   def Divide(self):
      self.UpdateInput()
      self.result =  self.a / self.b
      self.UpdateOutput()

   def Power(self):
      self.UpdateInput()
      self.result =  self.a ** self.b
      self.UpdateOutput()
   
   def OneBtnFunc(self): 
      self.UpdateInput()
      prevValue = int(self.a) 
      newValue = str(prevValue) + str(1)
      self.aField.setText(str(newValue))

   def TwoBtnFunc(self): 
         self.UpdateInput()
         prevValue = int(self.a) 
         newValue = str(prevValue) + str(2)
         self.aField.setText(str(newValue))

app = QApplication(sys.argv)
window  = MyWindow()
window.show()
sys.exit(app.exec_())



