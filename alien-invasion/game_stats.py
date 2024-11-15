class GameStats:
    """ track statistics for alien Invasion. """

    def __init__(self, ai_game):
        """ initialize statistics. """
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state till play button is pressed
        self.game_active = False


    def reset_stats(self):
        """ initilize statistics that can change during the game """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.enemykilled = 0