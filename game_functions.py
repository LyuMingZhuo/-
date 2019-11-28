import sys

import pygame

def check_events(ship):
    '''响应鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #飞船右移
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                #飞船左移
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings,screen,ship):
    '''更新屏幕图像并切换到新屏幕上'''
    # 每次循环时重绘屏幕
    screen.fill(ai_settings.back_color)
    ship.blitme()

    # 显示最近绘制的屏幕
    pygame.display.flip()