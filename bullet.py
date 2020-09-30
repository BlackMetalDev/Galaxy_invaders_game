import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями."""

    def __init__(self, ai_settings, screen, ship):
        """Создает объект пули в текущей позиции корабля."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Загрузка изображения пули.
        self.image = pygame.image.load('images/bullet.png')

        # Создает прямоугольник пули в (0, 0), затем задает ему корректную позицию.
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        #    ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Позиция пули.
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Обновление позиции пули."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Отрисовка пули."""
        #pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)