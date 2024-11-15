import pygame.font

class Scoreboard:
    """ class to report scoring information """

    def __init__(self, ai_game):
        """initialize scorekeeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.font = self.settings.sb_font

        self.prep_score()

    def prep_score(self):
        """ turn score into a rendered image. """
        score_str = "Score: " + str(self.stats.score) + "\r\n Aliens Killed: " + str(self.stats.enemykilled)
        self.score_image = self.font.render(score_str, True, self.settings.sb_text_color, self.settings.bg_color)

        #display the score at top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20 
    
    def show_score(self):
        """draw score to the screen """
        self.screen.blit(self.score_image, self.score_rect)

        
