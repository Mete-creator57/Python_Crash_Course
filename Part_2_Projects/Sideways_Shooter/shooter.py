# to exit the game
import sys 
# to manage the game
import pygame
# to group elements
from pygame import sprite # This is okay, but `pygame.sprite.Group` is more explicit
from jet import Jet
from preferences import Preferences
from fire import Fire_Ball
from star import Star

class Shooter_Game:
    """Class to manage the game"""
    def __init__(self):
        pygame.init()

        self.preferences = Preferences()

        self.screen = pygame.display.set_mode((self.preferences.width, 
                        self.preferences.height))
        self.screen_rect = self.screen.get_rect()

        self.jet = Jet(self)
        self.fireballs = pygame.sprite.Group() # Group to hold all active fireballs
        self.stars = pygame.sprite.Group()

        pygame.display.set_caption('Sideways Shooter')
        pygame.display.set_icon(self.preferences.icon)

        self._create_stars_()

        self.clock = pygame.Clock()


    def _create_stars_(self):
        """Create a grid of stars, ensuring they don't overlap with the jet's starting position."""
        # Create a dummy star to get dimensions without adding it to the group
        dummy_star = Star(self)
        star_width, star_height = dummy_star.rect.size

        # --- Calculate where stars should start to avoid the jet ---
        # Get the jet's initial right edge (it's initialized before _create_stars_ is called)
        jet_safe_zone_right_edge = self.jet.rect.right + (2 * star_width) # Add some padding
        # Calculate how many stars can fit horizontally, starting from `jet_safe_zone_right_edge`
        # and going to the right edge of the screen.
        available_space_x_for_stars = self.preferences.width - jet_safe_zone_right_edge

        # Ensure we don't divide by zero or negative if spacing is too small
        if (2 * star_width) <= 0: # Prevent division by zero if star_width somehow becomes 0
            number_stars_x = 0
        else:
            number_stars_x = available_space_x_for_stars // (2 * star_width)

        # --- Calculate vertical placement (as before) ---
        available_space_y = self.preferences.height - (2 * star_height)
        if (2 * star_height) <= 0: # Prevent division by zero
            number_rows = 0
        else:
            number_rows = available_space_y // (2 * star_height)

        # --- Create stars in the calculated grid ---
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                    new_star = Star(self)

                # Calculate X position: Start from the safe zone and add spacing
                    new_star.x = jet_safe_zone_right_edge + 2 * star_width * star_number
                    new_star.rect.x = new_star.x

                    # Calculate Y position
                    new_star.y = star_height + 2 * star_height * row_number
                    new_star.rect.y = new_star.y
               
                    self.stars.add(new_star)

    # DRAW ALL ELEMENTS ON THE SCREEN
    def _update_screen_(self):
        """Update the screen"""
        # Fill the screen with a color
        self.screen.fill(self.preferences.bg_color)

        # Draw the jet
        self.jet.blit_jet()

        self.stars.draw(self.screen)

        # Draw each fireball in a list on the screen
        for fireball in self.fireballs.sprites():
            fireball.blit_ball()
        

        # Replace the old screen with a new one
        pygame.display.flip()
    
    def _add_fireball(self):
        """Create a new fireball 
        and add it to the fireballs group only if there are less than 2 already."""
        if len(self.fireballs) < 2:
            new_fireball = Fire_Ball(self, self.jet) # Pass game and the jet object
            self.fireballs.add(new_fireball)
        
        
    def _check_events(self):
        """Check all events in the game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Keydown events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.jet.move_up = True
                elif event.key == pygame.K_DOWN:
                    self.jet.move_down = True
                elif event.key == pygame.K_SPACE:
                    self._add_fireball() # Call the method to create a new fireball

            # Keyup events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.jet.move_up = False
                elif event.key == pygame.K_DOWN:
                    self.jet.move_down = False
                
    def run_game(self):
        is_active = True
        while is_active:
            self._check_events()

            # Update jet position based on its flags
            self.jet.update()
            self.fireballs.update()

            self._update_screen_()
            # Set the frame rate to 60 per second
            self.clock.tick(60) 

if __name__ == '__main__':
    game = Shooter_Game()
    game.run_game()

