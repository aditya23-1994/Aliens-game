import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Responds to key presses and mouse events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        """Create a new group and add it to the bullet group"""
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right == False
    if event.key == pygame.K_LEFT:
        ship.moving_left == False


def update_screen(ai_settings, screen, ship, bullets):
    # Redraw the screen during each pass through a loop
    screen.fill(ai_settings.bg_color)
    #Redraw all bullets behind the ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Make the most recent drawn screen visible.
    pygame.display.flip()