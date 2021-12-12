import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30  # задаем FPS
screen = pygame.display.set_mode((600, 800))  # создаем экран

# задаем цвета
blue = (0, 184, 217)
grey = (133, 150, 150)
white = (255, 255, 255)
green = (153, 255, 153)
dark_green = (80, 200, 120)
yellow = (255, 255, 0)
purple = (128, 0, 255)
black = (0, 0, 0)

# небо
rect(screen, blue, (0, 0, 600, 400), 0)

# трава
rect(screen, green, (0, 400, 600, 400), 0)

# горы
polygon(screen, grey,
        [(0, 250), (60, 100), (120, 200), (200, 125), (380, 280), (430, 110), (470, 140), (600, 50), (600, 450),
         (350, 450), (330, 400), (0, 400), (0, 250)], 0)
polygon(screen, black,
        [(0, 250), (60, 100), (120, 200), (200, 125), (380, 280), (430, 110), (470, 140), (600, 50), (600, 450),
         (350, 450), (330, 400), (0, 400), (0, 250)], 1)


# функция альпаки
def alpaka(x, y, k, n):
    '''   Функция, рисующая альпаку
    если n == 1, альпака смотрит вправо
    если n == -1, альпака смотрит влево
    x, y - координаты левого верхнего угла прямоугольника головы при n == 1 и правого верхнего угла при n == -1
    k - относительный размер. При k == 1 размеры головы 50 на 30
    '''
    if (n == 1):
        ellipse(screen, white, (x, y, 50 * k, 30 * k), 0)  # голова смотрит вправо
        arc(screen, (255, 0, 0), (x + 5 * k, y - 20 * k, 12 * k, 25 * k), math.pi, 3 * math.pi / 2, 2)  # рог 1
        arc(screen, (255, 0, 0), (x, y - 25 * k, 12 * k, 32 * k), math.pi, 3 * math.pi / 2, 2)  # рог 2
        ellipse(screen, white, (x + 5 * k * n, y + 25 * k, 35 * k, 100 * k), 0)  # шея
        ellipse(screen, white, (x - 115 * k * n, y + 110 * k, 150 * k, 55 * k), 0)  # туловище
        ellipse(screen, white, (x - 105 * k * n, y + 145 * k, 15 * k, 35 * k), 0)  # нога левая задняя 1
        ellipse(screen, white, (x - 105 * k * n, y + 175 * k, 15 * k, 35 * k), 0)  # нога левая задняя 2
        ellipse(screen, white, (x - 102 * k * n, y + 205 * k, 20 * k, 10 * k), 0)  # нога левая задняя 3
        ellipse(screen, white, (x - 75 * k * n, y + 155 * k, 15 * k, 35 * k), 0)  # нога правая задняя 1
        ellipse(screen, white, (x - 75 * k * n, y + 185 * k, 15 * k, 35 * k), 0)  # нога правая задняя 2
        ellipse(screen, white, (x - 72 * k * n, y + 215 * k, 20 * k, 10 * k), 0)  # нога правая задняя 3
        ellipse(screen, white, (x - 15 * k * n, y + 145 * k, 15 * k, 35 * k), 0)  # нога левая передняя 1
        ellipse(screen, white, (x - 15 * k * n, y + 175 * k, 15 * k, 35 * k), 0)  # нога левая передняя 2
        ellipse(screen, white, (x - 12 * k * n, y + 205 * k, 20 * k, 10 * k), 0)  # нога левая передняя 3
        ellipse(screen, white, (x + 10 * k * n, y + 150 * k, 15 * k, 35 * k), 0)  # нога правая передняя 1
        ellipse(screen, white, (x + 10 * k * n, y + 180 * k, 15 * k, 35 * k), 0)  # нога правая передняя 2
        ellipse(screen, white, (x + 13 * k * n, y + 210 * k, 20 * k, 10 * k), 0)  # нога правая передняя 3
        circle(screen, purple, (x + 20 * k * n, y + 13 * k), 8 * k, 0)  # глаз
        circle(screen, black, (x + 24 * k * n, y + 13 * k), 3 * k, 0)  # зрачок
        ellipse(screen, white, (x + 18 * k * n, y + 10 * k, 5 * k, 2 * k), 0)  # блик
    else:
        ellipse(screen, white, (x - 50 * k, y, 50 * k, 30 * k), 0)  # голова смотрит влево
        arc(screen, (255, 0, 0), (x - 5 * k - 12 * k, y - 20 * k, 12 * k, 25 * k), 3 * math.pi / 2, 2 * math.pi, 2)  # рог 1
        arc(screen, (255, 0, 0), (x - 12 * k, y - 25 * k, 12 * k, 32 * k), 3 * math.pi / 2, 2 * math.pi, 2)  # рог 2
        ellipse(screen, white, (x + 5 * k * n - 35 * k, y + 25 * k, 35 * k, 100 * k), 0)  # шея
        ellipse(screen, white, (x - 115 * k * n - 150 * k, y + 110 * k, 150 * k, 55 * k), 0)  # туловище
        ellipse(screen, white, (x - 105 * k * n - 15 * k, y + 145 * k, 15 * k, 35 * k), 0)  # нога левая задняя 1
        ellipse(screen, white, (x - 105 * k * n - 15 * k, y + 175 * k, 15 * k, 35 * k), 0)  # нога левая задняя 2
        ellipse(screen, white, (x - 102 * k * n - 20 * k, y + 205 * k, 20 * k, 10 * k), 0)  # нога левая задняя 3
        ellipse(screen, white, (x - 75 * k * n - 15 * k, y + 155 * k, 15 * k, 35 * k), 0)  # нога правая задняя 1
        ellipse(screen, white, (x - 75 * k * n - 15 * k, y + 185 * k, 15 * k, 35 * k), 0)  # нога правая задняя 2
        ellipse(screen, white, (x - 72 * k * n - 20 * k, y + 215 * k, 20 * k, 10 * k), 0)  # нога правая задняя 3
        ellipse(screen, white, (x - 15 * k * n - 15 * k, y + 145 * k, 15 * k, 35 * k), 0)  # нога левая передняя 1
        ellipse(screen, white, (x - 15 * k * n - 15 * k, y + 175 * k, 15 * k, 35 * k), 0)  # нога левая передняя 2
        ellipse(screen, white, (x - 12 * k * n - 20 * k, y + 205 * k, 20 * k, 10 * k), 0)  # нога левая передняя 3
        ellipse(screen, white, (x + 10 * k * n - 15 * k, y + 150 * k, 15 * k, 35 * k), 0)  # нога правая передняя 1
        ellipse(screen, white, (x + 10 * k * n - 15 * k, y + 180 * k, 15 * k, 35 * k), 0)  # нога правая передняя 2
        ellipse(screen, white, (x + 13 * k * n - 20 * k, y + 210 * k, 20 * k, 10 * k), 0)  # нога правая передняя 3
        circle(screen, purple, (x + 20 * k * n, y + 13 * k), 8 * k, 0)  # глаз
        circle(screen, black, (x + 24 * k * n, y + 13 * k), 3 * k, 0)  # зрачок
        ellipse(screen, white, (x + 18 * k * n - 5 * k, y + 10 * k, 5 * k, 2 * k), 0)  # блик


# функция цветка
def cvetok(x, y, k):
    '''   Функция, рисующая цветок
    x, y - координаты левого верхнего угла центрального верхнего лепестка
    k - относительный размер цветка. При k == 1 размер лепестков 22 на 11
    '''
    ellipse(screen, blue, (x, y, 22 * k, 11 * k), 0)  # рисуем лепестки
    ellipse(screen, blue, (x + 10 * k, y + 3 * k, 22 * k, 11 * k), 0)
    ellipse(screen, blue, (x - 9 * k, y + 4 * k, 22 * k, 11 * k), 0)
    ellipse(screen, yellow, (x + 2 * k, y + 9 * k, 22 * k, 11 * k), 0)
    ellipse(screen, blue, (x - 12 * k, y + 11 * k, 22 * k, 11 * k), 0)
    ellipse(screen, blue, (x - 4 * k, y + 15 * k, 22 * k, 11 * k), 0)
    ellipse(screen, blue, (x + 14 * k, y + 10 * k, 22 * k, 11 * k), 0)
    ellipse(screen, blue, (x + 10 * k, y + 15 * k, 22 * k, 11 * k), 0)


# клумба с цветами
def clumba(i, j, l):
    '''  Функция, рисующая клумбу с цветами.
    i, j - координаты верхнего края самой клумбы.
    l - относительный размер клумбы. При l == 1 сама клумба имеет радиус 110, а лепестки цветов размеры 22 на 11
    '''
    circle(screen, dark_green, (i, j + 110 * l), 110 * l, 0)  # рисуем саму клумбу
    cvetok(i - 4 * l, j + 20 * l, l)  # рисуем цветки по часовой стрелке с самого верхнего
    cvetok(i + 38 * l, j + 50 * l, l)
    cvetok(i + 53 * l, j + 110 * l, l)
    cvetok(i - 5 * l, j + 140 * l, l)
    cvetok(i - 57 * l, j + 115 * l, l)
    cvetok(i - 70 * l, j + 60 * l, l)
    cvetok(i - 10 * l, j + 90 * l, l)
    cvetok(i + 40 * l, j + 80 * l, l)
    cvetok(i - 20 * l, j + 180 * l, l)


# теперь рисуем альпак и клумбы
clumba(60, 410, 0.2)
clumba(440, 475, 0.25)
clumba(575, 430, 0.35)
clumba(585, 525, 0.5)
clumba(440, 640, 0.65)
clumba(590, 735, 0.18)

alpaka(67, 550, 3, 1)
alpaka(190, 420, 0.4, 1)
alpaka(275, 335, 0.45, 1)
alpaka(560, 440, 1.2, -1)
alpaka(275, 460, 0.4, -1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()