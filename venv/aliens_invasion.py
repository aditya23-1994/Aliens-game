import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group

def run_game():
    ai_settings = Settings()
    #Initalize pygame and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship.
    ship = Ship(ai_settings,screen)
    #Make a group to store bullet in.
    bullets = Group()

    #Start the main loop for the game.
    while True: 
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

        #getrid of bullet that have disappeared .
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)



run_game()