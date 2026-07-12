import pygame


class Ship:
    """The main class to manage the ship"""

    # An instance of the alien invasion as a param
    def __init__(self, ai_instance):
        """Init the ship and set it's starting pos"""

        # a reference to the game's screen so
        # the ship knows where it has to be drawn
        self.screen = ai_instance.screen
        
        # get the screen rect to place the ship correctly on it
        self.screen_rect = ai_instance.screen.get_rect()

        # Load the ship image and assign it to the ship 
        self.image = pygame.image.load(r'images\DurrrSpaceShip.png')
        
        # rect -> rectangle (used for all objects)
        # get the ship rect
        self.ship_rect = self.image.get_rect()
        
        # start each new ship at the bottom center of the screen
        # place the ship at the bottom center
        self.ship_rect.midbottom = self.screen_rect.midbottom

        # movement flag; start with a not moving ship
        self.movement_right = False
        self.movement_left = False
        self.movement_up = False
        self.movement_down = False

    def update_movement(self):
        """Update the ship's postion based on the movement flag"""
        if self.movement_right == True:
            self.ship_rect.x += 1
        elif self.movement_left:
            self.ship_rect.x -= 1
        elif self.movement_down:
            self.ship_rect.y += 1
        elif self.movement_up:
            self.ship_rect.y -= 1



    def blit_draw(self):
        """Draw the ship based on a given location"""
        self.screen.blit(self.image, self.ship_rect)



