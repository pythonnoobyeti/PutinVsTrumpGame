import pygame
from pygame.sprite import Sprite
from src.utils.game_function import resource_path

class Dollar(Sprite):
    '''Класс для доллара'''
    def __init__(self, trump, screen, ayf_settings):
        '''Инициализирует атрибуты'''
        #Инициализация класса родителя
        super().__init__()
        self.ayf_settings = ayf_settings
        self.trump = trump
        self.image = pygame.image.load(resource_path('src/images/dol.bmp'))
        self.rect = self.image.get_rect()
        
        #Определение начальных координат
        self.rect.left = self.trump.rect.left
        self.rect.centery = self.trump.rect.centery
        
        #Определение вещественной координаты
        self.x = float(self.rect.x)
        
    def update(self):
        '''Обновляет координаты долларов'''
        self.x -= self.ayf_settings.dollar_speed
        self.rect.x = self.x
    
    def blit(self):
        '''Выводит доллары на экран'''
        self.screen.blit(self.image, self.rect)
        
    
