"""author  = Haibo """

#1.init operations
import pygame

#2.create game objects
#set_mode(screen constants)
window = pygame.display.set_mode((400,600))
# define game name
pygame.display.set_caption('Haibo')


#3.Game keeps running state
#game loop
while True:
    #4.Test event
    for event in pygame.event.get():
        # pass
        #check click close button event
        if event.type == pygame.QUIT:
            #quit (thread)    
            exit()