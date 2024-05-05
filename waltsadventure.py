import pygame
import sys
import time
from pygame.locals import *

pygame.init()

### Variables ###
clock=pygame.time.Clock()
FPS=60
win_with=800
win_height=800
tile_size=40
game_over=0
main_menu=True

### Display ###
pygame.display.set_caption("Walt's Adventure")
screen=pygame.display.set_mode((win_with, win_height))
bground=pygame.image.load("assets/fonas.png").convert()
restart=pygame.image.load("assets/restart.png")
start_image=pygame.image.load("assets//start.png")
exit_image=pygame.image.load("assets/exit.png")
menubackground=pygame.image.load("assets/menubak.png").convert()
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

### Decorator ###
def button_decorator(func):
    def wrapper(self):
        action = False
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, self.rect)
        return action
    return wrapper

### Classes ###
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    @button_decorator
    def draw(self):
        pass


class Player():
### Singleton ##
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, x, y):
        if getattr(self, 'initialized', False):
            return
        self.reset(x, y)
        self.initialized = True
        
    def update(self, game_over):
        dx=0
        dy=0
        if game_over==0:
            key=pygame.key.get_pressed()
            if key[pygame.K_a]:
                dx-=5
                self.flipped=True  
            if key[pygame.K_d]:
                dx+=5
                self.flipped=False 
            
            if key[pygame.K_w] and self.jump==False:
                for tile in map.tile_list:
                    if tile[1].colliderect(self.rect.x, self.rect.y+1, self.rect.width, self.rect.height):
                        self.vel_y=-15
                        self.jump=True
                        break
            if key[pygame.K_w]==False: 
                self.jump=False

            self.vel_y+=1
            if self.vel_y>10:
                self.vel_y=10
            dy+=self.vel_y

            for tile in map.tile_list:
                if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.rect.width, self.rect.height):
                    dx=0
                if tile[1].colliderect(self.rect.x, self.rect.y+dy, self.rect.width, self.rect.height):
                    if self.vel_y<0:
                        dy=tile[1].bottom-self.rect.top
                        self.vel_y=0
                    elif self.vel_y>=0:
                        dy=tile[1].top-self.rect.bottom
                        self.vel_y=0
                if tile[1].colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                    self.jump=False
                    if self.vel_y>=0:
                        dy=tile[1].top-self.rect.bottom
                        self.vel_y=0
            if pygame.sprite.spritecollide(self, hank_group, False):
                game_over=-1
                
            if pygame.sprite.spritecollide(self, end_group, False):
                game_over=-2
                         
            self.rect.x+=dx
            self.rect.y+=dy
            
        if self.flipped:
            flipped_image = pygame.transform.flip(self.image, True, False)
            screen.blit(flipped_image, self.rect)
        else:
            screen.blit(self.image, self.rect)

        return game_over
    
    def reset(self, x, y):
        img=pygame.image.load("assets/walts.png")
        self.image=pygame.transform.scale(img, (40, 80))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.width=self.image.get_width()
        self.height=self.image.get_height()
        self.vel_y=0
        self.jump=False
        self.flipped=False  
       

class Map():
    def __init__(self, data):
        self.tile_list=[]

        dirt=pygame.image.load("assets/dirt.png")
        dirt2=pygame.image.load("assets/dirt2.png")
        dirt3=pygame.image.load("assets/dirt3.png")
        row_count=0

        for row in data:
            col_count=0
            for tile in row:
                if tile==1:
                    img=pygame.transform.scale(dirt, (tile_size, tile_size))
                    img_rect=img.get_rect()
                    img_rect.x=col_count*tile_size
                    img_rect.y=row_count*tile_size
                    tile=(img, img_rect)
                    self.tile_list.append(tile)
                if tile==2:
                    img=pygame.transform.scale(dirt2, (tile_size, tile_size))
                    img_rect=img.get_rect()
                    img_rect.x=col_count*tile_size
                    img_rect.y=row_count*tile_size
                    tile=(img, img_rect)
                    self.tile_list.append(tile)  
                if tile==3:
                    img=pygame.transform.scale(dirt3, (tile_size, tile_size))
                    img_rect=img.get_rect()
                    img_rect.x=col_count*tile_size
                    img_rect.y=row_count*tile_size
                    tile=(img, img_rect)
                    self.tile_list.append(tile)  
                if tile==4:
                    hank=Enemy(col_count*tile_size, row_count*tile_size-10)
                    hank_group.add(hank)
                if tile==5:
                    end=Exit(col_count*tile_size, row_count*tile_size+10)
                    end_group.add(end)
                   
                col_count+=1
            row_count+=1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            

### File reading ###
with open("assets/pasaulis.txt", "r") as file:
    map_content=file.read()
map_data=eval(map_content)

class Enemy(pygame.sprite.Sprite): #Inhereting from Sprite and using class as a form of encapsulation
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("assets/hank.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.direction=1
        self.counter=0
        #Overriding the update and __init__ method is the use of polymorphism
    def update(self):
        self.rect.x+=self.direction
        self.counter+=1
        if self.counter>30:
            self.direction*=-1
            self.counter*=-1

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("assets/end.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


### Main ###
player=Player(50, win_height-120)
hank_group=pygame.sprite.Group()
end_group=pygame.sprite.Group()
map=Map(map_data)
song = pygame.mixer.Sound("assets/bad.mp3")
restart_button=Button(win_with//2 - 70, win_height//2 +20, restart)
start_button=Button(win_with//2 - 70, win_height//2 - 50, start_image)
exit_button=Button(win_with//2 - 70, win_height//2 +20, exit_image)
song.set_volume(0.05)


### Game Loop ###
run=True
while run:
    clock.tick(FPS)
    screen.blit(bground, (0, 0))
    if main_menu==True:
        screen.blit(menubackground, (0, 0))
        if exit_button.draw():
            ### Printing into the file ###
            readable_time = time.ctime()
            with open('assets/output.txt', 'a') as file:
                file.write(f'Logged out of the game on {readable_time}\n')
            run=False
        if start_button.draw():
            main_menu=False
    else:
        map.draw()
        if game_over==0:
            hank_group.update()
        hank_group.draw(screen)
        end_group.draw(screen)
        game_over=player.update(game_over)
        if game_over==-1:
            if restart_button.draw():
                player.reset(50, win_height-120)
                game_over=0
        if game_over==-2:
            font=pygame.font.Font(None, 100)
            text=font.render("You Win", True, (255, 255, 255))
            screen.blit(text, (win_with//2-150, win_height//2-50))
            if exit_button.draw():
                ### Printing into the file ###
                readable_time = time.ctime()
                with open('assets/output.txt', 'a') as file:
                    file.write(f'Logged out of the game on {readable_time}\n')
                run=False
        
    song.play()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
