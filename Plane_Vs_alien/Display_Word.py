"""author  =  Haibo """

import pygame

pygame.init()

window = pygame .display.set_mode((400,600))
pygame.display.set_caption('Haibo')

window.fill((255,255,255))
# ===============display Word================================================================
#1) create font objects
#Font(URL of Word File)
font = pygame.font.Font('E:\Pygame-game_develop\Plane_Vs_alien\wordfIle\wordfile.ttf',30)


#2.create word objects
#render (文字内容，True，文字颜色，背景颜色)
text = font.render('game_develop',True,(255,0,0),(255,255,0))

#3.blit screen

window.blit(text,(0,0))

#4.operation word objects
#1)get size
w,h = text.get_size()
window.blit(text,(400-w,600-h))

#scale and rotate
new1 = pygame.transform.scale(text,(400,50))
window.blit(new1,(0,60))

new2 = pygame.transform.rotozoom(text,0,2)
window.blit(new2,(0,120))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
