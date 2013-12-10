from pygame import locals
import pygame as view
import ImageGrab as cam
from pygame import time
from pygame import image
import filter_functions as fil
from spyi import createImage
from spyi import openImage
from decode import negativeFilter
BLACK=(0,0,0)
WHITE=(255,255,255)
OLIVE=(128,128,0)
MAROON=(128,0,0)
BACKGROUND=(800,800)
CANVAS=(600,600)

#grab screenshot backgound

filters=[fil.filterone(),fil.filtertwo(),fil.filterthree()]



def main():
    view.init() 
    cam.grab((0,0,800,800)).save('screenst.png','png')
    #startimage=openImage('canvasimg')
    currentimg=open('currentimg.png')
    FPS=30
    #canvas
    canvas=view.image.load("canvasimg.png")
    #canvas=view.Surface((500,600))
    canvasrect=canvas.get_rect()
    #canvas.fill((250,250,250))
    #screen
    screen=view.display.set_mode((600,600),locals.NOFRAME,32)
    view.display.set_caption("imageviewer")
    screen.fill((OLIVE))
    #background
    background=image.load('screenst.png')
    #background=view.Surface((800,800))
    #background.fill((250,250,250))
    #buttons 
    background.blit(canvas,canvasrect)
    b1=view.Surface((30,30))
    b1.fill(OLIVE)
    br1=b1.get_rect()
    br1.center=(85,185)
    background.blit(b1,br1)
    b2=view.Surface((30,30))
    b2.fill(OLIVE)
    br2=b2.get_rect()
    br2.center=(135,285)
    background.blit(b2,br2)
    b3=view.Surface((30,30))
    b3.fill(OLIVE)
    br3=b3.get_rect()
    br3.center=(365,485)
    background.blit(b3,br3)
    b4=view.Surface((30,30))
    b4.fill(OLIVE)
    br4=b4.get_rect()
    br4.center=(485,485)
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
                        currentimg=negativeFilter(currentimg)
                        createImage(currentimg,'outcanvasimg')

                        #buttonrect[button]=buttonrect[button]
                        #filters[button]()
            if ev.type==locals.QUIT:
                pass
                #view.quit()


if __name__=='__main__': main()
