"""author  =  Haibo """

import pygame

pygame.init()


width = 400
height = 600
window = pygame .display.set_mode((width, height))
pygame.display.set_caption("haibo")
window.fill((255,255,255))



font = pygame.font.Font('E:\Pygame-game_develop\Plane_Vs_alien\wordfIle\wordfile.ttf',30)


tx = 0
count = 0
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            exit()
        

        if event.type == pygame.MOUSEMOTION:
            count += 1
            print(count)

        if event.type == pygame.KEYDOWN:
            print("按键被按下",event.key,chr(event.key))
            if chr(event.key) == 's':
                print("True")

            text = font.render(chr(event.key),True,(255,0,0))
            # window.fill((255,255,255))
            window.blit(text,(tx,300))
            tx += 15
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("位置是",event.pos)

        if event.type == pygame.KEYUP:
            print("按键弹起")
        