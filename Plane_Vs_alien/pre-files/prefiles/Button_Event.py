"""author  =  Haibo """


import pygame


pygame.init()



width = 400
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("haibo")
window.fill((255,255,255))




font = pygame.font.Font('E:\Pygame-game_develop\Plane_Vs_alien\wordfIle\wordfile.ttf',30)

#确定按钮
bx1,by1,bw,bh = 30,100,100,50
pygame.draw.rect(window, (255,0,0),(bx1, by1, bw , bh))
text1 = font.render('Yes',True,(255,255,255))
tw1,th1 = text1.get_size()
tx1 = bx1 + bw/2 - tw1/2
ty1 = by1 + bh/2 - th1/2
window.blit(text1,(tx1,ty1))



#取消按钮
bx2,by2 = 30,200
pygame.draw.rect(window, (0,255,0),(bx2, by2, bw , bh))
text2 = font.render('No',False,(255,255,255))
tw2,th2 = text2.get_size()
tx2 = bx2 + bw/2 - tw2/2
ty2 = by2 + bh/2 - th2/2
window.blit(text2,(tx2,ty2))

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            #是否点击了确定按钮
            if bx1 <= mx <=bw and by1 <= my <= by1+ bh:
                pygame.draw.rect(window, (200,200,200),(bx1, by1, bw , bh))
                window.blit(text1,(tx1,ty1))
                pygame.display.update() 
                print('确定按钮被点击')

            if bx2 <= mx <=bw and by2 <= my <= by2+ bh:
                pygame.draw.rect(window, (200,200,200),(bx2, by2, bw , bh))
                window.blit(text2,(tx2,ty2))
                pygame.display.update()
                print('取消按钮被点击')

        if event.type == pygame.MOUSEBUTTONUP:
            pygame.draw.rect(window, (255,0,0),(bx1, by1, bw , bh))
            window.blit(text1,(tx1,ty1))
            pygame.display.update() 


            pygame.draw.rect(window, (0,255,0),(bx2, by2, bw , bh))
            window.blit(text2,(tx2,ty2))
            pygame.display.update() 
            