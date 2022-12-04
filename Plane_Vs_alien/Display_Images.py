"""author=  Haibo"""

import pygame 

pygame.init

window = pygame.display.set_mode((400,600))

pygame.display.set_caption('Haibo')
#set background color
window.fill((255,255,255))

#===============Game start static screen===============

#1. load images
image1 = pygame.image.load('E:\Pygame-game_develop\Plane_Vs_alien\Images\plane.png')

#2. blit images
#blit(blit objects,File URL)
window.blit(image1,(0,0))

#3.image settings
#(1)gets image size
w,h =image1.get_size()
#print(w,h)
window.blit(image1,(400-w,600-h))

#(2) rotates and scales
# scales(scale objects size)
# pygame.transform.scale(image1,(100,100))
new1 = pygame.transform.scale(image1,(100,100))
window.blit(new1,(210,0))


#rotozoom(scale/rotate objects, 旋转角度,缩放比例)
new2 = pygame.transform.rotozoom(image1,90,1)
window.blit(new2,(0,200))

#3.fresh display screen
#pygame.display.flip()
#pygame.display.update()

pygame.display.flip()   
pygame.display.update()

while True:
    #====================Game refresh====================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()