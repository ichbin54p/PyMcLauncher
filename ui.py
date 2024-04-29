import pygame

def main():
    run = True
    clock = pygame.time.Clock(60)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()
pygame.quit()