import pygame

class Ship():
	def __init__(self, ai_settings, screen):
	# Инициализация корабля.
	
		self.screen = screen
		
		# Загрузка изображения корабля.
		self.image = pygame.image.load('images/ship.png')
		
		# Получение прямоугольника(истинной формы корабля).
		self.rect = self.image.get_rect()
		
		# Прямоугольник экрана.
		self.screen_rect = screen.get_rect()
		
		# Новый корабль появляется в нижней средней части экрана.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# Флаги нажатия клавиш.
		self.moving_right = False
		self.moving_left = False
		
		self.ai_settings = ai_settings
		self.center = float(self.rect.centerx)

	def update(self):
	
		# Изменение позиции корабля при нажатии клавиш влево/вправо
		# с предотвращением выхода корабля за пределы экрана.
		if (self.moving_right and 
				self.rect.right < self.screen_rect.right):
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center
		
	def blitme(self):
	# Отрисовка корабля в текущей позиции.
		self.screen.blit(self.image, self.rect)
	