import pygame.font 

class Button:
    
    def __init__(self, ai_game, msg):
        """initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        #set the dimnsions and properties of the button.
        self.width, self.height = self.settings.button_width, self.settings.button_height
        self.color = self.settings.button_color
        self.text_color = self.settings.button_text_color
        self.font = self.settings.button_font

        #build the button's rect object and center it. 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #button message nees to be preped only once
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button """
        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        #Draw blank button and then draw message
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)