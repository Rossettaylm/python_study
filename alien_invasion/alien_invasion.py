import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    # 初始化设置对象和屏幕大小
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    # 创建标题
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于统计信息的实例, 并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")


    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship,
                    stats, sb, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb,
                    ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats,
                sb, ship, aliens, bullets, play_button)


run_game()
