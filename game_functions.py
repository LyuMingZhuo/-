import sys

import pygame

def check_events():
    '''响应鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    '''更新屏幕图像并切换到新屏幕上'''
    # 每次循环时重绘屏幕
    screen.fill(ai_settings.back_color)
    ship.blitme()

    # 显示最近绘制的屏幕
    pygame.display.flip()