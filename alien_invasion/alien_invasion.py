import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    #创建标题
    pygame.display.set_caption("Alien Invasion")
    #设置背景颜色
    bg_color = (230, 230, 230)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)

        pygame.display.flip()

run_game()
