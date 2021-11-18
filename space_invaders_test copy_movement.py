#creating an game in which you can control a character and destroy "bots" comming towards you 



#importing all the modules needed to create this app

import pygame
import pygame.mixer
from pygame.locals import *


def game():
#setting up pygame
    pygame.init()

                             
    #screen = pygame.display.set_mode((1600,900))
    screen = pygame.display.set_mode((1500,800))
    background = pygame.image.load('images/background_space.gif').convert()
    player1=pygame.image.load('images/player2.bmp').convert()
    # jogo a correr
    running = True


    # equanto o jogo estiver a correr
    while running:
        
        
        # adiciona janela do jogo
        pygame.display.flip()
        pygame.time.wait(10)
        screen.blit(background,(0,0))

        
        #position = player1.get_rect()
        screen.blit(player1, (650,600)) 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); 
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')
                if event.key == ord('q'):
                    pygame.quit()
                    main = False 







                    
game()