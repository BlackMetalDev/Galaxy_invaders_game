import sys
import pygame
from bullet import Bullet
	
def check_events(ai_settings, screen, ship, bullets):
# Обработка нажатий клавиш
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
# При нажатии клавиши вызывается данная функция
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
# При отпускании клавиши вызывается данная функция
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
		
def update_screen(ai_settings, screen, ship, bullets):
	# Назначение цвета фона.
	screen.fill(ai_settings.bg_color)
	
	# Отрисовка пуль.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	# Отрисовка корабля в текущей позиции.
	ship.blitme()
	
	# Обновление изображения на экране.
	pygame.display.flip()

def update_bullets(bullets):
	# Обновление позиций пуль и удаление пуль вышенших за предел экрана.
	bullets.update()
	for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
	
def fire_bullet(ai_settings, screen, ship, bullets):
	# Сделать выстрел, если максимум пуль на экране еще не достигнут.
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)
