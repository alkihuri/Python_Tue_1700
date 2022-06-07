#pyqt 3.0 
# https://docs.google.com/presentation/d/14PsvFT_9wBGSXjAtZ1D0K909I5fUud2U4GPuVMDoypQ/edit#slide=id.p
# Caesar cipher

class View(QMainWindow)
def  init  (self,newController):
    super(View,self).__init__()
    self.controller = newController
    self.setGeometry(300,200,300,250)
    self.setWindowTitle("Ceasar Cipher")
    self.word       = self.CreateInputField("Word:",   25,25)
    self.resultField  = self.CreateInputField("Result:"   25,75)
    self.encryptBtn   = self.CreateInputField("Encrypt:"   25,125,self.encryptHandler)
    self.decryptBtn   = self.CreateInputField("Decrypt:"   25,175 self.decryptHandler)

def EncryptHandler(self):
    self.controller.SetWordToEncrypt(self.word.text())
    self.controller.DoCrypt()

def DecryptHandler(self):
    self.controller.SetWordToEncrypt(self.word.text())
    self.controller.DoDecrypt()

def CreateLabel(self,text,x,y):
    newLabel = QtWidgets.QLabel(self)
    newLabel.setText(text)
    newLabel.move(x,y)
    return newLabel

def CreateInputField(self,labelx,y):
    offsetForInputField = 50
    self.CreateLabel(label,x,y)
    line = QLineEdit(self)
    line.move(x+offsetForInputField, y)
    line.resize(200, 32)
    return line

def CreateButton(self,text,x,y,fun):
    newButton = QtWidgets.QPushButton(self)
    newButton.setText(text)
    newButton.resize(250, 32)
    newButton.move(x,y)
    newButton.clicked.connect(fun)
    newButton.clicked.connect(self.UpdateUI)
    return newButton

def UpdateUI(self):
    self.resultField.setText(myController.GetResult())

