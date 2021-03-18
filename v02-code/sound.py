import pygame

class Sound():
    """Класс для звуков в игре"""
    def __init__(self):
        """Инициализация"""
        #Основная тема игры
        pygame.mixer.music.load('sounds/main.mp3')
        self.putin_victory = pygame.mixer.Sound('sounds/putin_victory.ogg')

