from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class myWindow(QMainWindow):

    def __init__(self):
        super(myWindow,self).__init__()
        self.counter = 0
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Counter")
        self.CreateLabel(str(self.counter))
        self.CreateButton('Click', self.Func_Counter, 100, 150)
        self.CreateButton('Minus', self.Func_Minus, 100, 180) 
        self.CreateButton('Erase', self.Func_Erase, 100, 210)

    def CreateLabel(self, text, x=150, y=50):
        self.newLabel = QtWidgets.QLabel(self)
        self.newLabel.setText(text)
        self.newLabel.move(x, y)

    def CreateButton(self, text, func, x, y):
        self.newButton = QtWidgets.QPushButton(self)
        self.newButton.setText(text)
        self.newButton.move(x, y)
        self.newButton.clicked.connect(func)
    
    def Func_Counter(self):
        self.counter += 1
        self.newLabel.setText(str(self.counter))
    
    def Func_Minus(self):
        self.counter -= 1
        self.newLabel.setText(str(self.counter))
    
    def Func_Erase(self):
        self.counter = 0
        self.newLabel.setText(str(self.counter))
    
    
        

app = QApplication(sys.argv)
window = myWindow()
window.show()
sys.exit(app.exec_())
