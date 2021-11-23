#creating an game in which you can control a character and destroy "bots" comming towards you 



#importing all the modules needed to create this app

import pygame



def game():
#setting up pygame
    pygame.init()

                            
    #screen = pygame.display.set_mode((1600,900))
    screen = pygame.display.set_mode((1500,800))
    background = pygame.image.load('images/background_space.bmp').convert()
    player1=pygame.image.load('images/player2.bmp').convert()
    # jogo a correr
    main = True


    # equanto o jogo estiver a correr
    while main:
        
        
        # adiciona janela do jogo
        pygame.display.flip()
        pygame.time.wait(10)
        screen.blit(background,(0,0))
        
        position = player1.get_rect(midbottom=(700,800))
        screen.blit(player1, position) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); 
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    screen.blit(background, position, position)
                    position = position.move(-50, 0)
                    screen.blit(player1, position) 
                    pygame.display.update()
                    pygame.time.delay(100)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    screen.blit(background, position, position)
                    position = position.move(50, 0)
                    screen.blit(player1, position) 
                    pygame.display.update()
                    pygame.time.delay(100)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    screen.blit(background, position, position)
                    position = position.move(0, -50)
                    screen.blit(player1, position) 
                    pygame.display.update()
                    pygame.time.delay(100)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    screen.blit(background, position, position)
                    position = position.move(0, 50)
                    screen.blit(player1, position) 
                    pygame.display.update()
                    pygame.time.delay(100)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('forward stop')
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    print('backwards stop')
                if event.key == ord('q'):
                    pygame.quit()
                    main = False 
        

game()
