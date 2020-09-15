class Settings():
	
	# Класс для хранения настроек игры.
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (120, 120, 120)
		self.bullets_allowed = 3
