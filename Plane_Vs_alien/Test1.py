import pygame  # 导入 pygame 库

def run_game():
    pygame.init()  # 初始化 pygame

    windows = pygame.display.set_mode((400, 600))  # 创建一个窗口, 宽 400, 高 600
    pygame.display.set_caption("haibo")  # 设置窗口标题

    windows.fill((255, 255, 255))  # 填充窗口背景色为白色

    image1 = pygame.image.load('E:\Pygame-game_develop\Plane_Vs_alien\pre-files\Images\plane.png')  # 加载图像
    rect = image1.get_rect()  # 获取图像的矩形对象

    screen_rect = windows.get_rect()  # 获取窗口的矩形对象
    rect.centerx = screen_rect.centerx  # 将图像的横坐标设置为窗口的中心横坐标
    rect.bottom = screen_rect.bottom  # 将图像的纵坐标设置为窗口的底部纵坐标

    windows.blit(image1, rect)  # 将图像绘制到窗口上

    pygame.display.flip()  # 更新窗口显示

    while True:
        for event in pygame.event.get():  # 获取事件列表
            if event.type == pygame.QUIT:  # 如果事件类型为退出程序
                exit()  # 退出程序

if __name__ == '__main__':
    run_game()  # 运行游戏
