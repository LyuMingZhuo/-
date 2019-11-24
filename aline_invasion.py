import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    #初始化游戏并创建和设置屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Aline_Invasiopn")

    #创建一艘飞船
    ship = Ship(screen)

    #设置背景颜色
    #back_color = (230,230,230),已导入SETTING类

    #开始游戏主循环
    while True:
        #监视鼠标键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环时重绘屏幕
        screen.fill(ai_settings.back_color)
        ship.blitme()

        #显示最近绘制的屏幕
        pygame.display.flip()

run_game()