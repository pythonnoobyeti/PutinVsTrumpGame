import sys, os, pygame
from random import randint
from time import sleep

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


from src.models.rubls import Rub
from src.models.trump import Trump
from src.models.dollar import Dollar



def check_key_down(event, putin, rubs, ayf_settings, statistic):
    '''Проверяет нажатие клавиш клавиатуры'''
    if event.key == pygame.K_UP:
        putin.up = True
    elif event.key == pygame.K_DOWN:
        putin.down = True
    elif event.key == pygame.K_SPACE:
        if len(rubs) < 1:
            rub = Rub(putin, ayf_settings)
            rubs.add(rub)
            if statistic.trump_limit <=3 and statistic.q <=100:
                statistic.f -= 1
            #Параметр активации анимации Путина
            putin.count_fire += 1
            

def check_key_up(event, putin):
    '''Проверяет отпускание клавиш клавиатуры'''
    if event.key == pygame.K_UP:
        putin.up = False
    elif event.key == pygame.K_DOWN:
        putin.down = False

def check_event(putin, rubs, button_play, ayf_settings, statistic, dollars, sb):
    '''Проверяет события с кнопками мыши и клавиатуры'''
    #Цикл для получения и обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, putin, rubs, ayf_settings, statistic)
        elif event.type == pygame.KEYUP:
            check_key_up(event, putin)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Получение картежа с координатами щелчка мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_button_collide(mouse_x, mouse_y, button_play, ayf_settings, 
                   statistic, rubs, dollars, sb)

def check_button_collide(mouse_x, mouse_y, button_play, ayf_settings, 
    statistic, rubs, dollars, sb):
        '''Проверка коллизий между кнопкой и щелчком'''
        collide = button_play.rect.collidepoint(mouse_x, mouse_y)
        if collide and not ayf_settings.game_active:
            pygame.mixer.music.play(-1)
            #Сбрасываем статистические параметры
            statistic.reset_game()
            dollars.empty()
            rubs.empty()
            sb.update_putin_life()
            #Сбрасываем динамические параметры
            ayf_settings.dynamic_settings()
            sb.update_trump_line()
            #Флаг игра активна
            ayf_settings.game_active = True
            #Не отображать мышь
            pygame.mouse.set_visible(False)
        
def rubs_update(rubs, putin):
    '''Обновляет координаты рублей и удалят рубли'''
    rubs.update()
    for rub in rubs.copy():
        if rub.rect.left >= putin.screen_rect.right:
            rubs.remove(rub)

def dollars_update(dollars, trump):
    '''Обновляет координаты долларов и удалят доллары'''
    dollars.update()
    for dol in dollars.copy():
        if dol.rect.right < 0:
            dollars.remove(dol)

def check_trump_rubs_collide(trump, rubs, ayf_settings, statistic, sb):
    '''Проверяет коллизии между Трампом и рублями'''
    if pygame.sprite.spritecollideany(trump, rubs):
        statistic.trump_limit -= 1
        statistic.w += 40
        statistic.f = ayf_settings.f
        statistic.q = ayf_settings.q 
        sb.update_trump_line()
        #Параметр активации анимации трампа при попадании
        trump.count_hit += 1
        rubs.empty()
        ayf_settings.dynamic_up()
        
    elif statistic.trump_limit <= 0:
        ayf_settings.game_active = False
        trump.rect.right = trump.screen_rect.right

def update_screen(screen, ayf_settings, putin, trump, rubs, button_play,
    statistic, dollars, sb, sd):
        '''Функция обновления экрана'''
        screen.fill(ayf_settings.bg_color)
        if not ayf_settings.game_active:
            #Емли игра не активна, отображает кнопку, отображает курсор
            #При достижении trump_limit 0 игра заканчивается
            putin_victory(screen, statistic, dollars, rubs, sd)
            trump_victory(screen, statistic, dollars, rubs, sd)
            button_play.blit()
            pygame.mouse.set_visible(True)
        
        #Если показатель находится в указанных рамках, то выводит изображение
        #при стрельбе
        if putin.count_fire > 0 and putin.count_fire <= 300:
            putin.image = putin.putin_images[1]
            putin.count_fire += 1
        #Если показатель выходит за рамки, то изображение Путина становится 
        #обычным и показатель обнуляется
        elif putin.count_fire > 300:
            putin.image = putin.putin_images[0]
            putin.count_fire = 0
        #Аналогично для Трампа
        if trump.count_hit > 0 and trump.count_hit <= 500:
            trump.image = trump.trump_images[1]
            trump.count_hit += 1
        elif trump.count_hit > 500:
            trump.image = trump.trump_images[0]
            trump.count_hit = 0
        
        #Если показатель находится в указанных рамках, то выводит изображение
        #при попадании в Путина
        if putin.count_hit > 0 and putin.count_hit <= 300:
            putin.image = putin.putin_images[2]
            putin.count_hit += 1
        #Если показатель выходит за рамки, то изображение Путина становится 
        #обычным и показатель обнуляется
        elif putin.count_hit > 300:
            putin.image = putin.putin_images[0]
            putin.count_hit = 0
        
        rubs.draw(screen)
        dollars.draw(screen)
        putin.blit_putin()
        trump.blit_trump()
        sb.show_score()
        pygame.display.flip()

def putin_victory(screen, statistic, dollars, rubs, sd):
    '''Вывод изображений при победе'''
    if statistic.trump_limit <= 0:
        dollars.empty()
        rubs.empty()
        #Загрузка победных изображений
        image_1 = pygame.image.load(resource_path('src/images/russia.bmp'))
        image_2 = pygame.image.load(resource_path('src/images/exp.bmp'))
        image_3 = pygame.image.load(resource_path('src/images/putin_fin.bmp'))
        #Отрисовка прямоугольников изображений и экрана
        rect_1 = image_1.get_rect()
        rect_2 = image_2.get_rect()
        rect_3 = image_3.get_rect()
        screen_rect = screen.get_rect()
        #Позиционирование изображений
        rect_1.center = screen_rect.center
        rect_2.center = screen_rect.center
        rect_3.bottom = screen_rect.bottom
        rect_3.left = screen_rect.left 
        #Вывод на экран изображений
        screen.blit(image_1, rect_1)
        screen.blit(image_2, rect_2)
        screen.blit(image_3, rect_3)
        pygame.mixer.music.pause()
        sd.putin_victory.play()
        
        

def trump_victory(screen, statistic, dollars, rubs, sd):
    '''Вывод изображений при победе'''
    if statistic.putin_limit <= 0:
        dollars.empty()
        rubs.empty()
        #Загрузка победных изображений
        image_1 = pygame.image.load(resource_path('src/images/america.bmp'))
        image_2 = pygame.image.load(resource_path('src/images/statue.bmp'))
        image_3 = pygame.image.load(resource_path('src/images/trump_fin.bmp'))
        #Отрисовка прямоугольников изображений и экрана
        rect_1 = image_1.get_rect()
        rect_2 = image_2.get_rect()
        rect_3 = image_3.get_rect()
        screen_rect = screen.get_rect()
        #Позиционирование изображений
        rect_1.center = screen_rect.center
        rect_2.center = screen_rect.center
        rect_3.bottom = screen_rect.bottom
        rect_3.right = screen_rect.right 
        #Вывод на экран изображений
        screen.blit(image_1, rect_1)
        screen.blit(image_2, rect_2)
        screen.blit(image_3, rect_3)
        

def update_trump(statistic, trump, ayf_settings, screen, dollars, sb, field,
     rubs):
    '''Управляет поведением трампа'''
    #Первый режим игры: Трамп ходит вверх вниз отталкиваясь от граней
    if statistic.trump_limit > 3:
        if trump.rect.bottom >= trump.screen_rect.bottom:
            ayf_settings.direction = -1
        elif trump.rect.top <= sb.surface.bottom:
            ayf_settings.direction = 1 
        trump.y += (ayf_settings.trump_speed_factor * 
            ayf_settings.direction)
        trump.rect.y = trump.y
        #После первого попадания начинает стрелять
        if len(dollars) < statistic.dollars_limit and (statistic.trump_limit < 
        ayf_settings.trump_limit):
            dol = Dollar(trump, screen, ayf_settings)
            dollars.add(dol)
        
    #Второй режим игры: Транм рандомно меняет координаты в разрешённой
    #области
    elif statistic.trump_limit <= 3:
        if statistic.trump_limit <= 1:
            if trump.i >= 300:
                trump.rect.x = randint((ayf_settings.sc_width/2), 
                      ayf_settings.sc_width - trump.rect.width)
                trump.rect.y = randint(sb.surface.bottom + trump.rect.height,
                      ayf_settings.sc_height - trump.rect.height)
                #Задержка для обновления координат
                trump.i = 0
                #Начинает стрелять
                if statistic.trump_limit <= 2 and (
                   len(dollars) < statistic.dollars_limit):
                       dol = Dollar(trump, screen, ayf_settings)
                       dollars.add(dol)
                       if statistic.trump_limit <= 1:
                           statistic.dollars_limit = 10
        elif statistic.trump_limit <= 3:
            if trump.i >= 450:
                trump.rect.x = randint((ayf_settings.sc_width/2), 
                      ayf_settings.sc_width - trump.rect.width)
                trump.rect.y = randint(sb.surface.bottom + trump.rect.height,
                      ayf_settings.sc_height - trump.rect.height)
                #Задержка для обновления координат
                trump.i = 0
                #Начинает стрелять
                if statistic.trump_limit <= 2 and (
                      len(dollars) < statistic.dollars_limit):
                          dol = Dollar(trump, screen, ayf_settings)
                          dollars.add(dol)
                          if statistic.trump_limit <= 1:
                              statistic.dollars_limit = 10
        #Задержка для обновления координат    
        trump.i += 1
    #Задержка для вывода анимации при попадании
    if trump.count_hit >= 1:
        trump.count_hit += 1
    #Обновление координат области
    field.update_field()

def check_putin_dollars_collide(putin, dollars, statistic, ayf_settings, trump,
     screen, sb):
    '''Проверяет коллизию между путиным и долларами'''
    collision = pygame.sprite.spritecollideany(putin, dollars)
    if collision:
        statistic.putin_limit -= 1
        putin.count_hit += 1
        sb.update_putin_life()
        dollars.remove(collision)
        if statistic.putin_limit <= 0:
            ayf_settings.game_active = False
            trump.rect.right = trump.screen_rect.right

def check_collide_rubs_field(rubs, trump, field, sb, ayf_settings, statistic):
    '''Смещает координату трампа по y, если есть пересечение field с rubs'''
    collide = pygame.sprite.spritecollideany(field, rubs)
    if collide and statistic.trump_limit <= 3 and statistic.q > 100:
        if trump.rect.top <= trump.screen_rect.centery:
            trump.rect.y += 250
        elif trump.rect.top > trump.screen_rect.centery:
            trump.rect.y -= 250
        statistic.q -= 20
    elif statistic.f <= 0:
        statistic.q = ayf_settings.q  
        statistic.f = 2        