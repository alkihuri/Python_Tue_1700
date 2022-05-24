#pyqt 1.0 
# https://docs.google.com/presentation/d/1gqyMy49e3D3A0E9ACEwZGh825fAHHC7Q8yT97-nw4Qw/edit?usp=sharing
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.counter = 0
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Counter")
        self.CreateLabel("0",100,100)
        self.CreateButton("Click!",100,150,self.CounterFunc)

    def CreateLabel(self,text,x=50,y=50):
        self.newLabel = QtWidgets.QLabel(self)
        self.newLabel.setText("0")
        self.newLabel.move(25,25)

    def CreateButton(self,text,x,y,fun):
        self.newButton = QtWidgets.QPushButton(self)
        self.newButton.setText("Button")
        self.newButton.move(25,125)
        self.newButton.clicked.connect(self.CounterFunc)

    def CounterFunc(self):
        self.counter +=1
        self.newLabel.setText(str(self.counter))

app = QApplication(sys.argv)
window  = MyWindow()
window.show()
sys.exit(app.exec_())