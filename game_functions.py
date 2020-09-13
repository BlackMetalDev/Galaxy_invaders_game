import sys
import pygame

def check_events(ship):
# Обработка нажатий клавиш
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()

def check_keydown_events(event, ship):
# При нажатии клавиши вызывается данная функция
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

def check_keyup_events(event, ship):
# При отпускании клавиши вызывается данная функция
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
		
def update_screen(ai_settings, screen, ship):
	# Назначение цвета фона.
	screen.fill(ai_settings.bg_color)
	
	# Отрисовка корабля в текущей позиции.
	ship.blitme()
	
	# Обновление изображения на экране.
	pygame.display.flip()

	
