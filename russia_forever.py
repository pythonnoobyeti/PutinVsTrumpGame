import sys
import pygame
from pygame.sprite import Group


from settings import Settings
from src.models.putin import Putin
from src.models.trump import Trump
from stats import Statistic
from src.models.button import Button
from src.models.scoreboard import ScoreBoard
from src.utils import game_function as gf
from src.models.field import Field
from src.models.sound import Sound



def run_game():
    '''Запускает игру'''
    pygame.init()
    sd = Sound()
    pygame.mixer.music.play(-1)
    ayf_settings = Settings()
    #Создание экрана и надписи в шапке 
    screen = pygame.display.set_mode((ayf_settings.sc_width, 
             ayf_settings.sc_height))
    pygame.display.set_caption('RUSSIA FOREVER')
     #Создание статистического класса  кнопки запуска
    statistic = Statistic(ayf_settings)
    button_play = Button(screen, 'Play')
    sb = ScoreBoard(statistic, screen, ayf_settings)
    #Создание оснвных игровых классов и групп
    putin = Putin(screen, ayf_settings, sb)
    trump = Trump(screen, ayf_settings, statistic)
    rubs = Group()
    dollars = Group()
    field = Field(trump, screen)

    while True:
        gf.check_event(putin, rubs, button_play, ayf_settings, statistic,
           dollars, sb)
        if ayf_settings.game_active:
            putin.update_putin()
            gf.update_trump(statistic, trump, ayf_settings, screen, dollars, 
            sb, field, rubs)
            gf.rubs_update(rubs, putin)
            gf.dollars_update(dollars, trump)
            gf.check_collide_rubs_field(rubs, trump, field, sb, ayf_settings,
               statistic)
            gf.check_trump_rubs_collide(trump, rubs, ayf_settings, statistic,
               sb)
            gf.check_putin_dollars_collide(putin, dollars, statistic, 
            ayf_settings, trump, screen, sb)
        gf.update_screen(screen, ayf_settings, putin, trump, rubs, button_play,
           statistic, dollars, sb, sd)

run_game()
