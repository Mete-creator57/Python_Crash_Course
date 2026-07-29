import pygame
from preferences import Preferences
class Jet:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.preferences = game.preferences # Access preferences from the game object
        self.image = pygame.image.load(r'jetfighter.png')
        self.rect = self.image.get_rect()

        # place in the midleft of the screen
        self.rect.midleft = self.screen_rect.midleft

        self.move_up = False
        self.move_down = False


        self.y = float(self.rect.y)

    def update(self):
        """Update the jet's position based on movement flags."""
        if self.move_up and self.rect.top > 0:
            self.y -= self.preferences.jet_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.preferences.jet_speed

        # Update the rect object from self.y
        self.rect.y = self.y


    def blit_jet(self):
        """Draw the jet on the screen"""
        self.screen.blit(self.image, self.rect)

