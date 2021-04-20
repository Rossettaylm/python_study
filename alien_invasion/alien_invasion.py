import sys
import pygame
from settings import Settings 
from ship import Ship

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    #创建标题
    pygame.display.set_caption("Alien Invasion")
    #设置背景颜色
    bg_color = (ai_settings.bg_color)
    #创建一艘飞船
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
