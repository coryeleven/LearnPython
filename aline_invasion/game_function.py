import sys
import pygame
def check_events():
    for event in pygame.event.get():
        "响应鼠标按键"
        if event.type == pygame.quit():
            sys.exit()