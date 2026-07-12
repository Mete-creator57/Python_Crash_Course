# import sys module to exit the game
import sys
from settings import Settings
# import this to use it's functionality
import pygame
from ship import Ship 
from character_tiy_draw_center import Fighter

class AlienInvasion:
    
    def __init__(self):

        # init the bg setting for pygame to work properly
        pygame.init()

        # create an instance of the settigns class
        self.settings = Settings(bg_color=(135, 206, 235))
        
       
        

        # set the game window size (width, high) 
        # def the size in the tuple
        self.screen = pygame.display.set_mode((self.settings.window_width,
         self.settings.window_height))

        # set the name of the game displaying window
        pygame.display.set_caption('Alien Game')
        
        # attribute as an Instance of the Classes
        self.ship = Ship(self)
        self.fighter = Fighter(self)

        # create an instance of the Clock class in pygame.time module
        # so the created instance can access all of the Clock's class methoods
        self.clock = pygame.time.Clock()

    def _check_events(self):
        """Manage all the events in the game"""
        # Watch for keyboard and mouse events
        # the event loop (every action performed by the user == event)

        # event.get() function returns the list of all events
        for event in pygame.event.get():
            # if the player clicks the x button to close the game
            if event.type == pygame.QUIT:  
                sys.exit() # the programm stops running

            # if the game detects a user input
            elif event.type == pygame.KEYDOWN:

                # check the movement on X axis
                if event.key == pygame.K_RIGHT:
                    # set the flag's value
                    self.ship.movement_right = True

                elif event.key == pygame.K_LEFT:
                    self.ship.movement_left = True
                
                # check the movement on Y axis
                elif event.key == pygame.K_UP:
                    self.ship.movement_up = True

                elif event.key == pygame.K_DOWN:
                    self.ship.movement_down = True
            
            # if user realeases pressing the button
            elif event.type == pygame.KEYUP:
                # if it was the right key
                if event.key == pygame.K_RIGHT:
                    # set the value to false
                    self.ship.movement_right = False
                if event.key == pygame.K_LEFT:
                    # set the value to false
                    self.ship.movement_left = False
                if event.key == pygame.K_UP:
                    # set the value to false
                    self.ship.movement_up = False
                if event.key == pygame.K_DOWN:
                    # set the value to false
                    self.ship.movement_down = False




            
            

    def _update_screen_ship(self):
        """Fill the screen with a specified bg color and draw the ship on the screen"""
        # redraw the screen during the each pass through the loop
        self.screen.fill(self.settings.bg_color)
            
        # draw the ship at the bottom center
        self.ship.blit_draw()

        self.fighter.blit_fighter()
        
        # draw the newest version of the screen
        pygame.display.flip()



    def run_game(self):
        """The main method where our game runs"""

        while True:
            # first, check the events to detect what's happening right now
            self._check_events()

            # update the movement of the ship
            self.ship.update_movement()

            # draw both fighter and ship and update the screen
            self._update_screen_ship()

            # set the fps to 60
            self.clock.tick(self.settings.fps)
        
        
# if the file is called directly
if __name__ == '__main__':
    # create an instance of the created class
    ai = AlienInvasion()

    # and call the main function for the game to start
    ai.run_game()

