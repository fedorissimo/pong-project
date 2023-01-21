import pygame

# size = width, height = [int(i) for i in input('Введите размеры экрана').split()]
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
    pygame.draw.rect(screen, firstplatformcolor, firstplatformcords)
    pygame.draw.rect(screen, secondplatformcolor, secondplatformcords)
    pygame.draw.circle(screen, ballcolor, ballcords, 10)
    pygame.display.flip() # смена кадра
    # изменение игрового мира
    # ...
    # временная задержка
    clock.tick(fps)
