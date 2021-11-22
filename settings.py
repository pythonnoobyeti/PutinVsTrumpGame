class Settings():
    '''Настройки игры'''
    def __init__(self):
        '''Инициализация параметров'''
        
        #Статические параметры экрана
        self.sc_width = 1200
        self.sc_height = 700
        self.bg_color = (100,12,74)
        
        #Основной флаг игры
        self.game_active = False
        
        #Количество жизней Трампа, Путина
        self.trump_limit = 6
        self.putin_limit = 3
        
        #Темп игры
        self.temp = 1.3
        
        
        
        #Инициализация динамических параметров
        self.dynamic_settings()
        
    def dynamic_settings(self):
        '''Инициализация динамических параметров'''
        self.putin_speed_factor = 0.6
        self.trump_speed_factor = 0.6
        self.rub_speed = 1
        self.dollar_speed = 2
        self.direction = 1
        #Количество разрешённых долларов
        self.dollars_limit = 1
        #Счётчик для рандомного перемещения
        self.q = 200
        self.w = 0
        self.f = 2
    
    def dynamic_up(self):
        '''ункция увеличения темпа игры'''
        self.putin_speed_factor *= self.temp
        self.trump_speed_factor *= self.temp
        self.rub_speed *= self.temp
        self.direction = 1
        
        
