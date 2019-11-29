import sys

import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 飞船右移
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 飞船左移
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # 飞船上移
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 飞船下移
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        #创建一个子弹，加入到编组Bullet中
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings,screen,ship,bullets):
    '''响应鼠标和键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship,bullets):
    '''更新屏幕图像并切换到新屏幕上'''
    # 每次循环时重绘屏幕
    screen.fill(ai_settings.back_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 显示最近绘制的屏幕
    pygame.display.flip()