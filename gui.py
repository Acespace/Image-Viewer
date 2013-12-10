from pygame import locals
import pygame as view
import ImageGrab as cam
from pygame import time
from pygame import image
from filters import glacierBlue()
from filters import yellowDayFilter()
from filters import crayon()
import filter_functions as fil
BLACK=(0,0,0)
WHITE=(255,255,255)

OLIVE=(128,128,0)
MAROON=(128,0,0)
BACKGROUND=(800,800)
CANVAS=(600,600)

#grab screenshot backgound
cam.grab((0,0,800,800)).save('screenst.png','png')

filters=[fil.filterone(),fil.filtertwo(),fil.filterthree()]



def main():
    view.init()
    FPS=30
    #canvas
    canvas=view.Surface((500,600))
    canvasrect=canvas.get_rect()
    canvas.fill((250,250,250))
    
    #screen
    screen=view.display.set_mode((600,600),locals.NOFRAME,32)
    view.display.set_caption("imageviewer")
    screen.fill((OLIVE))
    canvas=canvas.convert_alpha()
    canvas.set_alpha(127)
    #background
    background=image.load('screenst.png')
    #background=view.Surface((800,800))
    #background.fill((250,250,250))
    #buttons 
    background.blit(canvas,canvasrect)
    b1=view.Surface((48,48))
    b1.fill((34,171,181))
    br1=b1.get_rect()
    br1.center=(85,185)
    background.blit(b1,br1)
    b2=view.Surface((48,48))
    b2.fill((34,171,181))
    br2=b2.get_rect()
    br2.center=(135,285)
    background.blit(b2,br2)
    b3=view.Surface((48,48))
    b3.fill((34,171,181))
    br3=b3.get_rect()
    br3.center=(300,440)
    background.blit(b3,br3)
    b4=view.Surface((48,48))
    b4.fill((34,171,181))
    br4=b4.get_rect()
    br4.center=(450,440)
    background.blit(b4,br4)
    buttons=[b1,b2,b3,b4]
    buttonrect=[br1,br2,br3,br4]
    screen.blit(background,(0,0))




    while True: 
        #next frame   
        view.display.update()
        for ev in view.event.get():
            #mouse event
            if ev.type==locals.MOUSEBUTTONDOWN:
                mousepos=view.mouse.get_pos()
                for button in [0,1,2,3]:                
                    if buttonrect[button].collidepoint(mousepos):
                       view.quit()
                        #buttonrect[button]=buttonrect[button]
                        #filters[button]()
            if ev.type==locals.QUIT:
                pass
                #view.quit()


if __name__=='__main__': main()
