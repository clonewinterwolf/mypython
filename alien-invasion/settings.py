import pygame.font 

class Settings:
    """ Class to store all settings for Alien Invasion """

    def __init__(self):
        """ Initilize the games' settings """
        #Screen settings 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.caption = "Alien Invasion"
        
        #ship settings

        self.ship_limit = 3
        
        #bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_color = (238,130,238)
        self.bullet_allowed = 3

        #alien settings

        self.fleet_drop_speed = 5.0

        #alien bomb settings
     
        self.bomb_width = 4
        self.bomb_height = 20
        self.bomb_color = (233,0,0)
        self.bomb_allowed = 10

        #button settings
        self.button_color = (100, 105, 100)
        self.button_width = 200 
        self.button_height = 50
        self.button_text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont(None, 48) 

        #scoreboard settings
        self.sb_text_color = (30, 30, 30)
        self.sb_font = pygame.font.SysFont(None, 48)

        #game speed setting
        self.speed_scale = 1.1
    
    def initialize_dynamic_settings(self):
        """initilize settings that changes through the game. reset"""
        self.ship_speed = 1.5
        self.bomb_speed = 2
        self.alien_speed = 1.0
    
        #1 prepresent right, -1 left 
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings """
        self.bomb_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale


        
        
        
        

