import pygame


class Ship:
    """The main class to manage the ship"""

    # An instance of the alien invasion as a param
    def __init__(self, ai_instance):
        """Init the ship and set it's starting pos"""

        # make the ship attribute access the game's attribute (screen settings)
        self.screen = ai_instance.screen
        
        # get the screen rect to place the ship correctly on it
        self.screen_rect = ai_instance.screen.get_rect()

        # Load the ship image and assign it to the ship 
        self.image = pygame.image.load('Part_2_Projects\images\DurrrSpaceShip.png')
        
        # rect -> rectangle (used for all objects)
        # get the ship rect
        self.ship_rect = self.image.get_rect()
        
        # start each new ship at the bottom center of the screen
        # place the ship at the bottom center
        self.ship_rect.midbottom = self.screen_rect.midbottom

    def blit_draw(self):
        """Draw the ship based on a given location"""
        self.screen.blit(self.image, self.ship_rect)



