class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Инициализируем статистику, изменяющуюся в ходе игры."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Игра запускается в неактивном состоянии.
        self.game_active = False
        
        # Рекорд 
        self.high_score = 0
        
    def reset_stats(self):
        """Инициализируем статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
