from objects import GameObject, Player, Enemy, Projectiles
from framework import Globals
import pygame

class Handler:
    def __init__(self, player, hud):
        self.player = player
        self.laser_list = []
        self.enemy_list = []
        self.object_list = []
        self.hud = hud

    def update(self):
        # move the player
        self.player.move()

        #move the enemies
        for enemy in self.enemy_list:
            enemy.move()

        #move the lasers
        for laser in self.laser_list:
            laser.move()

        #move the objects
        for object in self.object_list:
            object.move()

        #detect and remove laser collisions
        for laser in self.laser_list:
            if not laser.out_of_bounds():
                for enemy in self.enemy_list:
                    if laser.collision_check(enemy):
                        print("Collision Between Enemy and Laser")
                        self.player.add_score(enemy)
                        self.remove(laser, enemy)
                        self.add_new_enemy()
                        continue
            else:
                print("Removing an off screen laser")
                self.laser_list.remove(laser)

        #detect and remove objects that collide with player

        for enemy in self.enemy_list:
            if self.player.collision_check(enemy):
                self.player.collided()
                self.remove(enemy)
                self.add_new_enemy()

        for object in self.object_list:
            if self.player.collision_check(object):
                self.player.collided()
                self.remove(object)

        self.player.update_lvl()

    def draw_objects(self, screen):
        for laser in self.laser_list:
            laser.draw(screen)

        self.player.draw(screen)

        for enemy in self.enemy_list:
            #print(enemy)
            enemy.draw(screen)

        self.hud.draw(screen, self.player)

    def add_new_enemy(self):
        new_enemy = Enemy.SuperSmartEnemy(2, self.player)
        if self.player.level == 1:
            print("Level 1 - Add Basic Slow")
            new_enemy = Enemy.BasicEnemy(0.5)
        elif self.player.level == 2:
            print("Level 2 - Add Basic Fast")
            new_enemy = Enemy.BasicEnemy(1)
        elif self.player.level == 3:
            print("Level 3 - Add Smart")
            new_enemy = Enemy.SmartEnemy(1)
        elif self.player.level == 4:
            print("Level 3 - Add Smart")
            new_enemy = Enemy.SmartEnemy(1)
        elif self.player.level == 5:
            new_enemy = Enemy.SuperSmartEnemy(0.5, self.player)
        elif self.player.level == 6:
            new_enemy = Enemy.SuperSmartEnemy(1, self.player)
        self.enemy_list.append(new_enemy)

    def add_enemy(self, enemy):
        self.enemy_list.append(enemy)

    def add_laser(self, laser):
        self.laser_list.append(laser)

    def add_object(self, object):
        self.object_list.append(object)

    def remove(self, *objs):
        print("REMOVING OBJECTS:", len(objs))
        for obj in objs:
            if issubclass(type(obj), Enemy.Enemy):
                print("ENEMY LIST BEFORE:" , len(self.enemy_list))
                self.enemy_list.remove(obj)
                print("ENEMY LIST AFTER:" , len(self.enemy_list))
            elif type(obj) is Projectiles.Bullet:
                self.laser_list.remove(obj)
                print("LASER LIST AFTER:", len(self.laser_list))

    def remove_laser(self, laser):
        self.enemy.remove(laser)


