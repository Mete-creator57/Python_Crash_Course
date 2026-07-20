import pygame
from settings import Settings

class Rocket:
    """Manage the rocket"""
    def __init__(self, game_obj):
        """Init the rocket settings"""

        # get the screen
        self.screen = game_obj.screen

        # shape a rect form
        self.screen_rect = game_obj.screen.get_rect()
        
        # get the game settings
        self.settings = game_obj.settings

        # upload the rocket image
        self.rocket_image = pygame.image.load(r'D:\Soft_Dev\Python_Crash_Course\Part_2_Projects\images\rocket.png')
        
        # shape the rocket as a rect
        self.rocket_rect = self.rocket_image.get_rect()
        
        # place each new rocket in the center of the screen
        self.rocket_rect.center = self.screen_rect.center
        
        # set the movement flags
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        
        # access settings's class methods
        
        self.rocket_x = float(self.rocket_rect.x)
        self.rocket_y = float(self.rocket_rect.y)

    def blit_rocket(self):
        """Display the rocket on the screen"""
        self.screen.blit(self.rocket_image, self.rocket_rect)

    def move_rocket(self):
        """Adjust the rocket position based on a flag"""
        # 
        if self.move_right and self.rocket_rect.right < self.screen_rect.right:
            self.rocket_x += self.settings.rocket_speed

        elif self.move_left and self.rocket_rect.left > self.screen_rect.left:
            self.rocket_x -= self.settings.rocket_speed

        elif self.move_up and self.rocket_rect.top < self.screen_rect.top:
            self.rocket_y -= self.settings.rocket_speed
        elif self.move_down and self.rocket_rect.bottom > self.screen_rect.bottom:
            self.rocket_y += self.settings.rocket_speed
        
        self.rocket_rect.x = self.rocket_x
        self.rocket_rect.y = self.rocket_y

    
        



        




