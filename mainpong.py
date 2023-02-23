import pygame
from random import randrange
# Инициализация Pygame и создание групп спрайтов
pygame.init()
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    # Класс шара
    def __init__(self, radius, x, y, counter_l, counter_r, fpscount):
        super().__init__(all_sprites)
        # Создание нужных переменных
        self.fps = fpscount
        self.counter_left = counter_l
        self.counter_right = counter_r
        self.radius = radius
        self.radius = radius
        # Создание самого шара и его коллизии
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color('red'),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        # Скорость шара в зависимости от FPS
        if self.fps == 144:
            self.x = -2
        else:
            self.x = -5
        self.y = randrange(-3, -1)
        if self.fps == 60:
            self.y *= 2

    def update(self):
        # Движение шара и проверка столкновений
        self.rect = self.rect.move(self.x, self.y)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.y = -self.y
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.x = -self.x
        if self.rect.collidelistall([firstplatformcords, secondplatformcords]):
            self.x = -self.x
        if self.rect.collidelistall([[0, 0, 1, width]]):
            self.rect.move_ip((width // 2), (height // 2))
            self.counter_left += 1

        elif self.rect.collidelistall([[width, 0, height - 1, width]]):
            self.rect.move_ip(- (width // 2), 0)
            self.counter_right += 1

    def count_left(self):
        # Счетчик слева
        return self.counter_left

    def count_right(self):
        # Счетчик справа
        return self.counter_right


class Border(pygame.sprite.Sprite):
    # Класс заграждений
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


# Задание экрана
size = width, height = 1000, 800
screen = pygame.display.set_mode(size)
# Переменная счетчика
counter_left = counter_right = 0
# Цвет платформ
firstplatformcolor = pygame.Color('black')
secondplatformcolor = pygame.Color('black')
ballcolor = pygame.Color('red')
# Задание шрифтов
font_menu = pygame.font.Font(None, 70)
text_play = font_menu.render('PLAY', True, (100, 255, 100))
pongfont = pygame.font.Font(None, 100)
text_menu = pongfont.render('PONG', True, (255, 0, 0))
text_60 = font_menu.render('60 FPS', True, (0, 255, 0))
text_144 = font_menu.render('144 FPS', True, (0, 255, 0))
# Координаты текста
text_x = width // 2 - text_menu.get_width() // 2
text_y = height // 3
text_w = text_menu.get_width()
text_h = text_menu.get_height()
text_x_play = width // 2 - text_play.get_width() // 2
text_y_play = 430
text_w_play = text_play.get_width()
text_h_play = text_play.get_height()
# pygame.Rect для удобной проверки коллизии
first_blue = pygame.Rect((100, 400, 50, 50))
first_red = pygame.Rect((100, 460, 50, 50))
first_green = pygame.Rect(160, 400, 50, 50)
first_yellow = pygame.Rect(160, 460, 50, 50)
second_blue = pygame.Rect(860, 400, 50, 50)
second_red = pygame.Rect(860, 460, 50, 50)
second_green = pygame.Rect(800, 400, 50, 50)
second_yellow = pygame.Rect(800, 460, 50, 50)
# Еще текст
fps_60 = pygame.Rect(text_x + 22, text_y + 250, 50, 50)
fps_144 = pygame.Rect(text_x + 12, text_y + 330, 50, 50)

fps = 60  # количество кадров в секунду
clock = pygame.time.Clock()
running = True


def main_menu():
    # Функция с игровым циклом меню
    global running, firstplatformcolor, secondplatformcolor, fps
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[0]:
                # Проверка нажатия на кнопки
                if text_w_play + text_x_play > pygame.mouse.get_pos()[0] > text_x_play and text_h_play + \
                        text_y_play > pygame.mouse.get_pos()[1] > text_y_play:
                    running = False
                if first_blue.collidepoint(pygame.mouse.get_pos()):
                    firstplatformcolor = pygame.Color('blue')
                elif first_red.collidepoint(pygame.mouse.get_pos()):
                    firstplatformcolor = pygame.Color('red')
                elif first_green.collidepoint(pygame.mouse.get_pos()):
                    firstplatformcolor = pygame.Color('green')
                elif first_yellow.collidepoint(pygame.mouse.get_pos()):
                    firstplatformcolor = pygame.Color('yellow')

                elif second_yellow.collidepoint(pygame.mouse.get_pos()):
                    secondplatformcolor = pygame.Color('yellow')
                elif second_green.collidepoint(pygame.mouse.get_pos()):
                    secondplatformcolor = pygame.Color('green')
                elif second_red.collidepoint(pygame.mouse.get_pos()):
                    secondplatformcolor = pygame.Color('red')
                elif second_blue.collidepoint(pygame.mouse.get_pos()):
                    secondplatformcolor = pygame.Color('blue')
                elif fps_60.collidepoint(pygame.mouse.get_pos()):
                    fps = 60
                elif fps_144.collidepoint(pygame.mouse.get_pos()):
                    fps = 144

            screen.fill(pygame.Color('black'))
            # Текст
            screen.blit(text_menu, (text_x, text_y))
            pygame.draw.rect(screen, (255, 0, 0), (text_x - 10,
                                                   text_y - 10,
                                                   text_w + 20, text_h + 20), 1)
            # Кнопки выбора цвета
            pygame.draw.rect(screen, pygame.Color('blue'), (100, 400, 50, 50))
            pygame.draw.rect(screen, pygame.Color('red'), (100, 460, 50, 50))
            pygame.draw.rect(screen, pygame.Color('green'), (160, 400, 50, 50))
            pygame.draw.rect(screen, pygame.Color('yellow'), (160, 460, 50, 50))

            pygame.draw.rect(screen, pygame.Color('green'), (800, 400, 50, 50))
            pygame.draw.rect(screen, pygame.Color('yellow'), (800, 460, 50, 50))
            pygame.draw.rect(screen, pygame.Color('blue'), (860, 400, 50, 50))
            pygame.draw.rect(screen, pygame.Color('red'), (860, 460, 50, 50))
            # Еще текст
            screen.blit(text_60, (text_x + 22, text_y + 250))
            screen.blit(text_144, (text_x + 12, text_y + 330))
            screen.blit(text_play, (text_x_play, text_y_play))
            pygame.draw.rect(screen, (0, 255, 0), (text_x_play - 10,
                                                   text_y_play - 10,
                                                   text_w_play + 20, text_h_play + 20), 1)
            # FPS и смена кадра
            pygame.display.flip()
            clock.tick(fps)


# Вызов функции
main_menu()

# Вссе для нажатий
up1_pressed = down1_pressed = up2_pressed = down2_pressed = False

up1 = pygame.K_w
down1 = pygame.K_s
up2 = pygame.K_i
down2 = pygame.K_k
# Координаты
firstplatformcords = [0, 0, 7, 80]
secondplatformcords = [width - 7, height - 80, 7, 80]
ballcords = [width // 2, height // 2]
# Создание барьера и шара
Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)

ball = Ball(10, ballcords[0], ballcords[1], counter_left, counter_right, fps)

running = True


def main_game():
    # Функция с главным игровым циклом
    global running, up1_pressed, up2_pressed, down1_pressed, down2_pressed
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Проверка нажатий
            if event.type == pygame.KEYDOWN:
                if event.key == up1:
                    up1_pressed = True
                if event.key == down1:
                    down1_pressed = True

                if event.key == up2:
                    up2_pressed = True
                if event.key == down2:
                    down2_pressed = True

            if event.type == pygame.KEYUP:
                if event.key == up1:
                    up1_pressed = False
                if event.key == down1:
                    down1_pressed = False

                if event.key == up2:
                    up2_pressed = False
                if event.key == down2:
                    down2_pressed = False
        # Перемещение платформ
        if up1_pressed and firstplatformcords[1] > 0:
            if fps == 144:
                firstplatformcords[1] -= 5
            else:
                firstplatformcords[1] -= 12
        elif down1_pressed and firstplatformcords[1] < width - 280:
            if fps == 144:
                firstplatformcords[1] += 5
            else:
                firstplatformcords[1] += 12

        if up2_pressed and secondplatformcords[1] > 0:
            if fps == 144:
                secondplatformcords[1] -= 5
            else:
                secondplatformcords[1] -= 12
        elif down2_pressed and secondplatformcords[1] < width - 280:
            if fps == 144:
                secondplatformcords[1] += 5
            else:
                secondplatformcords[1] += 12
        # Значения для счетчиков
        counter_left = ball.count_left()
        counter_right = ball.count_right()
        screen.fill(pygame.Color('white'))
        # Текст для счетчиков
        font = pygame.font.Font(None, 70)
        text_left = font.render(str(counter_left), True, (100, 255, 100))
        screen.blit(text_left, (height // 3, width // 30))

        text_right = font.render(str(counter_right), True, (100, 255, 100))
        screen.blit(text_right, (height - height // 3 + 140, width // 30))
        # Отрисовка
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.draw.rect(screen, firstplatformcolor, firstplatformcords)
        pygame.draw.rect(screen, secondplatformcolor, secondplatformcords)
        # FPS и смена кадра
        pygame.display.flip()
        clock.tick(fps)


# Вызов фунции
main_game()