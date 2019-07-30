import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    ai_settings = Settings()
    #Initalize pygame and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship.A group of bullets & a group of aliens.
    ship = Ship(ai_settings,screen)

    #Create an instance to store the game statistics
    stats = GameStats(ai_settings)
    #Make a group to store bullet in.
    bullets = Group()
    aliens = Group()
    #Create the fleet of alien
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Start the main loop for the game.
    while True: 
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)





run_game()