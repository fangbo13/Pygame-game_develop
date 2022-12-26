"""author  =  Haibo """

import pygame

pygame.init()


width = 400
height = 600

windows = pygame.display.set_mode((width, height))
pygame.display.set_caption("haibo")
windows.fill((255,255,255))

y = 100
x = 100
r = 30
y_speed = 2
pygame.draw.circle(windows, (255,0,0),(x,y),r)


num = 0
pygame.display.update()
while True:
    num += 1
    if num %1000 == 0:
        new1 = pygame.draw.circle(windows, (255,255,255),(x,y),r)

        #修改y坐标
        y += y_speed

        #检测下边界
        if y >= height - r:
            y_speed= -1
            
            
        #检测上边界    
        if y <= r : 
            y_speed =y_speed * -1

        pygame.draw.circle(windows, (0,255,0),(x,y),r)
        pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()