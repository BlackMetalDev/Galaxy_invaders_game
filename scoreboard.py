import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """Класс для вывода игровой информации."""

    def __init__(self, ai_settings, screen, stats):
        """Инициализируем атрибуты подсчета очков."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Настройки шрифта для вывода счета.
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 30)

        # Подготовка исходного изображения.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Преобразуем текущий счет в графическое изображение."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render('Счет: ' + score_str, True,
            self.text_color, self.ai_settings.bg_color)
            
        # Отображение счета в верхнем правом углу экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """Преобразуем рекордный счет в графическое изображение."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render('Рекорд: ' + high_score_str, 
            True, self.text_color, self.ai_settings.bg_color)
                
        # Отображение рекорда вверду в центре экрана.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
        """Преобразуем уровень в графическое изображение."""
        self.level_image = self.font.render('Уровень: ' + str(self.stats.level), True,
                self.text_color, self.ai_settings.bg_color)
        
        # Отображение уровня под текущим счетом.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        """Показываем количество оставшихся кораблей."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
    def show_score(self):
        """Отрисовка счета на экране."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Отрисовка кораблей.
        self.ships.draw(self.screen)
