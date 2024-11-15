import sys

import pygame

import random


from time import sleep

from pygame.constants import USEREVENT

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from bomb import Bomb
from scoreboard import Scoreboard

class AlienInvasion:
    """Overall class to manage game assest and behavior. """

    def __init__(self):
        """initialize the game and create game resource. """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.BOMBDROPEVENT = pygame.USEREVENT + 1
     
        pygame.display.set_caption(self.settings.caption)

        #initilize ship
        self.ship = Ship(self)
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
     
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self._create_fleet()

        #make play button. 
        self.play_button = Button(self, "Play")

    def run_game(self):
        """start the main loop for the game. """
        #self.ship.blitme()
  
        pygame.time.set_timer(self.BOMBDROPEVENT, 6000)
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_bombs()
            
            self._update_screen()


    def _check_events(self):
        """respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_visible(True)
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.K_p and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                 self._reset_game()            
            elif event.type == self.BOMBDROPEVENT:
                self._drop_bomb()
            

    def _update_screen(self):
        #redra the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        #draw ship
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #draw the score info
        self.sb.show_score();

        for bomb in self.bombs.sprites():
            bomb.draw_bomb()
        
        if not self.stats.game_active:
            self.play_button.draw_button()
        #make the most recently drawn screen visible
        pygame.display.flip()


    def _check_keydown_events(self, event):
        """response to key press"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        
        if event.key == pygame.K_r:
            self._reset()

        if event.key == pygame.K_q: 
            sys.exit()

    def _check_keyup_events(self, event):
        """response to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _check_play_button(self, mouse_pos):
        """start a new game when user click play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked  and not self.stats.game_active: #play button area only active when game is not active 
            self.settings.initialize_dynamic_settings()
            self._reset_game()
            #hid hte mouse cursor
            pygame.mouse.set_visible(False)
            self.sb.prep_score()

    def _fire_bullet(self):
        """ create a bullet and add it to the bullets group. """
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update position of bullets and get rid of old bullets"""
        self.bullets.update()
        
        #get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collision()


    def _check_bullet_alien_collision(self):
        """check bullet and alien collision """
        # check for any bullets that have hit aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.stats.enemykilled += 1 *  len(aliens)
            self.sb.prep_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()


    def _create_alien(self, alien_number, row_number):
        #create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2* alien_height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """create teh fleet of aliens """
        #Make an alien and find the number of aliens in a row
        #spacing between each alien is equal to one alien width 
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        #determin the number of rows of aliens that fit on the screen 
        ship_height = self.ship.rect.height
        alien_height = alien.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        #create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number,row_number)

    def _check_fleet_edges(self):
        """ respond appropriately if any aliens have reached an edge """
        for alien in self.aliens.sprites():   
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """drop the entire fleet and change the fllet's direction. """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """check if the fleet at at an edge and then update position of aliens group"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #look for aliens hitting the bottom
        self._check_aliens_bottom()


    def _ship_hit(self):
        """ respond to ship being hit by an alien """
        self.stats.ships_left -= 1
        print(f"ship left: {self.stats.ships_left}")
        if self.stats.ships_left > 0:
            self.ship.center_ship()
            #get rid of any alian and bullets
            self.aliens.empty()
            self.bullets.empty()
            self.bombs.empty()
        
            #create new fleet and center the ship
            self._create_fleet()
            sleep(1)
        else:
            self.stats.game_active = False
            print("Game Over")
    
    def _check_aliens_bottom(self):
        """ check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
        

    def _drop_bomb(self):
        """ Aliens drop bombs """ 
        for alien in self.aliens.sprites():
            if random.getrandbits(1): #ready to drop a bomb 
                if len(self.bombs) < self.settings.bomb_allowed:
                    new_bomb = Bomb(self, alien)
                    self.bombs.add(new_bomb)
                    print(f"bomb {len(self.bombs)}")


    def _update_bombs(self):
        """update position of bullets and get rid of old bullets"""
        self.bombs.update()

        #get rid of bombs that have disappeared
        for bomb in self.bombs.copy():
            if bomb.rect.bottom >= self.screen.get_rect().height: 
                self.bombs.remove(bomb)
                print("bomb disappeared")
        self._check_bomb_ship_collision()
        
    def _check_bomb_ship_collision(self):
        """check bomb and ship collision """
        # check for any bombs that have hit ship
        if pygame.sprite.spritecollideany(self.ship, self.bombs):
            self._ship_hit()


    def _reset_game(self):
        """ Reset everything to begining """    
        self.stats.game_active = True
        self.stats.reset_stats()
        self._clear_screen()
        
    def _clear_screen(self):
        """clear all moving part """
        self.bullets.empty()
        self.aliens.empty()
        self.bombs.empty()
        self._create_fleet()
        self.ship.center_ship()

#called when the file is called directly
if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
