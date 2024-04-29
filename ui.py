import pygame
from sys import argv
from pyautogui import size as screen_size

pygame.init()

class Events:
    class mouse:
        h = False
        c = False
        p = pygame.mouse.get_pos()


window = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PyMcLauncher")

scene = "home"

def draw():
    window.fill(pygame.Color(45, 45, 45))
    pygame.display.flip()


def main():
    run = True
    clock = pygame.time.Clock(60)
    while run:
        if Events.mouse.c:
            Events.mouse.c = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                Events.mouse.p = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Events.mouse.c = True
                Events.mouse.h = True
            if event.type == pygame.MOUSEBUTTONUP:
                Events.mouse.h = False
        draw()

main()
pygame.quit()