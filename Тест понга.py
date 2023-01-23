import pygame
import PyQt5
from random import randint, randrange
from pong2 import Ui_MainWindow
pygame.init()
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color('red'),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.x = randint(-5, 5)
        self.y = randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.x, self.y)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.y = -self.y
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.x = -self.x


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

if type(size[0]) == type(size[1]) == int:
    screen = pygame.display.set_mode(size)
else:
    print('Неправильный формат ввода')
firstplatformcolor = pygame.Color('black')
secondplatformcolor = pygame.Color('black')
ballcolor = pygame.Color('red')

pressed_up1 = pressed_down1 = False
up1 = pygame.K_i
down1 = pygame.K_k

up2 = pygame.K_w
down2 = pygame.K_s

firstplatformcords = [0, 0, 7, 80]
secondplatformcords = [width - 7, height - 80, 7, 80]
ballcords = [width // 2, height // 2]


Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
Ball(10, 100, 100)


fps = 60 # количество кадров в секунду
clock = pygame.time.Clock()
running = True
while running: # главный игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == up1:
                pressed_up1 = True
                firstplatformcords[1] -= 30
            if event.key == down1:
                firstplatformcords[1] += 30
                pressed_down1 = True

            if event.key == up2:
                pressed_up1 = True
                secondplatformcords[1] -= 30
            if event.key == down2:
                secondplatformcords[1] += 30
                pressed_down1 = True

        if event.type == pygame.KEYUP:
            if event.key == up1:
                pressed_up1 = False
            if event.key == down1:
                pressed_down1 = False
        # обработка остальных событий
        # ...
    # формирование кадра
    # ...

    screen.fill(pygame.Color('white'))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.draw.rect(screen, firstplatformcolor, firstplatformcords)
    pygame.draw.rect(screen, secondplatformcolor, secondplatformcords)
    pygame.draw.circle(screen, ballcolor, ballcords, 10)
    Ball(10, ballcords[0], ballcords[1])
    pygame.display.flip() # смена кадра
    # изменение игрового мира
    # ...
    # временная задержка
    clock.tick(fps)
