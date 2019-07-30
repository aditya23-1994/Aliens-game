import pygame as py
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullet fired from ship"""
    def __init__(self, ai_settings, screen, ship):
        """Creates a bullet object at the ship's current position """
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a bullet at rect(0, 0) and then set the currect position.
        self.rect = py.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = self.rect.bottom
        self.rect.top = self.rect.top
        self.rect.y = self.rect.height

        #store the bullet position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up te screen."""
        #Update the decimal position of the .
        self.y -= self.speed_factor
        #Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        py.draw.rect(self.screen, self.color, self.rect)
