"""author  =  Haibo """


import pygame


pygame.init()


windows = pygame.display.set_mode((400,600))
pygame.display.set_caption("haibo")
windows.fill((255,255,255))

image1 = pygame.image.load('E:\Pygame-game_develop\Plane_Vs_alien\pre-files\Images\plane.png')
rect = image1.get_rect()
screen_rect = windows.get_rect()

rect.centerx = screen_rect.centerx
rect.bottom = screen_rect.bottom

windows.blit(image1,rect)


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

run_game()