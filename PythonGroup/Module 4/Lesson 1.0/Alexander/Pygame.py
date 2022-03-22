class Player():  
    def __init__(self):
        self.weapon = Weapon("pistol")  

    weapon = ""
    level = 0 
    nick = ""


class Weapon():  
    def __init__(self, name):
        self.hold = name  

    hold = ""
    num =0  
    bullets = 0
    bulletType = ""


class Database():
    playerList = []





player = Player()
player.nick = "Jovan"
player.weapon = Weapon("Shotgun") 
player.level = (30)

