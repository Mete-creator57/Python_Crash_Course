import pygame
from pygame.sprite import Sprite

class Fire_Ball(Sprite):
    """Class to manage fireballs"""
    def __init__(self, game, jet):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Access preferences from the game object, don't create a new instance
        self.preferences = game.preferences

        self.image = pygame.image.load('Fireball1.png')
        self.rect = self.image.get_rect() # Use self.rect for consistency with Sprite

        # Position the fireball at the midright of the jet
        self.rect.midleft = jet.rect.midright

        # Store fireball's position as a float for precision
        self.x = float(self.rect.x)

    def update(self):
        """Move the fireball across the screen."""
        # Fireball always moves forward once created
        self.x += self.preferences.ball_speed

        # Update the rect object's position
        self.rect.x = self.x
            
        # Remove fireballs that have gone off-screen to save resources
        if self.rect.left >= self.screen_rect.right:
            self.kill() # Method provided by Sprite to remove itself from groups

    def blit_ball(self):
        """Draw the fireball on the screen"""
        self.screen.blit(self.image, self.rect)

