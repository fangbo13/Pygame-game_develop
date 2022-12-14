import sys
import pygame
from settings import Settings
from ship import Ship



def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("haibo")

    ship = Ship(screen)
    
    #设置背景颜色
    bg_color = (230,230,230)


    # 开始游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #填充背景色
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # 更新屏幕
        pygame.display.update()


run_game()