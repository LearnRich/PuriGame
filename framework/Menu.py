import pygame


class Button:
    hovered = False

    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.font = pygame.font.Font(None, 50)
        self.set_rect()

    def draw(self, screen):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = self.font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos


class Menu():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.button_list = []
        self.cols = 1

    def add_options(self, button_name_list):
        x_mod = 0
        counter = 0
        button_height = 50
        for name in button_name_list:
            self.button_list.append(
                Button(name, (self.x, self.y+(counter*button_height))))
            counter += 1

    def draw_all(self, screen):
        for button in self.button_list:
            button.draw(screen)


    def set_grid_dimensions(self, c):
        self.cols = c

    def update(self):
        for button in self.button_list:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                button.hovered = True
            else:
                button.hovered = False

    def get_clicked(self):
        for button in self.button_list:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                return button
        return None
