import pygame
class Preferences:
    def __init__(self):
        self.icon = pygame.image.load(r'space.jpg')
        self.width = 1000
        self.height = 800
        self.bg_color = (255, 255, 255)

        # Jet settings
        self.jet_speed = 5
