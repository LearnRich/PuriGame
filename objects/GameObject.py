from framework import Globals

class GameObject:
    def __init__(self, x, y, w, h, vel_x, vel_y):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.vel_x = vel_x
        self.vel_y = vel_y

    def __str__(self):
        return "xPos: " + str(self.x) + " || yPos: " + str(self.y)

    def out_of_bounds(self):
        if self.x - self.width -2 < 0 or \
                self.x + 2 > Globals.WIDTH or \
                self.y + self.height < -100 or \
                self.y + 2 > Globals.HEIGHT:
            return True
