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
        self.small_ship_image = pygame.image.load('images/small_ship.png')
        
        # Настройки шрифта для вывода счета.
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 30)

        # Подготовка исходного изображения.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Преобразуем текущий счет в графическое изображение."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render('Счет: ' + score_str, True,
            self.text_color, self.ai_settings.bg_color)
            
        # Отображение счета в верхнем правом углу экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 300
        self.score_rect.top = 12
        
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
        
        # Отображение уровня.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + self.small_ship_image.get_rect().width * 11
        self.level_rect.top = self.score_rect.top

    def show_score(self):
        """Отрисовка счета на экране."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Отрисовка оставшихся кораблей.
        for ship_number in range(self.stats.ships_left):
            self.screen.blit(self.small_ship_image, 
                (10 + ship_number * 1.5 * self.small_ship_image.get_rect().width, 8))