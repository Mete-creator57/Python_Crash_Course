import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage a single alien in the fleet"""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings # Important: access game's settings

        # load the alien image and get its rect attribute
        self.image = pygame.image.load('alien.png')

        # Scale the image to the desired size 
        self.image = pygame.transform.scale(self.image,
                                            (self.settings.alien_width, self.settings.alien_height))
        self.rect = self.image.get_rect() # Get rect *after* scaling

        # place each alien at the top left corner initially
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # get the exact horizontal position (on x axis) of an alien and store it
        self.x = float(self.rect.x) # using float for precision

