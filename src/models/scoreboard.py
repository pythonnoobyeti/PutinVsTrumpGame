import pygame
import pygame.font
from pygame.sprite import Group
from src.models.putin_small import Putin_small
from src.models.trump_small import Trump_small

class ScoreBoard():
    '''Класс для вывода статистики'''
    def __init__(self, statistic, screen, ayf_settings):
        '''Инициализация атрибутов'''
        self.statistic = statistic
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ayf_settings = ayf_settings
        self.update_putin_life()
        self.update_trump_life()
        #Создание полосы статистики
        self.surface = pygame.Rect(0, 0, self.ayf_settings.sc_width, 60)
    
    def update_putin_life(self):
        '''Обновляет количество жизней путина'''
        self.putins = Group()
        for n in range(self.statistic.putin_limit):
            putin = Putin_small(self.screen, self.ayf_settings)
            putin.rect.x = 10 + putin.rect.width * n
            putin.rect.y = 10
            self.putins.add(putin)
    
    def update_trump_life(self):
        '''Обновляет количество жизней трампа'''
        self.trump = Trump_small(self.screen, self.ayf_settings)
        self.trump.rect.right = self.screen_rect.right
        self.trump.rect.y = 10
        self.surface_trump = pygame.Rect(0, 0, (240 - self.statistic.w), 25)
        self.surface_trump.right = self.trump.rect.left
        self.surface_trump.centery = self.trump.rect.centery
    
    def update_trump_line(self):
        '''Обновляет полосу здоровья трампа'''
        self.surface_trump = pygame.Rect(0, 0, (240 - self.statistic.w), 25)
        self.surface_trump.right = self.trump.rect.left
        self.surface_trump.centery = self.trump.rect.centery
    
    def show_score(self):
        self.screen.fill((210,45,50) ,self.surface)
        self.putins.draw(self.screen)
        self.screen.blit(self.trump.image, self.trump.rect)
        self.screen.fill((0,250,0) ,self.surface_trump)
        
