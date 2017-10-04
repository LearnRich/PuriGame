import pygame
import random
from objects import GameObject
from framework import Globals

class Enemy(GameObject.GameObject):
    def __init__(self, x, y, w, h, vx, vy, speed_mod):
        super().__init__(x, y, w, h, vx, vy)
        self.speed_mod = speed_mod


class BasicEnemy(Enemy):
    def __init__(self, speed_mod):
        super().__init__(random.randrange(Globals.WIDTH),
                         random.randrange(-150, -10), 20, 32,
                         0,
                         random.randrange(1, 3),
                         speed_mod)
        self.color = Globals.BLUE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x,
                                               self.y,
                                               self.width,
                                               self.height])

    def move(self):
        self.y += self.vel_y


class SmartEnemy(Enemy):
    def __init__(self, speed_mod):
        super().__init__(random.randrange(Globals.WIDTH),
                         random.randrange(-150, -10), 20, 32,
                         random.randrange(1, 6),
                         random.randrange(1, 6),
                         speed_mod)
        self.color = Globals.BLUE

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, [self.x, self.y], self.width)

    def move(self):
        self.y += self.vel_y
        if self.x - self.width / 2 <= 0 or self.x + self.width / 2 >= Globals.WIDTH:
            self.vel_x *= -1

        self.x += self.vel_x


class SuperSmartEnemy(Enemy):
    def __init__(self, speed_mod, the_player):
        super().__init__(random.randrange(Globals.WIDTH),
                         random.randrange(-150, -10), 20, 32,
                         random.randrange(1, 6),
                         random.randrange(1, 6),
                         speed_mod)
        self.color = Globals.GREEN
        self.player = the_player

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.width, self.height])

    def move(self):
        self.y += self.vel_y
        if self.x < self.player.x:
            self.vel_x *= -1
        elif self.x > self.player.x:
            self.vel_x = self.vel_y
        else:
            self.vel_x = 0
        self.x += self.vel_x
