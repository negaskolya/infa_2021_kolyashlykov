from pygame import draw
from constants import *
from random import randint


class Target:
    """
    Класс Target, в котором объявляются методы движения цели и удаление её, когда это понадобится
    x - x координата цели
    y - y координата цели
    r - геометрический параметр цели
    Vx - x-копонента скорости
    Vy - y-компонента скорости
    price - стоимость данной цели
    """

    def move(self):
        """ метод реализующий движение цели """
        self.x += self.Vx
        self.y += self.Vy
        if self.x + self.r > SCREEN_WIDTH:
            self.Vx = randint(-10, 0)
            self.Vy = randint(-10, 10)
        if self.x - self.r < 0:
            self.Vx = randint(0, 10)
            self.Vy = randint(-10, 10)
        if self.y + self.r > SCREEN_HEIGHT:
            self.Vx = randint(-10, 10)
            self.Vy = randint(-10, 0)
        if self.y - self.r < 0:
            self.Vx = randint(-10, -10)
            self.Vy = randint(0, 10)

    def remove_target(self):
        """ метод, реализующий удаление цели """
        self.game.targets.remove(self)


class Ball(Target):
    """
    Дочерний класс Ball класса Target
    x - x координата
    y - y координата
    r - радиус шара
    Vx - x кмпонента скорости
    Vy - y компонента скорости
    price - стоимость шара
    """
    def __init__(self, game):
        self.game = game
        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.r = randint(30, 50)
        self.Vx = randint(-10, 10)
        self.Vy = randint(-10, 10)
        self.color = COLORS[randint(0, 5)]
        self.price = randint(1, 5)

    def render(self, screen):
        """ Отрисовка шара """
        draw.circle(screen, self.color, (self.x, self.y), self.r)
        screen.blit(self.game.user_font.render(str(self.price), False, (0, 0, 0)), (self.x, self.y-20))


class Cube(Target):
    """
    Дочерний класс Cube класса Target
    x - x координата
    y - y координата
    r - длина стороны квадрата
    Vx - x кмпонента скорости
    Vy - y компонента скорости
    price - стоимость данной мишени
    """
    def __init__(self, game):
        self.game = game
        self.x = randint(100, 700)
        self.y = randint(100, 500)
        self.r = randint(40, 60)/2
        self.Vx = 5
        self.Vy = 60
        self.color = COLORS[randint(0, 5)]
        self.price = randint(10, 20)

    def move(self):
        """ метод реализующий движение куба
        переобозначаем родительский метод движения, чтобы поменять характер движения """
        self.x += self.Vx
        self.y += self.Vy
        if self.x + self.r > SCREEN_WIDTH:
            self.Vx *= -1
        if self.x - self.r < 0:
            self.Vx *= -1
        if self.y + self.r > SCREEN_HEIGHT:
            self.Vy *= -1
        if self.y - self.r < 0:
            self.Vy *= -1

    def render(self, screen):
        """ Отрисовка куба """
        draw.rect(screen, self.color, (self.x - self.r, self.y - self.r, self.r*2, self.r*2))
        screen.blit(self.game.user_font.render(str(self.price), False, (0, 0, 0)), (self.x - 10, self.y-20))