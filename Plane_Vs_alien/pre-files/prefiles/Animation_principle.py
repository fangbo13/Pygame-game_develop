"""author  =  Haibo """

import pygame

pygame.init()

Win_WidtH = 400
Win_Height = 600

windows = pygame.display.set_mode((Win_WidtH,Win_Height))
pygame.display.set_caption("haibo")
windows.fill((255,255,255))

y = 100
pygame.draw.circle(windows,(255,0,0),(100,y),50)    
pygame.display.update()

num =1
r=100
while True:
    num+= 1
    #移动动画
    # if num % 10 == 0:
    #     pygame.draw.circle(windows,(255,255,255),(100, y), 50)
    #     y = y + 0.1 #速度
    #     pygame.draw.circle(windows,(255,0,0),(100,y),50)    
    #     pygame.display.update()
    #2)缩放动画

    if num % 10000 == 0:
        pygame.draw.circle(windows,(255,255,255),(100,y),r)
        r +=1
        pygame.draw.circle(windows,(255,0,0),(100,y),r)
        pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


