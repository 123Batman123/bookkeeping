import pygame

WIDTH = 360
HEIGHT = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, d, w, h_max):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((d, w))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, h_max)
    def update(self):
        self.rect.y += 5
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0