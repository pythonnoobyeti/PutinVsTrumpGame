import pygame
from pygame.sprite import Sprite

class Putin_small(Sprite):
    '''Класс создания иконок путина'''
    def __init__(self, screen, ayf_settings):
        '''Инициализация атрибутов'''
        super().__init__()
        self.screen = screen
        self.ayf_settings = ayf_settings
        self.image = pygame.image.load('images/Putin_small.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
