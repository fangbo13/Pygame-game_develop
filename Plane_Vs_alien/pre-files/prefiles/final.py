"""author  =  Haibo """


import pygame


pygame.init()



width = 400
height = 600




window = pygame.display.set_mode((width, height))
pygame.display.set_caption("haibo")
window.fill((255,255,255))
pygame.display.update()


plane = pygame.image.load('E:\Pygame-game_develop\Plane_Vs_alien\Images\dc.jpg')
pygame.display.update()



plane1_x,plane1_y = 173,551

plane1 = pygame.transform.scale(plane,(80,80))
plane_up = pygame.transform.scale(plane,(80,80))
plane_down = pygame.transform.scale(plane,(80,80))
plane_left = pygame.transform.scale(plane,(80,80))
plane_right = pygame.transform.scale(plane,(80,80))
plane_t = plane_up

window.blit(plane_t,(plane1_x,plane1_y))
pygame.display.update()


is_move = False
x_speed = 0
y_speed = 0

while True:
    if is_move == True:
        window.fill((255,255,255))
        plane1_x += x_speed
        plane1_y += y_speed

        window.blit(plane_t,(plane1_x,plane1_y))
        pygame.display.update()

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            char =chr(event.key)

            if chr(event.key) == 'w':
                is_move = True     
                x_speed = 0 
                y_speed = -1      
                plane_t = plane_up
                # window.fill((255,255,255))
                # plane1_y -= 100
                # window.blit(plane1,(plane1_x,plane1_y))
                # pygame.display.uwpdate()

            if chr(event.key) == 'a':
                is_move = True  
                x_speed = -1 
                y_speed = 0
                plane_t = plane_left  

            if chr(event.key) == 's':
                is_move = True
                x_speed = 0 
                y_speed = 1
                plane_t = plane_down 

            if chr(event.key) == 'd':
                is_move = True
                x_speed = 1 
                y_speed = 0         
                plane_t = plane_right

        if event.type == pygame.KEYUP:
            is_move = False
                

