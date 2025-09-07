import pygame
pygame.init()
screeen_width, screen_height = 400, 300
display_surface = pygame.display.set_mode((screeen_width, screen_height))
pygame.display.set_caption('adding backround image')


background_image = pygame.image.load("C:\\Users\\mirza\\OneDrive\\Pictures\\background.png").convert()
background_image=pygame.transform.scale(background_image, (screeen_width, screen_height))

penguin_image = pygame.image.load("C:\\Users\\mirza\\OneDrive\\Pictures\\penguin.png").convert_alpha()
penguin_image=pygame.transform.scale(penguin_image, (200, 200))

penguin_rect= penguin_image.get_rect(center=(screeen_width//2, screen_height//2+30))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)

        pygame.display.flip()
        clock.tick(30) 
    pygame.quit()
game_loop()