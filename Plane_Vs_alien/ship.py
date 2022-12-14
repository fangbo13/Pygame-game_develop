# 导入 pygame 库
import pygame

# 定义 ship 类
class Ship():
    # 初始化飞船
    def __init__(self, screen):
        # 设置屏幕属性
        self.screen = screen

        # 加载飞船图像并获取其矩形
        self.image = pygame.image.load('E:\Pygame-game_develop\Plane_Vs_alien\pre-files\Images\plane.png')
        self.rect = self.image.get_rect()

        # 获取屏幕的矩形
        self.screen_rect = screen.get_rect()

        # 将飞船的中心设置为屏幕的中心
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    # 绘制飞船的方法
    def blitme(self):
        self.screen.blit(self.image,self.rect)
