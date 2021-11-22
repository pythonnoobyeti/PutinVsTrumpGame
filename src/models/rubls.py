import pygame
from pygame.sprite import Sprite
from src.utils.game_function import resource_path


class Rub(Sprite):
    '''Класс для создания рублей, наследует от Sprite'''
    def __init__(self, putin, ayf_settings):
        '''Инициализация атрибутов'''
        #Инициализация атрибутов класса родителя
        super().__init__()
        self.putin = putin
        self.ayf_settings = ayf_settings
        self.image = pygame.image.load(resource_path('src/images/rub.bmp'))
        self.rect = self.image.get_rect()
        
        #Определение начальной координаты
        self.rect.center = self.putin.rect.center
        
        #Определение вещественной координаты
        self.x = float(self.rect.x)
        
    def update(self):
        '''Обновление координат рубля'''
        self.x += self.ayf_settings.rub_speed
        self.rect.x = self.x
        
        
