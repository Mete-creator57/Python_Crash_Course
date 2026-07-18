import pygame


class Ship:
    """The main class to manage the ship"""

    # An instance of the alien invasion as a param
    def __init__(self, game_instance):
        """Init the ship and set it's starting pos"""

        # a reference to the game's screen so
        # the ship knows where it has to be drawn
        self.screen = game_instance.screen

        # access the game settings
        self.settings = game_instance.settings
        
        # get the screen rect to place the ship correctly on it
        self.screen_rect = game_instance.screen.get_rect()

        # Load the ship image and assign it to the ship 
        self.image = pygame.image.load('D:\Soft_Dev\Python_Crash_Course\Part_2_Projects\images\DurrrSpaceShip.png')
        
        # rect -> rectangle (used for all objects)
        # get the ship rect
        self.ship_rect = self.image.get_rect()
        
        # start each new ship at the bottom center of the screen
        # place the ship at the bottom center
        self.ship_rect.midbottom = self.screen_rect.midbottom
        
        # store a float for the ship's  exact horizontal position
        self.ship_x = float(self.ship_rect.x)

        self.ship_y = float(self.ship_rect.y)

        # movement flag; start with a not moving ship
        self.movement_right = False
        self.movement_left = False
        self.movement_up = False
        self.movement_down = False

    def update_movement(self):
        """Update the ship's postion based on the movement flag"""

        # update the ship's x value, not it's rect
        if self.movement_right and self.ship_rect.right < self.screen_rect.right:
            self.ship_x += self.settings.ship_speed 
        
        # if the ship didn't reach the left side (left side 0)
        elif self.movement_left and self.ship_rect.left > self.screen_rect.left:
            self.ship_x -= self.settings.ship_speed

        elif self.movement_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_y += self.settings.ship_speed

        elif self.movement_up and self.ship_rect.top > self.screen_rect.top:
            self.ship_y = self.ship_y - self.settings.ship_speed

        # assign the updated coordinates to the ship's rect (form)
        self.ship_rect.x = self.ship_x
        self.ship_rect.y = self.ship_y


    def blit_draw(self):
        """Draw the ship based on a given location"""
        self.screen.blit(self.image, self.ship_rect)



