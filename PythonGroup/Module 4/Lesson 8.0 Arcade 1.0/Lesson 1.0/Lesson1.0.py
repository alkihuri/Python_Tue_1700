from random import randint
from sre_constants import JUMP 
import pygame 
from os import path
import keyboard
pygame.init() 

C_GREEN = (32, 128, 32)

x_start, y_start = 20, 10

img_file_back =     path.dirname(__file__)+ '/cave.png'
img_file_hero =     path.dirname(__file__)+ '/m1.png'
img_file_enemy =    path.dirname(__file__)+ '/enemy.png' 
img_file_bomb =     path.dirname(__file__)+ '/bomb.png'
img_file_princess = path.dirname(__file__)+ '/princess.png'

pygame.display.set_caption("ARCADE") 
window = pygame.display.set_mode((800, 600))

class Hero(pygame.sprite.Sprite):
   def __init__(self, filename, x_speed=0, y_speed=0, x=x_start, y=y_start):
       pygame.sprite.Sprite.__init__(self)
       
       self.image = pygame.transform.scale(pygame.image.load(filename), (120, 120)).convert_alpha()
                   
      
       self.rect = self.image.get_rect()
       
       self.rect.x = x
       self.rect.y = y
       
       self.x_speed = x_speed
       self.y_speed = y_speed
       
       self.stands_on = False

   def gravity(self):
       self.y_speed += 0.25
    
   def jump(self):
       if self.stands_on:
           self.y_speed = 0
    
   def update(self):
       
       self.rect.x += self.x_speed
       self.rect.y += self.y_speed
       
       platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
       if self.x_speed > 0:
           for p in platforms_touched:
               self.rect.right = min(self.rect.right, p.rect.left)
       elif self.x_speed < 0: 
           for p in platforms_touched:
               self.rect.left = max(self.rect.left, p.rect.right)
        
       self.gravity()

       if self.y_speed > 0: 
           for p in platforms_touched:
               self.y_speed = 0

               if p.rect.top < self.rect.bottom:
                   self.rect.bottom = p.rect.top
                   self.stands_on = p

       if keyboard.is_pressed('a'):
           self.rect.x += 0.5
       elif keyboard.is_pressed('d'):
           self.rect.x -= 0.5
        
       if keyboard.is_pressed('space'):
           self.jump()

class Enemy(pygame.sprite.Sprite): 
   def __init__(self, x=20, y=0, filename=img_file_enemy, width=100, height=100):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

   def update(self):
       self.rect.x = randint(5, -5)
       self.rect.y = randint(5, -5)

class Wall(pygame.sprite.Sprite):
   def __init__(self, x=20, y=0, width=120, height=120, color=C_GREEN):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # create property rect
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       
class FinalSprite(pygame.sprite.Sprite):
  
 def __init__(self, player_image, player_x, player_y, player_speed):
     
     pygame.sprite.Sprite.__init__(self)

     
     self.image = pygame.transform.scale(pygame.image.load(player_image), (60, 120))
     self.speed = player_speed

     
     self.rect = self.image.get_rect()
     self.rect.x = player_x
     self.rect.y = player_y

all_sprites = pygame.sprite.Group()

barriers = pygame.sprite.Group()

enemies = pygame.sprite.Group()

w = Wall(50, 150, 480, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(700, 50, 50, 360) 
barriers.add(w)
all_sprites.add(w)
w = Wall(350, 380, 640, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(-200, 590, 1600, 20)
barriers.add(w)
all_sprites.add(w)

run = True
while run:
    all_sprites.update()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False 





