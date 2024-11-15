import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    """ Class for alien """
    def __init__(self, ai_game):
        """ initilize the alien and set its starting position """
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load the alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start new alien at the bottom centoer of the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store a decimal value for the alien s orginal horizontal position. to keep speed same for moving left and right. 
        self.x = float(self.rect.x)
        #self.y = self.rect.y

        #movement flag
        #self.moving_right = False
        #self.moving_left = False
        #self.moving_up = False
        #self.moving_down = False
    
    def check_edges(self):
        """return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            #print(f"{self.settings.fleet_direction} hit edge")
            return True

    def update(self):
        """Move alient to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x