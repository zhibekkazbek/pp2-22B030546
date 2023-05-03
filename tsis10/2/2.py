#Импортирование нужных библиотек
import pygame
import random, psycopg2, time
from config import config

db_level = 0
params = config()
connection = psycopg2.connect(**params)
cursor = connection.cursor()


def db():
    global name, db_level
    mode = int(input("Select:\n1 - if you have account\n2 - you want to creat new account\nEnter:"))


    if mode == 1:
        name = input("Enter your name:")
        cursor.execute(f"SELECT * FROM record WHERE name = '{name}'")
        result = cursor.fetchall()

        for x in result:
            db_level = x[1]

        if len(result) == 0:
            print("No results")
            time.sleep(0.5)
            return db()

        else: print(db_level)


    elif mode == 2:
        name = input("Enter the name you want:")
        cursor.execute(f"SELECT * FROM record WHERE name = '{name}'")
        res = cursor.fetchall()

        if len(res) == 0:
            cursor.execute(f"INSERT INTO record (name, maxlevel) VALUES ('{name}', {db_level})")
            print("done")
            connection.commit()

        else:
            print("Sorry,this nickname already exists\nchoose another name")
            time.sleep(0.5)
            return db()

db()

#Инициализация пайгейм
pygame.init()

#Даем значения высоты и ширины окна и обозначаем максимальный и текущий уровень
height = 400
width = 400
MAX_LEVEL = 7
level = db_level


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

fps = pygame.time.Clock()

#Даем значение одного блока и скорости змеи
snake_block = 20
snake_speed = 5

font = pygame.font.Font(None,30)

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Wall:
    #Эта функция инициялизирует уровень и открывет нам нужный файл, а так же все координаты стен закидывает в лист
    def __init__(self, level):
        self.level = level
        self.body = []
        path = r"C:\Users\Сырым\Documents\pp2-22B030546\tsis10\2\levels\\"
        f = open(f"{path}level{self.level}.txt", "r")

        for y in range(0, height // snake_block + 1):
            for x in range(0, width // snake_block + 1):

                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    #Рисует стены по координатам
    def draw(self):
        for point in self.body:
            rect = pygame.Rect(snake_block * point.x, snake_block * point.y, snake_block, snake_block)
            pygame.draw.rect(screen, (254,1,154), rect)

#Эта функция отвечает за отоброжения текущего уровня и счета
def Score(score,level):
    value = font.render(f"SCORE: {score}",True,(255,255,255))
    screen.blit(value, (0,0))
    uroven = font.render(f'LEVEL: {level}', True,(255,255,255))
    screen.blit(uroven, (0,40))

def Snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0,255,0),(x[0], x[1], snake_block-1, snake_block-1))

#Эта функция выводит на экран текст который получает по указанным координатам 
def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [10, height // 3])

counter, text = 1000, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 100)
font1 = pygame.font.SysFont('Consolas', 30)
tt = random.randint(2,3)
cnt = 0
#Основная функция игры

for x in range(0,7): 
    if x == level: 
        snake_speed = snake_speed + x  
    else: continue

def main():
    #Устанавливаем глобальные перемнные для дальнешего изменения или использования
    # переменная статус будет отвечать за цикл игры, клоус за рестарт, уолл генерацию стен
    global level, snake_speed, text, counter, font1, tt, cnt, db_level, name,r
    status = True
    close = False
    wall = Wall(level)
    
    x1 = width // 2
    y1 = height // 2
    
    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

    #Даем координаты еды и проверяем ее на что не оказалось ли она в стене
    foodx = round(random.randrange(0, width - snake_block)/ 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block)/ 20.0) * 20.0
    for point in wall.body:
        if foodx == snake_block * point.x and foody == snake_block * point.y:
            foodx = round(random.randrange(0, width - snake_block)/ 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block)/ 20.0) * 20.0
        else:
            continue
    
    food1x = round(random.randrange(0, width - snake_block)/ 20.0) * 20.0
    food1y = round(random.randrange(0, height - snake_block)/ 20.0) * 20.0
    for point in wall.body:
        if food1x == snake_block * point.x and food1y == snake_block * point.y:
            food1x = round(random.randrange(0, width - snake_block)/ 20.0) * 20.0
            food1y = round(random.randrange(0, height - snake_block)/ 20.0) * 20.0
        else:
            continue

    while status:
        while close == True:
            screen.fill((0,0,0))
            message("Press Space-to continue or Q-Quit", (255,255,255))
            Score(snake_length - 1, level)
            pygame.display.update()

            if level > db_level:
                cursor.execute(f"UPDATE record SET maxlevel = {level} WHERE name = '{name}'")
                connection.commit()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        status = False
                        close = False
                    if event.key == pygame.K_SPACE:
                        main()
        screen.fill((0,0,0))
        #Цикл будет проверять на какую клавишу мы нажали и через условия она дает координаты как двигаться
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                status = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
            
                elif event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0

                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -snake_block
            
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = snake_block
                
                elif event.key == pygame.K_SPACE:
                    close = True
                    

            if event.type == pygame.USEREVENT: 
                counter -= 10
                cnt += 10
                text = str(counter).rjust(3) if counter > 0 else f'{cnt-10}'
                if cnt == 1500:
                    counter = 1000
                    cnt = 0
                if counter > 0:
                    pygame.draw.rect(screen, (0,0,255), (food1x, food1y, snake_block, snake_block))
                else: continue

        """ if pause:
            message("To save your results press:s", (255,255,255))
            screen.blit(image,imrect)
            r = snake_speed
            snake_speed = 0.00000000001"""

        #условие проверяет не перешли ли мы границу
        if  x1 > width or x1 < 0 or y1 > height or y1 < 0:
            close = True

        #Ранее мы дали координаты как будет двигаться змея и сечас мы даем
        # координаты для головы что бы она двигалась
        x1 += dx
        y1 += dy
      
        pygame.draw.rect(screen, (255,0,0), (foodx, foody, snake_block, snake_block))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        #Дали листу который будет отвечать за рисование тела змеи
        snake_list.append(snake_head)

        #Эта функция проверяет, если длина snake_list(текущая длина змеи) больше snake_length (желаемая длина змеи)
        #то функция del удаляет первый элемент из списка snake_list. Это что бы всегдаа сохр желаемою длинну змеи
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        #Проверяет коснулась ли она саму себя
        for x in snake_list[:-1]:
            if x == snake_head:
                close = True

        #через это условие меняем уровень и даем новую скорость
        if  (snake_length - 1) >= 6:
            level = (level + 1) % MAX_LEVEL
            wall.__init__(level)
            wall.draw()
            snake_length = 1
            snake_list = []
            x1 = width // 2
            y1 = height // 2
            Snake(snake_block,snake_list)
            snake_speed += 1
        

        #вызываем все функции и обнавляем
        Snake(snake_block, snake_list)
        Grid()
        wall.draw()
        Score(snake_length - 1, level)
        #screen.blit(font1.render(text, True, (255,255, 255)), (32, 48))
        
        pygame.display.update()

        #Проверяем сьела ли наша змея еди и если да то даем ей новую координату
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

            for point in wall.body:
                if foodx == snake_block * point.x and foody == snake_block * point.y:
                    foodx = round(random.randrange(0, width - snake_block)/ 20.0) * 20.0
                    foody = round(random.randrange(0, height - snake_block)/ 20.0) * 20.0
                else:
                    continue
            #Каждая сьетая еда +1 к счету
            snake_length += 1

        if x1 == food1x and y1 == food1y:
            food1x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            food1y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

            for point in wall.body:
                if food1x == snake_block * point.x and food1y == snake_block * point.y:
                    food1x = round(random.randrange(0, width - snake_block)/ 20.0) * 20.0
                    food1y = round(random.randrange(0, height - snake_block)/ 20.0) * 20.0
                else:
                    continue
                tt = random.randint(2,3) 
            #Каждая сьетая еда 2 или 3 к счету
            snake_length += tt

        #Проверяем коснулась ли наша змея стен
        for point in wall.body:
            if x1 == snake_block * point.x and y1 == snake_block * point.y:
                close = True 

        if level == 0:
            snake_speed = 5

        #Скорость обнавления и скорость змеи
        fps.tick(snake_speed)
    
    #для завершения работы Pygame,
    pygame.quit()
    quit()

#рисуем сетку для удобства
def Grid():
    for x in range(0, width, snake_block):
        for y in range(0, height, snake_block):
            rect = pygame.Rect(x, y, snake_block, snake_block)
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)

#Вызываем функцию игры
main()
connection.close()
cursor.close()