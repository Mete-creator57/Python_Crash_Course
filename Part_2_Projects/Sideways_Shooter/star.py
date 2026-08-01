import pygame
from pygame.sprite import Sprite
import os # Import os for robust path handling
# from pathlib import Path # Pathlib is fine, but os.path.join is often more common for assets
class Star(Sprite):
    """A class representing a star"""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() # Store screen_rect for easy access

        # Construct the path to star.png robustly
        # This assumes star.png is in the same directory as star.py
        image_path = os.path.join(os.path.dirname(__file__), 'star.png')
        self.image = pygame.image.load(image_path)

        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        # Initial positioning will be handled by the _create_stars_ method in Shooter_Game.
        # We'll just set a default, which will be immediately overwritten.
        self.rect.x = 0
        self.rect.y = 0

        self.x = float(self.rect.x) # Keep this for float precision for movement

