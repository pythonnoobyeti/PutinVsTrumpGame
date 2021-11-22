import pygame.font
from src.utils.game_function import resource_path

class Button():
    '''Класс кнопки пуска игры'''
    def __init__(self, screen, msg):
        '''Инициализация атрибутов'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #Параметры кнопки
        self.width = 100
        self.height = 100
        self.text_color = (100, 14, 82)
        self.bg_color = (115, 89, 28)
        #Создание экземпляра типа font
        
        #Создание прямоугольника, относительно которого происходит выравнивание
        #кнопки
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.image = pygame.image.load(resource_path('src/images/play.bmp'))
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = self.rect.centerx
        self.image_rect.centery = self.rect.centery
        
        #Функция отрисовки кнопки
        self.buttom_render(msg)
        
    def buttom_render(self, msg):
        '''Создаёт изображение кнопки и определяет её положение'''
        pass
    
    def blit(self):
        '''Выводит на экран прямоугольник и изображение кнопки'''
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.image, self.image_rect)
