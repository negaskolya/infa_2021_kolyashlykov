import pygame
from target_class import *
from constants import *
from random import randint


class Game:
    """
    Основной класс игры
    targets - список, содержащий объекты классов Ball и Cube - мишеней
    counter - счёт игрока
    self.start() - запускает игру при инициализации объекта класса
    """
    def __init__(self, screen):
        self.screen = screen
        self.user_font = pygame.font.SysFont("Comic Sans MS", 30)
        self.counter = 0
        self.run = True
        self.targets = []
        self.start()

    def handle_events(self):
        """
        Метод класса Game
        Обработка событий
        Удаляет мишень после клика в его области
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for j in self.targets:
                    if abs(event.pos[0] - j.x) < j.r and abs(event.pos[1] - j.y) < j.r:
                        self.counter += j.price
                        j.remove_target()

    def main_render(self):
        """
        Создание экрана и отрисовка каждого из шаров
        """
        self.screen.fill(BLACK)
        for i in self.targets:
            i.render(self.screen)
        self.screen.blit(self.user_font.render(f'Score: {self.counter}', False, (255, 255, 255)), (10, 10))

    def start(self):
        """
        создание целей и занесение их в targets
        основной цикл программы
        """
        i = 0
        while i < randint(5, 7):
            self.targets.append(Ball(self))
            i += 1
        i = 0

        while i < randint(5, 7):
            self.targets.append(Cube(self))
            i += 1

        clock = pygame.time.Clock()
        while self.run:
            clock.tick(FPS)
            self.handle_events()
            if len(self.targets) == 0:
                self.run = False
            for i in self.targets:
                i.move()
            self.main_render()
            pygame.display.update()


pygame.init()
screen1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game1 = Game(screen1)