import pygame
from src.utils.game_function import resource_path


class Trump():
    '''Класс для Трампа'''
    def __init__(self, screen, ayf_settings, statistic):
        '''Инициализация атрибутов'''
        self.statistic = statistic
        self.trump_images = [pygame.image.load(resource_path('src/images/Trump_1.bmp')),
             pygame.image.load(resource_path('src/images/Trump_2.bmp'))]
        self.image = self.trump_images[0]
        self.screen = screen
        self.ayf_settings = ayf_settings
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        #Параметры анимации при попадении
        #Задержка для анимации. При активации анимации обнуляется и 
        #начинает набирать значение
        self.count_hit = 0
        #Задержка для изменения координат во втором режиме
        self.i = 300
        
        #Определение начального положения
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right
        
        #Определение вещественной координаты
        self.y = float(self.rect.y)
            
    def blit_trump(self):
        '''Вывод Трампа на экран'''
        self.screen.blit(self.image, self.rect)
        
        

