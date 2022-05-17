# Подключить нужные модули
from random import randint 
import pygame 
from os import path
pygame.init() 
# during the game we write the inscriptions of the size 72
font = pygame.font.Font(None, 72)
#Global variables (settings)
win_width = 800
win_height = 600
# boundaries beyond which the character does not go (the background starts to go)
left_bound = win_width / 40            
right_bound = win_width - 8 * left_bound
shift = 0
x_start, y_start = 20, 10 
img_file_back =     path.dirname(__file__)+ '/cave.png'
img_file_hero =     path.dirname(__file__)+ '/m1.png'
img_file_enemy =    path.dirname(__file__)+ '/enemy.png'
img_file_bomb =     path.dirname(__file__)+ '/bomb.png'
img_file_princess = path.dirname(__file__)+ '/princess.png'
FPS = 60 
# colors:
C_WHITE = (255, 255, 255)
C_DARK = (48, 48, 0)
C_YELLOW = (255, 255, 87)
C_GREEN = (32, 128, 32)
C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)
# Game launch
pygame.display.set_caption("ARCADA")
window = pygame.display.set_mode([win_width, win_height])
back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height))

# Классы
# класс для цели (стоит и ничего не делает)

  # конструктор класса
   
      # Вызываем конструктор класса (Sprite):
       

      # каждый спрайт должен хранить свойство image - изображение 

      # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан 

#класс для главного героя     
 class Hero(pygame.sprite.Sprite):
   def __init__(self, filename, x_speed=0, y_speed=0, x=x_start, y=y_start, width=120, height=120):
       pygame.sprite.Sprite.__init__(self)
       # the picture is loaded from a file and includes proteins of the required sizes:
       self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha()
                   # use convert_alpha, we need to keep transparency
       # each sprite must store a rect property - a rectangle. This property is needed to determine the touches of sprites.
       self.rect = self.image.get_rect()
       # put the character at the given point (x, y):
       self.rect.x = x
       self.rect.y = y
       # create properties, remember the passed values:
       self.x_speed = x_speed
       self.y_speed = y_speed
       # add the stands_on property - this is the platform on which the character stands
       self.stands_on = False # if none, then the value is False

       




        # картинка загружается из файла и умещается в прямоугольник нужных размеров:
         
                    # используем convert_alpha, нам надо сохранять прозрачность

        # каждый спрайт должен хранить свойство rect - прямоугольник. Это свойство нужно для определения касаний спрайтов. 
        
        # ставим персонажа в переданную точку (x, y):
         
        # создаем свойства, запоминаем переданные значения:
         
        # добавим свойство stands_on - это та платформа, на которой стоит персонаж
        
        # если ни на какой не стоит, то значение - False
    #функция для падения (гравитация)  
      def gravitate(self):
       self.y_speed += 0.25

def jump(self, y):
       if self.stands_on:
           self.y_speed = y


    #функция для прыжка

    #функция апдейт для данного спрайта. так как спрайт будет премещаться. Самая веселая часть ) 
     

#класс для стены. Делали точно такой же в проекте Лабиринт :))) 
    #конструктор
#sprites 
# list of all characters in the game:
all_sprites = pygame.sprite.Group()
#list of obstacles:
barriers = pygame.sprite.Group()
# list of enemies:
enemies = pygame.sprite.Group()
# min list:
bombs = pygame.sprite.Group()
# create a character, add it to the list of all sprites:
robin = Hero(img_file_hero)
all_sprites.add(robin)
# create walls, add them:
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

#класс врага 
# create enemies, add them:
en = Enemy(50, 480)
all_sprites.add(en)
enemies.add(en)

en = Enemy(400, 480)
all_sprites.add(en)
enemies.add(en)

# create mines, add them:
bomb = Enemy(550, 520, img_file_bomb, 60, 60)
bombs.add(bomb) # do not add bombs to the list of all sprites, we will draw them with a separate command
               # we can detonate bombs so easily, and also make them immobile, update() is not called

# create the final sprite, add it:
pr = FinalSprite(img_file_princess, win_width + 500, win_height - 150, 0)
all_sprites.add(pr)

class Enemy(pygame.sprite.Sprite): # enemy
   def __init__(self, x=20, y=0, filename=img_file_enemy, width=100, height=100):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

   def update(self):
       ''' moves the character using the current horizontal and vertical speed'''
       self.rect.x += randint(-5, 5)
       self.rect.y += randint(-5, 5)


    #конструктор 

    # функция апдейт с рандомным перемещением 
          def update(self):
       '''' moves the character using the current horizontal and vertical speed'''
      # move horizontally first
       self.rect.x += self.x_speed
       # # if we went behind the wall, then we will stand close to the wall
       platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
       if self.x_speed > 0: # we go to the right, the right edge of the character is close to the left edge of the wall
           for p in platforms_touched:
               self.rect.right = min(self.rect.right, p.rect.left) # if they touched several at once, then the right edge is the minimum possible
       elif self.x_speed < 0: # go left, put the left edge of the character close to the right edge of the wall
           for p in platforms_touched:
               self.rect.left = max(self.rect.left, p.rect.right) # if several walls are touched, then the left edge is the maximum
       # now moving vertically      
       self.gravitate()
       self.rect.y += self.y_speed
       # if we went behind the wall, then we will stand close to the wall
       platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
       if self.y_speed > 0: # go down
           for p in platforms_touched:
               self.y_speed = 0
               # We check which of the platforms below is the highest, align with it, remember it as our support:
               if p.rect.top < self.rect.bottom:
                   self.rect.bottom = p.rect.top
                   self.stands_on = p
       elif self.y_speed < 0: # go up
           self.stands_on = False #  so we're not standing on anything!
           for p in platforms_touched:
               self.y_speed = 0  # when colliding with a wall, the vertical speed is extinguished
               self.rect.top = max(self.rect.top, p.rect.bottom) # align the top edge with the bottom edges of the walls that were run over


# Запуск игры 


# список всех персонажей игры:


# список препятствий:

# список врагов:

# список мин:


# создаем персонажа, добавляем его в список всех спрайтов:

# создаем стены, добавляем их:
class Wall(pygame.sprite.Sprite):
   def __init__(self, x=20, y=0, width=120, height=120, color=C_GREEN):
       pygame.sprite.Sprite.__init__(self)
       # picture - a new rectangle of the required dimensions:
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # create property rect
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y




# создаем врагов, добавляем их:


# создаем мины, добавляем их:
            
            # в список всех спрайтов бомбы не добавляем, будем рисовать их отдельной командой
            # так легко сможем подрывать бомбы, а также делаем их неподвижными, update() не вызывается

# создаем финальный спрайт, добавляем его: 

#class for target (costs and does nothing)
class FinalSprite(pygame.sprite.Sprite):
 # constructor 
 def __init__(self, player_image, player_x, player_y, player_speed):
     # Call  the class constructor (Sprite):
     pygame.sprite.Sprite.__init__(self)

     # each sprite must store an image property - an image
     self.image = pygame.transform.scale(pygame.image.load(player_image), (60, 120))
     self.speed = player_speed

     # each sprite must store the property rect - the rectangle in which it is inscribed
     self.rect = self.image.get_rect()
     self.rect.x = player_x
     self.rect.y = player_y

# Main game loop:
run = True
finished = False

while run:
   # Event Handling
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
               robin.x_speed = -5
           elif event.key == pygame.K_RIGHT:
               robin.x_speed = 5
           elif event.key == pygame.K_UP:
               robin.jump(-7)

       elif event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT:
               robin.x_speed = 0
           elif event.key == pygame.K_RIGHT:
               robin.x_speed = 0
               if not finished:
       # Moving Game Objects
       all_sprites.update()

       # beyond checking the rules of the game
       # check touch with bombs:
       pygame.sprite.groupcollide(bombs, all_sprites, True, True)
               # if the bomb touches the sprite, then it is removed from the list of bombs, and the sprite is removed from all_sprites!

       # check the touch of the hero with the enemies:
       if pygame.sprite.spritecollide(robin, enemies, False):
           robin.kill() # the kill method removes the sprite from all groups in which it is listed

       # check screen borders:
       if (
           robin.rect.x > right_bound and robin.x_speed > 0
           or
           robin.rect.x < left_bound and robin.x_speed < 0
       ): # when exiting to the left or right, we transfer the change to the screen shift
           shift -= robin.x_speed 
           # move all the sprites to a common shift (and separately the bombs, they are in another list):
           for s in all_sprites:
               s.rect.x -= robin.x_speed # robin himself is also in this list, so his movement will be visually canceled
           for s in bombs:
               s.rect.x -= robin.x_speed
               # Rendering
       # draw the background with a shift
       local_shift = shift % win_width
       window.blit(back, (local_shift, 0))
       if local_shift != 0:
           window.blit(back, (local_shift - win_width, 0))

       # draw all sprites on the screen surface before checking for win/loss
       # if the game ended in this iteration of the loop, then a new background will be drawn on top of the characters
       all_sprites.draw(window) 
       # we draw a group of bombs separately - so a bomb that has left its group will automatically cease to be visible
       bombs.draw(window)

       # check for win and loss:
       if pygame.sprite.collide_rect(robin, pr):
           finished = True
           window.fill(C_BLACK)
           # write text on the screen
           text = font.render("YOU WIN!", 1, C_RED)
           window.blit(text, (250, 250))

       # check for loss:
       if robin not in all_sprites or robin.rect.top > win_height:
           finished = True           
           window.fill(C_BLACK)
           # write text on the screen
           text = font.render("GAME OVER", 1, C_RED)
           window.blit(text, (250, 250))

   pygame.display.update()

   # Pause
   pygame.time.delay(20)





 
    # Обработка событий
      
        # Перемещение игровых объектов  

        # дальше проверки правил игры
        # проверяем касание с бомбами: 
                # если бомба коснулась спрайта, то она убирается из списка бомб, а спрайт - из all_sprites!

        # проверяем касание героя с врагами: 
           # robin.kill() # метод kill убирает спрайт из всех групп, в которых он числится

        # проверяем границы экрана: 
             # при выходе влево или вправо переносим изменение в сдвиг экрана 
            # перемещаем на общий сдвиг все спрайты (и отдельно бомбы, они ж в другом списке): 
                        # сам robin тоже в этом списке, поэтому его перемещение визуально отменится
            

        # Отрисовка
        # рисуем фон со сдвигом
        

        # нарисуем все спрайты на экранной поверхности до проверки на выигрыш/проигрыш
        # если в этой итерации цикла игра закончилась, то новый фон отрисуется поверх персонажей
         
        # группу бомб рисуем отдельно - так бомба, которая ушла из своей группы, автоматически перестанет быть видимой
       

        # проверка на выигрыш и на проигрыш:
        

        # проверка на проигрыш:
         
            # пишем текст на экране
             

     

    # Пауза 