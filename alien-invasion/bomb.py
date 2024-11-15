import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):
    """ a class to manage bullets fired from teh ship """
    def __init__(self, ai_game, alien):
        """ create a bullet object at the ships' current position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.color = self.settings.bomb_color

        #create bullet rectangle at (0,0) and set correct postion. 
        self.rect = pygame.Rect(0, 0, self.settings.bomb_width, self.settings.bomb_height)
        self.rect.midbottom = alien.rect.midbottom
        #store bullet's position as decimal value
        self.y = float(self.rect.y) 

    def update(self):
        """ move the bomb down the screen. """
        self.y += self.settings.bomb_speed
        self.rect.y = self.y

    def draw_bomb(self):
        """draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
