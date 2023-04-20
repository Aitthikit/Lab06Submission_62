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
    def __init__(self,r,g,b, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = (r,g,b)
        self.text = 'submit'
        self.txt_surface = font.render('submit', False, (0,0,0))
        self.active = False
    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
    def isMouseOn(self):
        tf = []
        for a,b in zip(pg.mouse.get_pos(),(self.rect.x,self.rect.y)):
            if (a >= b) :
                tf.append(True)
            else:
                tf.append(False)
        for a,b in zip(pg.mouse.get_pos(),(self.rect.x+self.rect.w,self.rect.y+self.rect.h)):
            if (a <= b) :
                tf.append(True)
            else:
                tf.append(False)
        for i in tf:
            if i == False:
                return False
        return True 
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = (0,0,0)
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = (255,0,0) if self.active else (0,0,0) # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
class InputBoxN:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = (0,0,0)
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = (255,0,0) if self.active else (0,0,0) # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.unicode in ['0','1','2','3','4','5','6','7','8','9'] :
                    self.text += event.unicode
                else:
                    None
                # Re-render the text.
                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
pg.init()
run = True
textShow = ''
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
font = pg.font.Font('freesansbold.ttf', 24) # font and fontsize
text = font.render('First Name', True, (0,0,0), (255,255,255))
text1 = font.render('Last Name', True, (0,0,0), (255,255,255))
text2 = font.render('Age', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
text3 = font.render(textShow, True, (0,0,0), (255,255,255))
textRect = text.get_rect() # text size
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect.bottomleft = (100, 80)
textRect1.bottomleft = (100,180)
textRect2.bottomleft = (100,280)
textRect3.bottomleft = (20,460)
COLOR_INACTIVE = pg.Color(0,0,0) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color (28,134,238)     # ^^^
FONT = pg.font.Font(None, 32)
btn = Button(0,0,0,400,300,100,100)
input_box1 = InputBox(100, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32) # สร้าง InputBox2
input_box3 = InputBoxN(100, 300, 140, 32)
input_boxes = [input_box1, input_box2,input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย

while(run):
    screen.fill((255, 255, 255))
    keep = []
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        keep.append(box.text)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    if btn.isMouseOn():
        if pg.mouse.get_pressed(num_buttons=3) == (True,False,False):
            btn.color = (230,230,250)
            for i in keep[0:3]:
                print(i)
            textShow = 'Hello '+ keep[0]+" "+keep[1]+"! You are "+keep[2]+" years old."
            text3 = font.render(textShow, True, (0,0,0), (255,255,255))
            keep = []
        else:
            btn.color = (128,128,128)
    else:
        btn.color = (255,0,0)
    btn.draw(screen)
    pg.time.delay(100)
    pg.display.update()
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    