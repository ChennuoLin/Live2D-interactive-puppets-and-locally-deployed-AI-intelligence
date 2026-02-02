# -*- coding: utf-8 -*-
# -*- file: live2d_test.py -*-
import live2d.v3 as live2d
import pygame
from pygame.locals import *
from OpenGL.GL import *
import time
import random
import threading

touch_area={'head':[(-0.5, 0.93), (-0.31, 0.65)],'body_up':[(-0.47, 0.63), (-0.31, 0.27)],'body_down':[(-0.49, 0.27), (-0.25, 0.0)],
'left_hand':[(-0.44, 0.61), (-0.64, -0.02)],'left_foot':[(-0.53, 0.04), (-0.47, -0.86)],
'right_hand':[(-0.36, 0.61), (-0.13, -0.02)],'right_food':[(-0.38, -0.02), (-0.22, -0.87)]}

#list_0=[]

touch_time={'body_down':0}

num=[0]
motion_list=[]

def print_numbers():
    a=input('')
    motion_list.append(a)

def area_detection(a):
    for item in list(touch_area.keys()):
        x1, y1 = touch_area[item][0]
        x2, y2 = touch_area[item][1]
        x, y = a
        
        if ((min(x1, x2) <= x <= max(x1, x2)) and (min(y1, y2) <= y <= max(y1, y2))):
            if len(motion_list)!=0:
                motion_list.clear()
                print(motion_list[0])


            if item == "body_down":
                if model.IsMotionFinished()==True:
                    touch_time["body_down"]=int(touch_time["body_down"])+1
                    if touch_time["body_down"]>=5:
                        live2d.dispose()
                        pygame.quit()
                        exit()

                    pygame.mixer.music.load("./vioce/under.mp3")
                    pygame.mixer.music.play()

                    model.StartMotion("Flick3", 0, 1)
                

            elif item == "body_up":
                
                pygame.mixer.music.load("./vioce/body.mp3")
                pygame.mixer.music.play()
                model.StartMotion("Idle",0,5)


            elif item == "head":
                if model.IsMotionFinished()==True:
                    pygame.mixer.music.load("./vioce/head.mp3")
                    pygame.mixer.music.play()
                    model.StartMotion("Tap",0,1)
                
                

            elif item == "left_foot" or item == "left_hand":
                model.StartMotion("Tap2",0,1)
            elif item == "right_food" or item == "right_hand":
                model.StartMotion("Tap3",0,1)



class Live2D(object):
 
    @staticmethod
    def render(surface: pygame.SurfaceType) -> object:
        texture_data = pygame.image.tostring(surface, "RGBA", 1)
        id: object = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, id)
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGBA,
            surface.get_width(),
            surface.get_height(),
            0,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            texture_data
        )
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        return id
 
    @staticmethod
    def blit(id: object, *args: tuple[tuple[3], tuple[3], tuple[3], tuple[3]]) -> None:
        glBindTexture(GL_TEXTURE_2D, id)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(*args[3])
        glTexCoord2f(1, 0); glVertex3f(*args[1])
        glTexCoord2f(1, 1); glVertex3f(*args[2])
        glTexCoord2f(0, 1); glVertex3f(*args[0])
        glEnd()
 
 
live2d.setLogEnable(False)
pygame.init()
live2d.init()
 
screen=pygame.display.set_mode((460, 520), DOUBLEBUF | OPENGL | pygame.SRCALPHA, vsync = 1)

if live2d.LIVE2D_VERSION == 3:
    live2d.glewInit()

model: live2d.LAppModel = live2d.LAppModel()
model.LoadModelJson(r".\miku\runtime\miku.model3.json")
model.Resize(400, 500)
model.SetAutoBlinkEnable(True)
model.SetAutoBreathEnable(True)
model.StartMotion("Idle",0,1)
pygame.mixer.music.load("./vioce/Hi.mp3")
pygame.mixer.music.play()
thread1 = threading.Thread(target=print_numbers)
thread1.start()
run: bool = True
TF=[True]
while run:
    
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
            run = not run
            break

        if event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            gl_x = round((mouse_x / 400) - 1,2) 
            gl_y = round(1 - (mouse_y / 275),2)
            #list_0.append((gl_x,gl_y))
            #print(list_0)
            area_detection((gl_x,gl_y))
        
        if model.IsMotionFinished()==True and event.type != MOUSEBUTTONDOWN and TF[-1]:
            list_motion=['Flick0','Flick2']
            model.StartMotion(random.choice(list_motion),0,1)
            TF.append(False)
        else:
            TF.append(True)
        
    
    live2d.clearBuffer()
    screen.fill((255, 255, 255, 0))
    
    glEnable(GL_TEXTURE_2D)
    #Live2D.blit(back, *back_pos)
    model.Update()
    model.Draw()
    pygame.display.flip()


 
#print(list_0)
live2d.dispose()
pygame.quit()
exit()
