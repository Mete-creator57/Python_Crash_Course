# to exit the game
import sys 
# to manage the game
import pygame
# to group elements
from pygame import sprite 
from jet import Jet
from preferences import Preferences
from fire import Fire_Ball

class Shooter_Game:
    """Class to manage the game"""
    def __init__(self):
        pygame.init()

        self.preferences = Preferences()

        self.screen = pygame.display.set_mode((self.preferences.width, 
                        self.preferences.height))
        self.screen_rect = self.screen.get_rect()

        self.jet = Jet(self)
        self.fire_ball = Fire_Ball(self, self.jet)

        pygame.display.set_caption('Sideways Shooter')
        pygame.display.set_icon(self.preferences.icon)
        self.clock = pygame.Clock()

    def _update_screen_(self):
        """Update the screen"""
        # Fill the screen with a color
        self.screen.fill(self.preferences.bg_color)

        # draw the jet on to the 
        self.jet.blit_jet()
        self.fire_ball.blit_ball()

        # replace the old screen with a new one
        pygame.display.flip()

    def _check_events(self):
        """Check all events in the game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Keydown events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.jet.move_up = True # Set flag to True
                elif event.key == pygame.K_DOWN: # Use elif for mutually exclusive keys
                    self.jet.move_down = True # Set flag to True
                elif event.key == pygame.K_SPACE:
                    self.fire_ball.move = True

            # Keyup events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.jet.move_up = False # Set flag to False
                elif event.key == pygame.K_DOWN: # Use elif for mutually exclusive keys
                    self.jet.move_down = False # Set flag to False
                

    def run_game(self):
        is_active = True
        while is_active:
            self._check_events() # check the events 

            # update ball and jet positions based on their flags
            self.jet.update() # Call the jet's update method here
            self.fire_ball.update() 

            self._update_screen_()
            # set the frame rate to 60 per second
            self.clock.tick(60) 

if __name__ == '__main__':
    game = Shooter_Game()
    game.run_game()
