import sys 
import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen1):
        pg.draw.rect(screen1,(120,20,220),(self.x,self.y,self.w,self.h))
pg.init()
run = True
win_x, win_y = 800, 480
a = 100
b = 100
screen = pg.display.set_mode((win_x, win_y))
screen2 = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(a,b,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา
screen2.fill((255, 0, 0))
q = 1
while(run):
    screen.fill((255, 0, 255))
    firstObject.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
    firstObject.x = a
    firstObject.y = b
    pg.time.delay(10)
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            a += q
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            a += -q
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม D
            b += -q
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            b += q
        if event.type == pg.KEYDOWN and event.key == pg.K_q:
            q += 1