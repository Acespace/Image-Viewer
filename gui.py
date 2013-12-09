from pygame import locals
import pygame as view
from PIL import ImageGrab
BLACK=(0,0,0)
WHITE=(255,255,255)
OLIVE=(128,128,0)
MAROON=(128,0,0)
BACKGROUND=(800,800)
CANVAS=(600,600)


def main():
    view.init()
    FPS=30
    clocky=view.time.Clock
    #screen
    screen=view.display.set_mode((800,800),locals.NOFRAME,32)
    view.display.set_caption("imageviewer")
    screen.fill((OLIVE))
    #background
    background=view.Surface((800,800))
    background.fill((250,250,250))
    #buttons    
    b1=view.Surface((30,30))
    br1=b1.get_rect()
    br1.center=(85,185)
    background.blit(b1,br1)
    b2=view.Surface((30,30))
    br2=b2.get_rect()
    br2.center=(135,285)
    background.blit(b2,br2)
    b3=view.Surface((30,30))
    br3=b3.get_rect()
    br3.center=(365,485)
    background.blit(b3,br3)
    b4=view.Surface((30,30))
    br4=b4.get_rect()
    br4.center=(485,485)
    background.blit(b4,br4)
    buttons=[b1,b2,b3,b4]
    buttonrect=[br1,br2,br3,br4]
    screen.blit(background,(0,0))
    while True:    
        view.display.update()
        #clocky.tick(FPS)
        for event in view.event.get():
            if event.type==locals.QUIT:
                pass
                #view.quit()


if __name__=='__main__': main()
