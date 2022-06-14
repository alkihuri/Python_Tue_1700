from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QComboBox 
import sys
import os 

class ReaderView(QMainWindow):   
    def __init__(self):
        super(ReaderView,self).__init__()                        
        self.setGeometry(0,0,600,600)                                        
        self.setWindowTitle("Poem reader")
        self.poemSelectField = self.CreateComboBox("Poem:",    150,25)    
        self.poemSelectField.addItems(["WILLIAM SHAKESPEARE","RUDYARD KIPLING"])
        self.poemField = self.CreateLabel("POEM NOT LOADED",150,100)  
   
    def CreateLabel(self,text,x,y):
        newLabel = QtWidgets.QLabel(self)
        newLabel.setText(text)
        newLabel.move(x,y)
        return newLabel 
    
    def CreateComboBox(self,label,x,y):
        self.CreateLabel(label,x,y)
        combo = QComboBox(self)
        combo.move(x+50, y)
        combo.resize(200, 32)
        combo.activated[str].connect(self.WriteShake)   
        return combo
    
    def WriteShake(self):
        poem = ["Let me not to the marriage of true minds\n"
        ,"Admit impediments. Love is not love\n"
        ,"Which alters when it alteration finds,\n"
        ,"Or bends with the remover to remove.\n"]

        currentFilePath     = os.path.dirname(__file__)      
        newpoemFilePath = currentFilePath + "/WILLIAM SHAKESPEARE.txt"
        f = open(newpoemFilePath,"w")
        f.writelines(poem) 

    def WriteKip(self):
        KipPoem = ["If you can keep your head when all about you \n",
        "Are losing theirs and blaming it on you, \n",
        "If you can trust yourself when all men doubt you, \n",
        "But make allowance for their doubting too; \n",
        "If you can wait and not be tired by waiting, \n",
        "Or being lied about, don't deal in lies, \n",
        "Or being hated, don't give way to hating, \n",
        "And yet don't look too good, nor talk too wise. \n"]

        self.poemField.resize(500, 25 * len(KipPoem))
        self.poemField.setText(''.join(KipPoem))

app = QApplication(sys.argv)   
myView = ReaderView()
myView.show()
sys.exit(app.exec_())

    

