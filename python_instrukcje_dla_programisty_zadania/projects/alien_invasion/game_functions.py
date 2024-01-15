import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Reakcja na zdarzenia generowane przez klawiature i mysz"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Rozpoczecie nowej gry po kliknieciu przycisku Gra"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)


def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Wyzerowanie ustawien dotyczacych gry
    ai_settings.initialize_dynamic_settings()

    # Ukrycie kursora myszy
    pygame.mouse.set_visible(False)

    # Wyzerowanie danych gry
    stats.reset_stats()
    stats.game_active = True

    # Wyzerowanie obrazow tablicy wynikow
    sb.prep_images()

    # Usuniecie zawartosci list aliens i bullets
    aliens.empty()
    bullets.empty()

    # Utworzenie nowej floty i wysrodkowanie statku
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Reakcja na nacisniecie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        ship_fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_s:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    """Reakcja na zwolnienie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Uaktualnienie obrazow na ekranie i przejscie do nowego ekranu"""
    # Odswiezenie ekranu w trakcie kazdej iteracji petli
    screen.fill(ai_settings.bg_color)

    # Ponowne wyswietlenie wszystkich pociskow pod warstwami statku kosmicznego i obcych
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Wyswietlenie informacji o punktacji
    sb.show_score()

    # Wyswietlenie przycisku tylko wtedy, gdy gra jest nieaktywna
    if not stats.game_active:
        play_button.draw_button()

    # Wyswietlenie ostatnio uaktualnionego ekranu
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Uaktualnienie polozenia pociskow i usuniecie tych niewidocznych na ekranie"""
    # Uaktualnienie polozenia pociskow
    bullets.update()

    # Usuniecie pociskow, ktore znajduja sie poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Reakcja na kolizje miedzy pociskiem i obcym"""

    # Usuniecie wszystkich pociskow i obcych, miedzy ktorymi doszlo do kolizji
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        # Jezeli cala flota zostala zniszczona, gracz przechodzi na kolejny poziom
        start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets)


def start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Przygotowanie nowego poziomu
    bullets.empty()
    ai_settings.new_level_settings()

    # Inkrementacja numeru poziomu
    stats.level += 1
    sb.prep_level()
    create_fleet(ai_settings, screen, ship, aliens)


def ship_fire_bullet(ai_settings, screen, ship, bullets):
    """Wystrzeliwanie pocisku, jesli nie przekroczono ustalonego limitu"""
    # Utworzenie nowego pocisku i dodanie go do grupy pociskow
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """Utworzenie pelnej floty obcych"""
    # Utworzenie obcego i ustalenie liczby obcych, ktorzy zmieszcza sie w rzedzie
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Utworzenie pierwszego rzedu obcych
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """Ustalenie liczby obcych, ktorzy zmieszcza sie w rzedzie"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Utworzenie obcego i umieszczenie go w rzedzie"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Ustalenie, ile rzedow obcych zmiesci sie na ekranie"""
    available_space_y = (ai_settings.screen_height - (4 * alien_height)) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Sprawdzenie, czy flota znajduje sie przy krawedzi ekranu,
    a nastepnie uaktualnienie polozenia wszystkich obcych we flocie"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Wykrywanie kolizji miedzy obcym i statkiem
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Wyszukiwanie obcych docierajacych do dolnej krawedzi ekranu
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def change_fleet_direction(ai_settings, aliens):
    """Przesuniecie calej floty w dol i zmiana kierunku, w ktorym sie porusza"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """Odpowiednia reakcja, gdy obcy dotrze do krawedzi ekranu"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Sprawdzenie, czy ktorykolwiek obcy dotarl do dolnej krawedzi ekranu"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Reakcja na uderzenie obcego w statek"""
    if stats.ships_left > 0:
        # Zmniejszenie wartosci przechowywanej w ship_left
        stats.ships_left -= 1

        # Uaktualnienie tablicy wynikow
        sb.prep_ships()

        # Usuniecie zawartosci list aliens i bullets
        aliens.empty()
        bullets.empty()

        # Utworzenie nowej floty i wysrodkowanie statku
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pauza
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_high_score(stats, sb):
    """Sprawdzenie, czy mamy nowy najlepszy wynik w grze"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
        sb.save_hs_to_file(stats.high_score)
