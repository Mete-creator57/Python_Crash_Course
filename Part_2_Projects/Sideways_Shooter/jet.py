import pygame
class Jet:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(r'jetfighter.png')
        self.rect = self.image.get_rect()

        # place in the midleft of the screen
        self.rect.midleft = self.screen_rect.midleft


    def blit_jet(self):
        """Draw the jet on the screen"""
        self.screen.blit(self.image, self.rect)


        
        
