import pygame
from src.utils.game_function import resource_path


class Sound():
    """Класс для звуков в игре"""
    def __init__(self):
        """Инициализация"""
        #Основная тема игры
        pygame.mixer.music.load(resource_path('src/sounds/main.mp3'))
        self.putin_victory = pygame.mixer.Sound(resource_path('src/sounds/putin_victory.ogg'))

