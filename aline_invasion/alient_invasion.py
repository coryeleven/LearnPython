import  sys
import pygame
from setting import  Setting
from ship import Ship


def run_game():
    #初始化背景
    # bgcolor = (230,230,230)
    pygame.init()
    #初始化游戏并创建一个屏幕对象
    # screen = pygame.display.set_mode((1200,800))
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    #开始游戏主循环
    while True:
        #监视鼠标键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_setting.bgcolor)
        ship.blitme()
        #显示游戏窗口
        pygame.display.flip()

run_game()


