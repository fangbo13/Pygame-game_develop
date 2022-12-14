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

#3.画圆
#circle(位置,颜色，圆心坐标，半径，线宽=0为 默认填充)
pygame.draw.circle(window,(0,0,255),(200,250),100,2)

#4.画矩形
#rect(位置，颜色，矩形范围，线宽=0)
pygame.draw.rect(window,(120,20,60),(100,70,200,100),3)

#5.画椭圆
#Ellipsis(位置，颜色， 圆形范围，线宽=0)
pygame.draw.ellipse(window,(255,0,0),(30,70,100,200),1)

#6.画弧线
#arc(位置，颜色，矩形范围，起始弧度，终止的弧度，线宽=1)

pygame.draw.arc(window,(0,0,0),(50,70,70,100),0,3.1415926,4)


pygame.display.update()   

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
#================================================================