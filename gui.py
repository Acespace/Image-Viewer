from pygame import locals
import pygame as view
from PIL import ImageGrab
 
rectpath=[]       
#for x in range(0,800,4):
    
        


#constants
BLACK=(0,0,0)
WHITE=(255,255,255)
OLIVE=(128,128,0)
MAROON=(128,0,0)
BACKGROUND=(800,800)
CANVAS=(600,600)
FPS=70




view.init()

canvas=view.Surface((CANVAS),0,)
img=ImageGrab.grab()
img.save("screenimage.jpg")
background=view.image.load("screenimage.jpg")
backgroundrect=background.get_rect()
background.blit(background,(0,0))

screen=view.display.set_mode(CANVAS,locals.NOFRAME,32)
screen=view.Surface.fill(screen,(OLIVE))
clocky=view.time.Clock
chazsurface=view.image.load("chazzy.png")

chazrect=chazsurface.get_rect()

b1=view.Surface((30,30))
br1=view.Rect(85,185,30,30)
b1.blit(b1,br1)

b2=view.Surface((30,30))
br2=view.Rect(135,285,30,30)
b2.blit(b2,br2)

b3=view.Surface((30,30))
br3=view.Rect(365,485,30,30)
b3.blit(b3,br3)

b4=view.Surface((30,30))
br4=view.Rect(485,485,30,30)
b4.blit(b4,br4)
br4.blit(br4,screen)




while True:    
    view.display.flip()
    view.time.Clock()
    for event in view.event.get():
        if event.type==locals.QUIT:
            view.quit()
