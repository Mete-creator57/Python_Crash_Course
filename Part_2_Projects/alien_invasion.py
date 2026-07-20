# import sys module to exit the game
import sys
from settings import Settings
# import this to use it's functionality
import pygame
from ship import Ship 
from character_tiy_draw_center import Fighter
from rocket import Rocket

class AlienInvasion:
    
    def __init__(self):

        # init the bg settings for pygame to work properly
        pygame.init()

        

        # create an instance of the settigns class
        self.settings = Settings(bg_color=(135, 206, 235))
        
        self.is_fullscreen = False
        self.setup_screen_mode()
        
        
        
        # set the name of the game displaying window
        pygame.display.set_caption('Alien Game')
        
        # attribute as an Instance of the Class
        self.ship = Ship(self)
        self.fighter = Fighter(self)
        self.rocket = Rocket(self)

        # create an instance of the Clock class in pygame.time module
        # so the created instance can access all of the Clock's class methoods
        self.clock = pygame.time.Clock()
    


    def setup_screen_mode(self):
        """Set up the display mode based on config flags instead of console input"""
        if self.is_fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.window_height = self.screen.get_rect().height
            self.settings.window_width = self.screen.get_rect().width
        else:
            self.screen = pygame.display.set_mode((self.settings.window_width, 
                                                   self.settings.window_height))
    

        # MANAGE ALL EVENTS IN THE GAME

 
    def _check_events(self):
        """Manage all the events in the game"""
        # Watch for keyboard and mouse events

        # event.get() function returns the list of all events
        for event in pygame.event.get():

            # quit the game (close via cursor)
            if event.type == pygame.QUIT:  
                sys.exit() # the programm stops running

            # if player presses a button
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_ship(event)
                self._check_keydown_rocket_(event)

            
            # if player releases a key
            elif event.type == pygame.KEYUP:
                self._check_keyup_ship(event)
                self._check_keyup_rocket_(event)
                


    # ROCKET MOVEMENT CONTROL   

    def _check_keydown_rocket_(self, event):
        """Handle the rocket keydown events"""
        if event.key == pygame.K_d:
            msg = 'Moving right (Rocket)'
            print(msg)
            self.rocket.move_right = True
        elif event.key == pygame.K_a:
            print('Moving left (Rocket)')
            self.rocket.move_left = True
        elif event.key == pygame.K_w:
            print('Moving up (Rocket)')
            self.rocket.move_up = True
        elif event.key == pygame.K_s:
            msg = 'Moving down (Rocket)'
            print(msg)
            self.rocket.move_down = True

    def _check_keyup_rocket_(self, event):
        """Check for keyup events (when user doesn't hold or press the button)"""

        if event.key == pygame.K_d:
            self.rocket.move_right = False

        elif event.key == pygame.K_a:
            self.rocket.move_left = False

        elif event.key == pygame.K_w:
            self.rocket.move_up = False

        elif event.key == pygame.K_s:
            self.rocket.move_down = False

         
         
         
    # SHIP MOVEMENT CONTROL

    def _check_keydown_ship(self, event):
        """Check and handle the keydown events"""
        
        # exit the game via pressing Q
        if event.key == pygame.K_q:
            sys.exit()

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

        

    def _check_keyup_ship(self, event):
        """Check and handle KEYUP events"""
        # if user realeases pressing the button
        if event.key == pygame.K_RIGHT:
            # set the value to false
            self.ship.movement_right = False

        elif event.key == pygame.K_LEFT:
            # set the value to false
            self.ship.movement_left = False

        elif event.key == pygame.K_UP:
            # set the value to false
            self.ship.movement_up = False

        elif event.key == pygame.K_DOWN:
            # set the value to false
            self.ship.movement_down = False
            
    

            

    def _update_screen_(self):
        """Fill the screen with a specified bg color and draw the ship on the screen"""
        self.screen.fill(self.settings.bg_color)
            
        # draw the elements on to the screen
        self.ship.blit_draw()
        self.fighter.blit_fighter()
        self.rocket.blit_rocket()
        
        # draw the newest version of the screen
        pygame.display.flip()


    

    
    # GAME LOOP

    def run_game(self):
        """The main method where our game runs"""
        while True:
            self._check_events()
            self.ship.move_ship()
            self.rocket.move_rocket()
            self._update_screen_()
            self.clock.tick(self.settings.fps)
        
        
# if the file is called directly
if __name__ == '__main__':
    # create an instance of the created class
    game = AlienInvasion()

    # and call the main function for the game to start
    game.run_game()

