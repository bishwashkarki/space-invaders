
import pygame

screen = pygame.display.set_mode((1600,900))
#screen = pygame.display.set_mode((1500,800))

background = pygame.image.load('images/background_space.bmp').convert()
player1=pygame.image.load('images/player1.bmp').convert()
projectile1=pygame.image.load('images/fireball1.gif').convert()
player1 = pygame.transform.scale(player1, (50, 50))
projectile1 = pygame.transform.scale(projectile1, (20, 20))

enemy1=pygame.image.load("images/alien1.bmp").convert()
enemy1 = pygame.transform.scale(enemy1, (50, 50))

enemy_pos=enemy1.get_rect(midtop=(700,100))
#pos=pygame.image.load("images/white166.gif").convert()

enemy_run=1
FPS=60
fpsClock=pygame.time.Clock()



class space_ship:
    
    def __init__(self):
        pass

    def shoot_proj(self,x,y):
        #x , y = pos_x_y.rect.x , pos.rect.y
        ball_position = projectile1.get_rect(midbottom=(x,y))
        screen.blit(projectile1, ball_position)
        
        
        while True:
            #self.space_ship_movement()
            if (ball_position.top>0):
                screen.blit(background, ball_position, ball_position)
                ball_position = ball_position.move(0, -10)
                screen.blit(projectile1, ball_position) 
                pygame.display.update()
                pygame.time.delay(30)
                if pygame.Rect.colliderect(enemy_pos,ball_position)==True:
                    global enemy_run
                    enemy_run=2
                    break
            else:
                break
            

    def space_ship_movement(self):

        #pos_x_y=pos.get_rect(spritex,spritey)
        speed=2

        
        spritex=700
        spritey=800

        WHITE=(255, 255, 255)
        player1.set_colorkey(WHITE)

        


        main=True

        while main:
            screen.blit(background,(0,0))
            screen.blit(player1, (spritex, spritey))
            if enemy_run==1:
                screen.blit(enemy1,enemy_pos)
            elif enemy_run==2:
                screen.fill(WHITE)
                enemy1.kill()
                pygame.display.update(enemy_pos)

            #if pygame.Rect.colliderect(enemy_pos,ball_position)==True:
            #    
            #
            #
            

            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_LEFT]:
                spritex -= speed

            if keys_pressed[pygame.K_RIGHT]:
                spritex += speed

            if keys_pressed[pygame.K_UP]:
                spritey -= speed

            if keys_pressed[pygame.K_DOWN]:
                spritey += speed

            
                
                
                
                






            pygame.display.update()
            fpsClock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); 
                    main = False
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        pygame.quit()
                        main = False 
                    if event.key == event.key == ord('z'):
                        self.shoot_proj(spritex,spritey)
                

            

        

#class shoot_projectile:
#    #def __init__(self,spritex,spritey,vel):
#    #    self.spritex=spritex
#    #    self.spritey=spritey
#    #    self.vel=vel
    

#proj_cor = shoot_projectile(500,500,2)