import pygame

class Field():
    '''Класс для области вокруг трампа'''
    def __init__(self, trump, screen):
        '''Инициализация основных параметров'''
        self.trump = trump
        self.screen = screen
        
        #Создаём поверхность
        self.rect = pygame.Rect(0, 0, 200, 200)
        self.rect.centerx = self.trump.rect.centerx
        self.rect.centery = self.trump.rect.centery
    
    def update_field(self):
        self.rect.centerx = self.trump.rect.centerx
        self.rect.centery = self.trump.rect.centery
        
        
