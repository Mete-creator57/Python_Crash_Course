import pygame
import sys
class Empty_Game:
    def __init__(self, width, height):
        # always use pygame.init() for pygame to work correctly
        pygame.init()
        self.screen = pygame.display.set_mode((height, width))
        pygame.display.set_caption('Test the keys')

        self.clock = pygame.time.Clock()

    def _update_screen_(self):
        self.screen.fill((100, 100, 100))
        # draw the newest version of the screen
        pygame.display.flip()
    
    # detect all keydown events (pressed keys or buttons)
    def detect_keydown_events(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('Key: W was detected by the system')
            




    def main_loop(self):
        is_active = True
        while is_active:
            self._update_screen_()
            for event in pygame.event.get():
                self.detect_keydown_events(event)

            self.clock.tick(30)


empty_game = Empty_Game(100, 1080)

empty_game.main_loop()
