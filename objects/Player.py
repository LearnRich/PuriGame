import random, pygame, math
from framework import Globals, SpriteSheet
from objects import GameObject, Projectiles, Enemy


class Player(GameObject.GameObject):
    def __init__(self):
        super().__init__(Globals.WIDTH/2 - 20, Globals.HEIGHT - 75, 20, 32, 0, 0)
        self.color = Globals.RED
        self.health = 100
        self.score = 0
        self.score_change = False
        self.level = 1
        self.anim_speed_init = 10
        self.anim_speed = self.anim_speed_init
        self.sprite_sheet = SpriteSheet.SpriteSheet("./res/puri/puri_sheet.png")

        self.anim_idle = [
            self.sprite_sheet.get_image(0, 0, Globals.IMG_WIDTH, Globals.IMG_HEIGHT),
            self.sprite_sheet.get_image(32, 0, Globals.IMG_WIDTH, Globals.IMG_HEIGHT),
        ]
        self.anim_right = [
            self.sprite_sheet.get_image(64, 0, Globals.IMG_WIDTH, Globals.IMG_HEIGHT),
            self.sprite_sheet.get_image(0, 32, Globals.IMG_WIDTH, Globals.IMG_HEIGHT),
            self.sprite_sheet.get_image(32, 32, Globals.IMG_WIDTH, Globals.IMG_HEIGHT),
            self.sprite_sheet.get_image(64, 32, Globals.IMG_WIDTH, Globals.IMG_HEIGHT)
        ]

        self.anim_left = [
            pygame.transform.flip(
                self.sprite_sheet.get_image(64,
                                            0,
                                            Globals.IMG_WIDTH,
                                            Globals.IMG_HEIGHT),
                True,
                False),
            pygame.transform.flip(self.sprite_sheet.get_image(0, 32, Globals.IMG_WIDTH, Globals.IMG_HEIGHT),True, False),
            pygame.transform.flip(self.sprite_sheet.get_image(32, 32, Globals.IMG_WIDTH, Globals.IMG_HEIGHT),True, False),
            pygame.transform.flip(self.sprite_sheet.get_image(64, 32, Globals.IMG_WIDTH, Globals.IMG_HEIGHT),True, False)
        ]

        self.anim_pos = 0
        self.anim_idle_max = len(self.anim_idle)-1
        self.anim_right_max = len(self.anim_right)-1
        self.anim_left_max = len(self.anim_left)-1
        self.img = self.anim_idle[0]

    def draw(self, surface):
        surface.blit(self.img, (self.x, self.y, 32, 32))
        pygame.draw.rect(surface, Globals.GREEN, (self.x, self.y, 32, 32), 2)

    def collision_check(self, enemy):
        if self.x <= enemy.x + enemy.width and self.x + self.width >= enemy.x:
            if self.y <= enemy.y + enemy.height and self.y + self.height >= enemy.y:
                return True
        return False

    def collided(self):
        self.color = [random.randrange(255), random.randrange(255), random.randrange(255)]
        if self.health > 0:
            self.health -= 10

    def shoot(self):
        x = self.x+self.width/2
        y = self.y
        new_bullet = Projectiles.Bullet(x, y)
        return new_bullet

    def add_score(self, enemy):
        print(self.score)
        if type(enemy) is Enemy.BasicEnemy:
            self.score += 1
        elif type(enemy) is Enemy.SmartEnemy:
            self.score += 5
        self.score_change = True
        print(self.score)

    def move_left(self):
        self.vel_x = -5

    def move_right(self):
        self.vel_x = 5

    def move(self):
        if self.health > 0:
            if self.x < 0:
                self.x = Globals.WIDTH + 1
            elif self.x + self.vel_x > Globals.WIDTH:
                self.x = 0
            self.x += self.vel_x

            self.anim_speed -= 1
            if self.anim_speed == 0:
                # If IDLE
                if self.vel_x == 0:
                # IDLE ANIM
                    # changes here
                    if self.anim_pos >= self.anim_idle_max:
                        self.anim_pos = 0
                    else:
                        self.anim_pos += 1
                    self.img = self.anim_idle[self.anim_pos]
                    self.anim_speed = self.anim_speed_init
                elif self.vel_x > 0:
                    if self.anim_pos >= self.anim_right_max:
                        self.anim_pos = 0
                    else:
                        self.anim_pos += 1
                    self.img = self.anim_right[self.anim_pos]
                    self.anim_speed = self.anim_speed_init
                elif self.vel_x < 0:
                    if self.anim_pos >= self.anim_left_max:
                        self.anim_pos = 0
                    else:
                        self.anim_pos += 1
                    self.img = self.anim_left[self.anim_pos]
                    self.anim_speed = self.anim_speed_init

    def stop(self):
        self.vel_x = 0

    def update_lvl(self):
        if self.score > 2 and self.score_change:
            lvlcheck = math.log(self.score, 2)
            if lvlcheck.is_integer():
                self.level += 1
        self.score_change = False
