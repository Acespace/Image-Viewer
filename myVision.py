import sys, pygame

from pygame import time 


from pygame import * 









def swell(bl, pos):

    x,y = pos

    for b in bl:
        if b.collidepoint(x,y):
            b.inflate(30,30)

            


    




    

    
def main():

    # Initialise screen
    pygame.init()
    size = width, height = 600, 600
    # was 550,600

    screen = pygame.display.set_mode(size)

    screen.fill((255,255,255))
    # Makes whole screen white
    
  
    leftWall = pygame.Rect(0, 0, 60, 600)
    
    pygame.draw.rect(screen,(64,50,132), leftWall,0)
    # makes left wall

    rightWall = pygame.Rect(540, 0, 60, 600)

    pygame.draw.rect(screen,(60,3,26), rightWall,0)
    # makes right wall

    baseLayer = pygame.Rect(60, 480, 480, 120)

    # makes button button holder (rectangle)

    pygame.draw.rect(screen,(104,114,113), baseLayer,0)



    #red button
    ButtonList=[]
    redButton = pygame.Rect(100, 500, 90, 65 )
    ButtonList.append(redButton)
    pygame.draw.rect(screen, (100,0,0), redButton)

    #green button
    greenButton = pygame.Rect(250, 500, 90, 65 )
    ButtonList.append(greenButton)
    pygame.draw.rect(screen, (0,100,0), greenButton)

    #blue button 
    blueButton = pygame.Rect(400, 500, 90, 65 )
    ButtonList.append(blueButton)
    pygame.draw.rect(screen, (0,0,100), blueButton)



    
    mousePos = pygame.mouse.get_pos()
    


            
            

    
    
    
    
        
    while True :
        pygame.display.update()
        swell(ButtonList,mousePos)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            
            


            

                print "hello"


            
if __name__ == '__main__': main()
