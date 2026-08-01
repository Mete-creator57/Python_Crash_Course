import pygame
from pygame.sprite import Sprite
from pathlib import Path
class Star(Sprite):
    """A class representing a star"""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        path = Path('star.png')
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        # place each new star at topright
        self.rect.topright = game.screen_rect.topright
        # move the x left
        self.rect.x -= 10
        # move the y down
        self.rect.y += 10



        self.x = float(self.rect.x)

