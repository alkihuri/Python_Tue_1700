import pygame
from pygame import *
import keyboard
from os import *

window = display.set_mode((400, 640))
window = display.set_caption('ShooterGame')

img_dir = path.join(path.dirname(__file__), 'img') 
spaceShip_img = pygame.image.load(path.join(img_dir, "ship.png")).convert() 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(spaceShip_img, (50, 38))
        self.rect = self.image.get_rect()
        self.speedx = 0
    def update(self):
        if keyboard.is_pressed('a'):
            print('a')
            speedx += -8
        if keyboard.is_pressed('d'):
            print('d')
            speedx += 8

        self.rect.x += self.speedx 

player = Player()
 

running = True
while running:

    for eachEvents in event.get():
        if eachEvents.type == QUIT:
            running = False


 