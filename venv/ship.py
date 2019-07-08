import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get it's rect.
        self.image = pygame.image.load('C:/Users/hp/PycharmProjects/alien_invasion_game/images/adding_ship_image/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start ecah ship from the bottom.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship center.
        self.center = float(self.rect.centerx)

        #Movement Flag.
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """Update the ship position based on the moving flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #Update the rect objectfrom self.center
        self.rect.centerx = self.center
            
    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)