import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """显示得分信息的类"""
    
    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 28)

        # 准备初始得分图像和最高分图像,初始等级,飞船剩余数量
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()



    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        # 将得分圆整为10的倍数, round()函数表示精确到小数点后多少位
        rounded_score = int(round(self.stats.score, -1))
        # 对千分位插入逗号
        score_str = "{:,}".format(rounded_score)
        msg = 'Your score: ' + score_str
        self.score_image = self.font.render(msg, True, 
                self.text_color, self.ai_settings.bg_color)

        # 将得分放在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """将最高分渲染成图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        msg = 'Highest score: ' + high_score_str
        self.high_score_image = self.font.render(msg, 
                True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        """将初始等级转换为渲染的图像"""
        msg = 'Level: ' + str(self.stats.level)
        self.level_image = self.font.render(msg, True, self.text_color, self.ai_settings.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_ships(self):
        """显示还剩下多少艘飞船"""
        if self.stats.ships_left > 0:
            msg = "Ships left: "
        else :
            msg = "No ships left!"
        self.ship_str_image = self.font.render(msg, True, self.text_color, self.ai_settings.bg_color)

        self.ship_str_rect = self.ship_str_image.get_rect()
        self.ship_str_rect.left = 10
        self.ship_str_rect.top = 20

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = self.ship_str_rect.right + ship_number * ship.rect.width
            ship.rect.centery = self.ship_str_rect.centery
            self.ships.add(ship)



    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ship_str_image, self.ship_str_rect)
        self.ships.draw(self.screen)
