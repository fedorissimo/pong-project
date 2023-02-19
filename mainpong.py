import pygame
from random import randint, randrange

pygame.init()
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, counter_l, counter_r):
        super().__init__(all_sprites)
        self.counter_left = counter_l
        self.counter_right = counter_r
        self.radius = radius
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color('red'),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.x = -2
        self.y = randrange(-3, -1)

    def update(self):
        self.rect = self.rect.move(self.x, self.y)
        # print(self.rect)
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
            self.rect.move_ip(- (width // 2), - (height // 2))
            self.counter_right += 1

    def count_left(self):
        return self.counter_left

    def count_right(self):
        return self.counter_right


class Border(pygame.sprite.Sprite):
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


size = width, height = 1000, 800

counter_left = counter_right = 0

if type(size[0]) == type(size[1]) == int:
    screen = pygame.display.set_mode(size)
else:
    print('Неправильный формат ввода')
firstplatformcolor = pygame.Color('black')
secondplatformcolor = pygame.Color('black')
ballcolor = pygame.Color('red')
font = pygame.font.Font(None, 70)
text_play = font.render('PLAY', True, (100, 255, 100))

first_blue = pygame.Rect((100, 400, 50, 50))
first_red = pygame.Rect((100, 460, 50, 50))
first_green = pygame.Rect(160, 400, 50, 50)
first_yellow = pygame.Rect(160, 460, 50, 50)
second_blue = pygame.Rect(860, 400, 50, 50)
second_red = pygame.Rect(860, 460, 50, 50)
second_green = pygame.Rect(800, 400, 50, 50)
second_yellow = pygame.Rect(800, 460, 50, 50)

text_x_play = width // 2 - text_play.get_width() // 2
text_y_play = 430
text_w_play = text_play.get_width()
text_h_play = text_play.get_height()
fps = 144  # количество кадров в секунду
clock = pygame.time.Clock()
running = True

while running:  # главный игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
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

        screen.fill(pygame.Color('black'))
        text_menu = font.render('PONG', True, (100, 255, 100))

        text_x = width // 2 - text_menu.get_width() // 2
        text_y = height // 3
        text_w = text_menu.get_width()
        text_h = text_menu.get_height()
        screen.blit(text_menu, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10,
                                               text_y - 10,
                                               text_w + 20, text_h + 20), 1)

        pygame.draw.rect(screen, pygame.Color('blue'), (100, 400, 50, 50))
        pygame.draw.rect(screen, pygame.Color('red'), (100, 460, 50, 50))
        pygame.draw.rect(screen, pygame.Color('green'), (160, 400, 50, 50))
        pygame.draw.rect(screen, pygame.Color('yellow'), (160, 460, 50, 50))

        pygame.draw.rect(screen, pygame.Color('green'), (800, 400, 50, 50))
        pygame.draw.rect(screen, pygame.Color('yellow'), (800, 460, 50, 50))
        pygame.draw.rect(screen, pygame.Color('blue'), (860, 400, 50, 50))
        pygame.draw.rect(screen, pygame.Color('red'), (860, 460, 50, 50))

        screen.blit(text_play, (text_x_play, text_y_play))
        pygame.draw.rect(screen, (0, 255, 0), (text_x_play - 10,
                                               text_y_play - 10,
                                               text_w_play + 20, text_h_play + 20), 1)
        pygame.display.flip()  # смена кадра
        # изменение игрового мира
        # ...
        # временная задержка
        clock.tick(fps)

up1_pressed = down1_pressed = up2_pressed = down2_pressed = False

up1 = pygame.K_w

down1 = pygame.K_s

up2 = pygame.K_i
down2 = pygame.K_k

firstplatformcords = [0, 0, 7, 80]
secondplatformcords = [width - 7, height - 80, 7, 80]
ballcords = [width // 2, height // 2]

Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)

ball = Ball(10, ballcords[0], ballcords[1], counter_left, counter_right)

fps = 144  # количество кадров в секунду
clock = pygame.time.Clock()
running = True
while running:  # главный игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    if up1_pressed and firstplatformcords[1] > 0:
        firstplatformcords[1] -= 5
    elif down1_pressed and firstplatformcords[1] < width - 280:
        firstplatformcords[1] += 5

    if up2_pressed and secondplatformcords[1] > 0:
        secondplatformcords[1] -= 5
    elif down2_pressed and secondplatformcords[1] < width - 280:
        secondplatformcords[1] += 5
        # обработка остальных событий
        # ...
    counter_left = ball.count_left()
    counter_right = ball.count_right()
    # print(counter_left)
    # формирование кадра
    # ...
    screen.fill(pygame.Color('white'))

    font = pygame.font.Font(None, 70)
    text_left = font.render(str(counter_left), True, (100, 255, 100))
    screen.blit(text_left, (height // 3, width // 30))

    text_right = font.render(str(counter_right), True, (100, 255, 100))
    screen.blit(text_right, (height - height // 3 + 140, width // 30))

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.draw.rect(screen, firstplatformcolor, firstplatformcords)
    pygame.draw.rect(screen, secondplatformcolor, secondplatformcords)
    # pygame.draw.circle(screen, ballcolor, ballcords, 10)
    # Ball(10, ballcords[0], ballcords[1])
    pygame.display.flip()  # смена кадра
    # изменение игрового мира
    # ...
    # временная задержка
    clock.tick(fps)
