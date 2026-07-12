import pygame

class Fighter:
    """Manage the fighter"""
    def __init__(self, ai_instance):
        """Init the attributes"""
        
        # let the class know with what screen it's interacting
        self.screen = ai_instance.screen
        
        # shape the form of a screen (rectangle)
        self.screen_rect = self.screen.get_rect()
        
        # upload the image of the ship and save it in a variable
        self.fighter_image = pygame.image.load(r'images\fighter.bmp')
        
        # set the fighter shape (rectangle)
        self.fighter_rect = self.fighter_image.get_rect()
        
        # place the fighter (rectangle) at the center of the screen shape
        # which is a rectangle as well
        # align with the center of the screen form (rect)
        self.fighter_rect.center = self.screen_rect.center

    def blit_fighter(self):
        """Display the fighter image on the screen"""
        self.screen.blit(self.fighter_image, self.fighter_rect)

        