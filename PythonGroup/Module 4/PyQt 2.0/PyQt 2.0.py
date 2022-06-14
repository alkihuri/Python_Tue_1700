from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel, QLineEdit
import sys

running = True

class AdvWindow(QMainWindow):
    def __init__(self):
        super(AdvWindow,self).__init__()
        self.setGeometry(200,200,300,300)

        self.CreateInput(150, 100)

        self.CreateLabel('0', 150, 150)

        self.CreateButton('+', 150, 175, self.Power)
        

    def CreateButton(self, text, x, y, func):
        newButton = QtWidgets.QPushButton(self)
        newButton.setText(text)
        newButton.move(x, y)
        newButton.clicked.connect(func)
        return newButton

    def CreateLabel(self, text, x, y):
        newLabel = QtWidgets.QLabel(self)
        newLabel.setText(text)
        newLabel.move(x, y)
        return newLabel

    def CreateInput(self, x, y):
        line = QLineEdit(self)
        line.move(x, y)
        line.resize(200, 32)
        return line

    def Power(self):
        pass


class CalcWindow(QMainWindow):
    def __init__(self):
        super(CalcWindow,self).__init__()
        self.setGeometry(200,200,300,300)

        self.inputA = self.CreateInput(50, 50)
        self.inputB = self.CreateInput(50, 100)

        self.result = self.CreateLabel('0', 150, 125)

        self.Plus = self.CreateButton('+', 100, 150, self.Plus)
        self.Minus = self.CreateButton('-', 100, 175, self.Minus)
        self.Multi = self.CreateButton('*', 100, 200, self.Multi)
        self.Div = self.CreateButton('/', 100, 225, self.Div)

        self.OpenWindow = self.CreateButton('Adv Window', 100, 250, self.NewWindow)

               

        
    def CreateButton(self, text, x, y, func):
        newButton = QtWidgets.QPushButton(self)
        newButton.setText(text)
        newButton.move(x, y)
        newButton.clicked.connect(func)
        return newButton

    def CreateLabel(self, text, x, y):
        newLabel = QtWidgets.QLabel(self)
        newLabel.setText(text)
        newLabel.move(x, y)
        return newLabel

    def CreateInput(self, x, y):
        line = QLineEdit(self)
        line.move(x, y)
        line.resize(200, 32)
        return line


    def Plus(self):
        result = float(self.inputA.text()) + float(self.inputB.text())
        self.result.setText(str(result))
    
    def Minus(self):
        result = float(self.inputA.text()) - float(self.inputB.text())
        self.result.setText(str(result))
    
    def Multi(self):
        result = float(self.inputA.text()) * float(self.inputB.text())
        self.result.setText(str(result))
    
    def Div(self):
        result = float(self.inputA.text()) / float(self.inputB.text())
        self.result.setText(str(result))

    def NewWindow(self):
        app2 = QApplication(sys.argv)
        window2 = AdvWindow()
        window2.show()
        sys.exit(app2.exec_())







app = QApplication(sys.argv)
window  = CalcWindow()
window.show()
sys.exit(app.exec_())

    


    


