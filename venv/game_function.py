import sys
import pygame
from bullet import Bullet
from aliens import Alien
from time import sleep

def check_events(ai_settings, screen, ship, bullets):
    """Responds to key presses and mouse events """
    for event in pygame.event.get():
        if event.type   == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key   == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key   == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        """Create a new group and add it to the bullet group"""
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    elif event.key     == pygame.K_q:
        sys.exit()
def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right == False
    if event.key == pygame.K_LEFT:
        ship.moving_left == False

def update_bullets(ai_Settings, screen, ship, aliens, bullets):
    """updaate position of bullets and get rid of old bullets"""
    #UPDATE BULLET POSITION
    bullets.update()
    #get rid of bullets that have disappered.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        #Destroy existing bullet and create new fleet.
        bullet.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def update_screen(ai_settings, screen, ship, alien, bullets):
    # Redraw the screen during each pass through a loop
    screen.fill(ai_settings.bg_color)
    #Redraw all bullets behind the ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)
    # Make the most recen  t drawn screen visible.
    pygame.display.flip()
def get_number_alien_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x
def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of aliens that fits on to the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2* alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create full fleet of aliens"""
    #Create an alien and find the number of aliens in a row.
    #Spacing between each alien is equal to the number of alien width.
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows    = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #Create the frist row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
        #create an alien and  place it in a row.
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
def check_fleet_edges(ai_settings, aliens):
    """Respond appropratley if any alien reached to the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,stats, screen, ship, aliens, bullets):
    """Update position of the alien in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #Look for alien ship collision.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, aliens,ship, bullets)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by aliens"""
    if stats.ships_left > 0 :
    #Decrement ship_left.
        stats.ships_left -= 1

    #Empty the list of aliens & bullets.
        aliens.empty()
        bullets.empty()

    #Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

    #Pause
        sleep(0.5)

    else:
        stats.game_active = False
def check_aliens_bottom(ai_Settings, stats, screen, aliens, ship, bullets):
    """Check if the alien as reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, aliens, ship, bullets)
            break

