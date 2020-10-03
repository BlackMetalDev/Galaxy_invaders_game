import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship

def run_game(): 

    # Инициализация микшера до инициализации самого Pygame
    # позволяет избавиться от задержки звуков.
    pygame.mixer.pre_init(44100, -16, 2, 2048)

    # Инициализация игры и создание графического окна.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Galaxy Invasion")

    # Загрузка фонового изображения.
    bg = pygame.image.load("images/space_background.png").convert()

    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")
    
    # Создание экземпляров для хранения игровой статистики и очков.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Создание корабля, группы пуль и группы пришельцев.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Основной цикл игры.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
            bullets, play_button, bg)

run_game() 

