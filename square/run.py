import pygame
from square.play import Player
from square.play import BLUE, WIDTH, HEIGHT


def square_run():
    FPS = 30
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    player = Player(50,50,25)
    all_sprites.add(player)
    
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        screen.fill(BLUE)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
square_run()