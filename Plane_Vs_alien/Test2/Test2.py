""" author =  haibo"""

import sys
import pygame
from t2setting import Setting2
from test2HF import Ship
import t2ft as tf
pygame.init()

t2setting1 = Setting2()

screen = pygame.display.set_mode((t2setting1.screen_width,t2setting1.screen_height))
pygame.display.set_caption("haibo")


ship = Ship(screen,t2setting1)

while True:
    tf.check_events(ship)
    ship.update()
    tf.update_screen(t2setting1,screen,ship)

run_game()
