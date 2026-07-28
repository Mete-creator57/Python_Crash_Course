class Settings:

    def __init__(self, height: int = 800, width: int = 1200, bg_color: tuple = (230, 230, 230)):

        self.window_height = height
        self.window_width = width
        self.bg_color = bg_color
        self.fps = 60

        # ship settings
        self.ship_speed = 10
        self.rocket_speed = 20

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 # limit the bullets number