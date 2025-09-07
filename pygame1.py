import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))


doone = False

while not doone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doone = True
    pygame.display.flip()