import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage bullets fired from the ship"""
    def __init__(self, game_instance):
        super.__init__() # inherit Sprite to get access to all of the methods
        self.screen = game_instance.screen
        self.settings = game_instance.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) with the width and height provided
        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                             self.settings.bullet_height)
                                              
        # Place the bullet (it's rect) in the midtop of the ship (it's rect)
        # Make each new bullet apear on top of the ship
        self.bullet_rect.midtop = game_instance.ship.ship_rect.midtop

        # Store the bullet's position (on y axis) as a float
        # this is used to modify the bullet location by it's speed
        # as we've done with the rocket and the ship
        self.bullet_y = float(self.bullet_rect.y)

    def move_bullet(self):
        """Manage the bullet movements"""
        # Move the exact pos on Y-axis
        self.bullet_y -= self.settings.bullet_speed
        
        # update the bullet position on Y axis
        self.bullet_rect.y = self.bullet_y

    def draw_bullet(self):
        """Display the bullet on the screen"""
                # screen to display on, obj's color, obj's rect (shape)
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)

    


        


