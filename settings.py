class Settings():
    '''存储所有的类'''

    def __init__(self):
        '''初始化游戏设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.back_color = (230,230,230)
        #设置飞船属性
        self.ship_speed_factor = 3