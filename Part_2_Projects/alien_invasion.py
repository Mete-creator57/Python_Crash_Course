# import sys module to exit the game
import sys

# import this to use it's functionality
import pygame

class AlienInvasion:
    
    def __init__(self):

        # init the bg setting for pygame to work properly
        pygame.init()
        
        # set the bg color
        self.bg_color = (230, 230, 230)

        # set the game window size (width, high) 
        # def the size in the tuple
        self.screen = pygame.display.set_mode((1200, 800))

        # set the name of the game displaying window
        pygame.display.set_caption('Alien Game')

        # create an instance of the Clock class in pygame.time module
        # so the created instance can access all of the Clock's class methoods
        self.clock = pygame.time.Clock()


    def run_game(self):
        """The main method where our game runs"""

        while True:
            # Watch for keyboard and mouse events
            # the event loop (every action performed by the user == event)

            # event.get() function returns the list of all events
            for event in pygame.event.get():
                # detect the event
                # if the player clicks the x button to close the game
                if event.type == pygame.QUIT:  
                    sys.exit() # the programm stops running
        
            # redraw the screen during the each pass through the loop
            self.screen.fill(self.bg_color)


            # at the end of each itearation of the while loop
            # this function makes the most revcently drawn screen visible
            # deleting the old one and replacing it with the new one
            pygame.display.flip()
            # set the fps to 60
            self.clock.tick(60)
        
# if the file is called directly
if __name__ == '__main__':
    # create an instance of the created class
    ai = AlienInvasion()

    # and call the main function for the game to start
    ai.run_game()

