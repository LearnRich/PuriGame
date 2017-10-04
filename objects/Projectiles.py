from framework import Globals
from objects import GameObject
import pygame


class Bullet(GameObject.GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 2, 5, 0, 5)
        self.color = Globals.RED

    def draw(self, screen):
        pygame.draw.line(screen, self.color,
                [self.x, self.y],
                [self.x, self.y+self.height],
                self.width)

    def move(self):
        self.y -= self.vel_y

    def collision_check(self, enemy):
        if self.x <= enemy.x + enemy.width and \
                                self.x + self.width >= enemy.x:
            if self.y <= enemy.y + enemy.height and \
                                    self.y + self.height >= enemy.y:
                return True
        return False

    def on_screen(self):
        if self.x - self.width > 0 and self.x < Globals.WIDTH:
            if self.y + self.height > 0:
                return True