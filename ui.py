import pygame
from sys import argv

pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PyMcLauncher")

class Events:
    class mouse:
        h = False
        c = False
        p = pygame.mouse.get_pos()
        

class Button:
    def __init__(self, x, y, paddingX, text):
        self.x = x
        self.y = y
        self.f = "arial.ttf"
        self.c = pygame.Color(70, 70, 70)
        self.plain_text = text
        self.padding = paddingX
        self.t = pygame.font.SysFont(self.f, 50).render(self.plain_text, True, "white")
        self.clicked = False
        self.execute = False
    def menu(self):
        if Events.mouse.p[0]+self.padding > self.x and Events.mouse.p[0] < self.x + (len(self.plain_text)*20)+(self.padding) and Events.mouse.p[1] > self.y and Events.mouse.p[1] < self.y+70:
            if Events.mouse.h:
                self.c = pygame.Color(30, 30, 30)
                self.clicked = True
            else:
                if self.clicked:
                    self.execute = True
                    self.clicked = False
                self.c = pygame.Color(100, 100, 100)
        else:
            self.c = pygame.Color(70, 70, 70)
        pygame.draw.rect(window, self.c, (self.x-self.padding, self.y, 100+(self.padding*2), 70))
        window.blit(self.t, (self.x, self.y+17))
            
            
buttons = [Button(window.get_width()/2-70, 200, 100, "Launch"), Button(window.get_width()/2-70, 300, 100, "Version")]

scene = "home"


def home():
    window.fill(pygame.Color(47, 49, 54))
    for button in buttons:
        button.menu()


def draw():
    if scene == "home":
        home()
    else:
        window.fill("white")
    pygame.display.flip()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
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