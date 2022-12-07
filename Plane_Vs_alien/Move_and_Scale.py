""" author  =  Haibo """

import pygame
 
pygame.init()


width = 400
height = 600
windows = pygame.display.set_mode((width, height))
pygame.display.set_caption("haibo")
windows.fill((255,255,255))

#1.Display static ball
pygame.draw.circle(windows,(255,0,0),(100,100),50)
pygame.display.update()

y=100

while True:
    y += 1
    pygame.draw.circle(windows,(255,0,0),(100,y),50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
