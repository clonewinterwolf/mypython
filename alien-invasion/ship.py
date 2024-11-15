import pygame

class Ship:
    """ Class for user's ship """
    def __init__(self, ai_game):
        """ initilize the ship and set its starting position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start new ship at the bottom centoer of the screen 
  
        self.rect.midbottom = self.screen_rect.midbottom
        #store decimal value of ship original location
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        """ draw the shp at its current location """
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """ Update the ship's position based on movement flag. """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """ center the ship on the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

