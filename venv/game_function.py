import sys
import pygame

def check_events(ship):
    """Responds to key presses and mouse events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right == False
                if event.key == pygame.K_LEFT:
                    ship.moving_left == Flase

            if event.key == pygame.K_LEFT:
                ship.moving_left == False

def update_screen(ai_settings, screen, ship):
    # Redraw the screen during each pass through a loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Make the most recent drawn screen visible.
    pygame.display.flip()