"""author  =  Haibo """

from random import randint
import pygame

pygame.init()



width = 400
height = 600

window =  pygame.display.set_mode((width,  height))
pygame.display.set_caption("haibo")
window.fill((255,255,255))

pygame.display.update()

count = 0 #统计事件的次数
while True:
    for event in pygame.event.get():
        #for 循环中的代码只有事件发生后才会执行
        count += 1 
        print(count)
#=============================鼠标事件===================================
        #event的type属性是用来区分不同类型的事件
        if event.type == pygame.QUIT:
            exit()
            #点击事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('鼠标摁下',event.pos)
            #传入位置形参
            mx,my = event.pos
            pygame.draw.circle(window,(255,255,0),(mx,my),50)
            pygame.display.update()
            #鼠标弹起
        if event.type == pygame.MOUSEBUTTONUP:
            print("鼠标弹起")
        if event.type == pygame.MOUSEMOTION:
            print("鼠标移动")
            mx,my = event.pos
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            pygame.draw.circle(window,(r,g,b),(mx,my),100)
            
            pygame.display.update()
