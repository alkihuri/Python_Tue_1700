print("Robolab Python Pro Course / Shooter template project =) ")


# link for presentation => https://docs.google.com/presentation/d/1UkxfjWFpecW7BD-9ngFL7hs1fSykJnfQynp53x15_i8/edit#slide=id.g122dbdc220d_1_85


# modules import 
import pygame
import random
from os import path
#colors and window size set up
WHITE = (255,255,255)
BLACK = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Yellow = (255,255,0)
WIDTH = 480
HEIGHT = 600
FPS = 30 
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
    score = 0
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
#Game entities innit
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(2):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    #shoot mechanic function
def shoot(self):
    bullet = Bullet(self.rect.centrex,self.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)
    hits = pygame.sprite.groupcolide(mobs,bullets,True,True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        hits = pygame.sprite.spritecollide(player,mobs,|False)
        if hits:
            running = False
        

#mob generation system ~ mob (NPC) class
self.rect.x = random.radrange(WIDTH - self.rect.width)
self.rect.y = random.randrange(-300,-30)
self.speedy = randeom.randrange(-3,3)

def update(self)
self.rect.x += self.speedx
self.rect.x += self.speedy
if self.rect.top > Height +10 or self.rect.left < -25 or self.rect.right >WIDTH + 20:
    self.rect.x = random.randrange(WIDTH - self.rect.width)
    self.rect.y = random.randrange (-100,-40)
    self.speedy = random.randrange (1,8)
#mob generation system ~ generation

#Game lifecycle
running = True 
while running:
    #fps
clock.tick(FPS)
    #event handler
for event.type == -pygame.QUIT:
        #event to close window
        if event.type == pygame.QUIT:
            running = False
            elif event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    player.shoot()
        #shoot [if event.type == pygame.KEYDOWN] [if event.key == pygame.K_SPACE]

    #update of render
 all_sprites.update()
 screen.fill(BLACK)
 screen.bliy(background,background_rect)
 all_spriyes.draw(screen)

 hits - pygame.sprite.groupcolide(mobs,bullets,True,True)
 for hit in hits:
     player.score+-1
     print(player.score)
     m = Mob()
     all_sprites.add(m)
     mobs.add(m)
    #screen flip
pygame.display.flip()

 pygame.quit


 






 

 