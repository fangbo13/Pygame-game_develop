"""author  =  Haibo """

import pygame

pygame.init()


window = pygame .display.set_mode((400,600))
pygame.display.set_caption('Haibo')

window.fill((255,255,255))
#================================================================
image1 = pygame.image.load('E:\Pygame-game_develop\Plane_Vs_alien\Images\plane.png')

new1 = pygame.transform.scale(image1,(50,50))
window.blit(new1, (100,50))

#================================================================
#1.画直线
#line(位置，颜色，起点，终点，宽度=1)
pygame.draw.line(window,(255,0,0),(10,20),(200,20))

#2.画折线
#line(位置，颜色，是否闭合,多个点，宽度=1)

points =    [(10,300),(100,160),(180,260),(300,10)]
pygame.draw.lines(window,(0,255,0),True,points,3)

pygame.display.update()




pygame.display.update()   

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
#================================================================