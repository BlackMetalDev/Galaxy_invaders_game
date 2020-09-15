import pygame
import game_functions as gf
from pygame.sprite import Group
from ship import Ship
from settings import Settings

def run_game():
	pygame.init()
	ai_settings = Settings()
	
	# Размер (разрешение) окна игры.
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))	
	pygame.display.set_caption("Galaxy")
	
	# Создание корабля.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	
	# Основной цикл игры.
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()



