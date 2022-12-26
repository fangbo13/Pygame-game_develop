
import pygame

class Ship():
    def __init__(self, screen ,t2setting1):

        self.screen = screen
        self.t2setting1 = t2setting1

        self.image = pygame.image.load('E:\Pygame-game_develop\Plane_Vs_alien\pre-files\Images\plane.png')
        self.rect = self.image.get_rect()


        self.screen_rect = screen.get_rect()     

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.screen.blit(self.image,self.rect) 
               

        self.center = float(self.rect.centerx)
        self.center = float(self.rect.bottom)


        
        self.moving_right = False
        self.moving_left  = False
        self.moving_up    = False
        self.moving_down  = False


    def update(self):
       
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.t2setting1.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.t2setting1.ship_speed_factor


        if self.moving_up and self.rect.top >0:
            self.bottom -= self.t2setting1.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.t2setting1.ship_speed_factor


        self.rect.centerx = self.center


    def blitme(self):
        self.screen.blit(self.image,self.rect)

