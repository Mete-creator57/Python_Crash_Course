import pygame
from preferences import Preferences


class Fire_Ball():
    """Class to manage fireballs"""
    def __init__(self, game, jet):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.preferences = Preferences()

        self.image = pygame.image.load('Fireball1.png')
        self.ball_rect = self.image.get_rect()
    
        self.ball_rect.midright = jet.rect.midright

        self.move = False

        self.x = float(self.ball_rect.x)

    def update(self):
        if self.move:
            self.x += self.preferences.ball_speed

        # move the ball 
        self.ball_rect.x = self.x
            

    
    def blit_ball(self):
        self.screen.blit(self.image, self.ball_rect)
    

    


    
