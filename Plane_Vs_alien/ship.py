# 导入 pygame 库
import pygame

# 定义 Ship 类
class Ship():
    # 初始化飞船
    def __init__(self, ai_settings, screen):
        # 设置屏幕属性
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其矩形
        self.image = pygame.image.load('E:\Pygame-game_develop\Plane_Vs_alien\pre-files\Images\plane.png')
        self.rect = self.image.get_rect()

        # 获取屏幕的矩形
        self.screen_rect = screen.get_rect()

        # 将飞船的中心设置为屏幕的中心
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 将飞船的属性 center 设置为浮点数，以便在 update() 方法中更新飞船的位置
        self.center = float(self.rect.centerx)

        # 将飞船的属性 moving_right 和 moving_left 设置为布尔值，用于在 update() 方法中移动飞船
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # 更新飞船的位置
    def update(self):
        # 如果 moving_right 和 moving_left 均为 False，则飞船不会移动
        # 否则，如果 moving_right 为 True 且飞船的右边界小于屏幕的右边界，则将飞船的 center 向右移动
        # 否则，如果 moving_left 为 True 且飞船的左边界大于 0，则将飞船的 center 向左移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        if self.moving_up and self.rect.top >0:
            self.rect.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.ai_settings.ship_speed_factor

        # 将矩形至于中心

        self.rect.centerx = self.center

    # 绘制飞船的方法
    def blitme(self):
        self.screen.blit(self.image,self.rect)
