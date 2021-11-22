import pygame

class Statistic():
    '''Класс для ведения игровой статистики'''
    def __init__(self, ayf_settings):
        '''Инициализация параметров'''
        self.ayf_settings = ayf_settings
        #Функция для сброса параметров
        self.reset_game()
    
    def reset_game(self):
        '''Сбрасывает параметры'''
        self.trump_limit = self.ayf_settings.trump_limit
        self.putin_limit = self.ayf_settings.putin_limit
        self.dollars_limit = self.ayf_settings.dollars_limit
        self.q = self.ayf_settings.q
        self.w = self.ayf_settings.w
        self.f = self.ayf_settings.f
