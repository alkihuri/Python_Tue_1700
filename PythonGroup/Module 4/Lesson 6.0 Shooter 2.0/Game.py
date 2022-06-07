print("Robolab Python Pro Course / Shooter template project =) ")


# link for presentation => https://docs.google.com/presentation/d/1UkxfjWFpecW7BD-9ngFL7hs1fSykJnfQynp53x15_i8/edit#slide=id.g122dbdc220d_1_85


# modules import 
import pygame
import random
from os import path
#colors and window size set up
WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH = 480
HEIGHT = 600
FPS = 15 
# Window creating
pygame.init()
pygame.mixer.init()
window_size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Shooter 2nd lesson")
clock = pygame.time.Clock() 
# Game sprites 
img_dir = path.join(path.dirname(__file__),"img")
background = pygame.load(path.join(img_dir,"field.png")).convert()
background_rect = background.get_rect() 
player_img = pygame.load(path.join(img_dir,"field.png")).convert()
npc_img = pygame.load(path.join(img_dir,"npc.png")).convert()
bullet_img = pygame.load(path.join(img_dir,"bullet.png")).convert()

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_size = (50,50)
        self.image = pygame.transform.scale(player_img,player_size)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH /2
        self.rect.bottom = HEIGHT - player_size.x
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keysate = pygame.key.get_pressed()
        if keysate[pygame.K_LEFT]:
            self.speedx = -8 
        if keysate[pygame.K_RIGHT]:
            self.speedx = 8   
        self.rect.x += self.speedx
    #shoot mechanic function


#mob generation system ~ mob (NPC) class
    class Mob(pygame.sprite.Sprite):
        def _init_(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(npc_img , (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-300, -30)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if select.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
#mob generation system ~ generation

#Game lifecycle
running = True
While running:
    #fps
    clock.tick(FPS)
    #event handler
    for event in pygame.event.get():
        #event to close window
        if event.type == pygame.QUIT
        running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE
        #shoot [if event.type == pygame.KEYDOWN] [if event.key == pygame.K_SPACE]

    #update of render

    #screen flip

class Hero(pygame.sprite.Sprite):
    def _init_(self, filename, x_speed=0, y_speed=0, x=x_start, y=y_start, width=120, height=120):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.transform.scale(pygame.imsge.load(filename), (width, height)) .convert_alpha()
        self.rect = self.image.get.rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.stands_on = False

def gravitate(self):
    self.y_speed += 0.25
    def jump(self, y):
        if self.stands_on:
            self.y_speed = y

def update(self):
    self.rect.x += self.x_speed
    platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
    if self.x_speed > 0:
        for p in platforms_touched:
            self.rect.right = min(self.rect.right, p.rect.left)
            elif self.x_speed < 0:
                for p in platforms_touched:
                    self.rect.left = max(self.rect.left, p.rect.right)
                    self.gravitate()
                    self.rect.y += self.y_speed
                    platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
                    if self.y_speed > 0:
                        for p in platforms_touched:
                            self.y_speed = 0
                            if p.rect.top < self.rect.bottom:
                                self.rect.bottom = p.rect.top
                                self.stands_on = p
                            elif self.y_speed < 0:
                                self.stands_on = False
                                for p in platforms_touched:
                                    self.y_speed = 0
                                    self.rect.top = max(self.rect.top, p.rect.bottom)

class Enenmy(pygame.sprite.Sprite):
    def_init_(self, x=20, y=0, filename=img_file_enemy, width=100, height=100):
    pygame.sprite.Sprite_init_(self)
    self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)) .convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    def update(self):
        self.rect.x += randint(-5, 5)
        self.rect.y += randint(-5, 5)

        class Wall(pygame.sprite.Sprite)
        def_init_(self, x=20, y=0, height=120, width=120, colour=C_BLUE):
        pygame.sprite.Sprite_init_(self)
        self.image = pygame.surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

class FinalSprite(pygame.sprite.Sprite):
    def_init_(self, player_image, player_x, player_y, player_speed):
    pygame.sprite.Sprite._init_(self)
    self.image = pygame.transform.scale(pygame.image.load(player_image), (60, 120))
    self.speed = player_speed
    self.rect = self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y

 


 






 