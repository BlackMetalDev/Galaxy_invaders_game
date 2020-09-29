class Settings():
    """Класс для хранения настроек игры."""

    def __init__(self):
        """Инициализируем статические настройки игры."""
        # Настройки экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        # Настройки корабля.
        self.ship_limit = 3
            
        # Настройки пуль.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 200, 200, 200
        self.bullets_allowed = 200
        
        # Настройки пришельцев.
        self.fleet_drop_speed = 10
            
        # Темп ускорения игры.
        self.speedup_scale = 1.1

        # Темп увеличения награды (очков) за уничтожение пришельца.
        self.score_scale = 1.5
    
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализируем настройки, изменяющиеся по ходу игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        # Подсчет очков.
        self.alien_points = 50
    
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Увеличивает настройки скорости и награду (очки) за уничтожение пришельца."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)