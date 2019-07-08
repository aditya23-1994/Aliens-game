import pygame
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    ai_settings = Settings()
    #Initalize pygame and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship.
    ship = Ship(ai_settings,screen)

    #Start the main loop for the game.
    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()