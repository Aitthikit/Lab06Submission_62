import sys 
import pygame as pg
class Rectangle:
    def __init__(self,r=0,g=0,b=0,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = r
        self.g = g
        self.b = b
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    def __init__(self,r=0,g=0,b=0, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self,r,g,b, x, y, w, h)
    
    def isMouseOn(self):
        tf = []
        for a,b in zip(pg.mouse.get_pos(),(self.x,self.y)):
            if (a >= b) :
                tf.append(True)
            else:
                tf.append(False)
        for a,b in zip(pg.mouse.get_pos(),(self.x+self.w,self.y+self.h)):
            if (a <= b) :
                tf.append(True)
            else:
                tf.append(False)
        for i in tf:
            if i == False:
                return False
        return True 
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(255,0,0,20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา
while(run):
    screen.fill((255, 255, 255))
    print(pg.mouse.get_pressed())
    if btn.isMouseOn():
        if pg.mouse.get_pressed(num_buttons=3) == (True,False,False):
            btn.r = 230
            btn.g = 230
            btn.b = 250
        else:
            btn.r = 128
            btn.g = 128
            btn.b = 128
    else:
        btn.r = 255
        btn.g = 0
        btn.b = 0
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False