import pygame
from src.utils.game_function import resource_path


class Putin():
    '''Класс создания Путина'''
    def __init__(self, screen, ayf_settings, sb):
        '''Инициализация атрибутов'''
        self.sb = sb
        self.screen = screen
        self.ayf_settings = ayf_settings
        self.putin_images = [pygame.image.load(resource_path('src/images/Putin_1.bmp')),
             pygame.image.load(resource_path('src/images/Putin_2.bmp')), 
             pygame.image.load(resource_path('src/images/Putin_3.bmp'))]
        self.image = self.putin_images[0]
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        #Параметры анимации
        self.count_fire = 0
        self.count_hit = 0
        
        #Определяем начальные координаты
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        
        #Определяем флаги для передвижений
        self.up = False
        self.down = False
        
        #Определяем вещественную координату
        self.y = float(self.rect.y)
        
    def update_putin(self):
        '''Обновление координат Путина(перемещение)'''
        if self.up and self.rect.top >= self.sb.surface.bottom:
            self.y -= self.ayf_settings.putin_speed_factor
            self.rect.y = self.y
        if self.down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.ayf_settings.putin_speed_factor
            self.rect.y = self.y
            
    
    def blit_putin(self):
        '''Функция для ывод на экран Путина'''
        self.screen.blit(self.image, self.rect)
        
        
