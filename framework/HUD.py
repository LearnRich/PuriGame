from framework import Globals
import pygame

class HUD():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 25

    def draw(self, screen, player):
        pygame.draw.rect(screen, (67,70,75), [self.x, self.y, Globals.WIDTH, self.height])
        font = pygame.font.SysFont("Calibri", 18, True, False)
        score_text = font.render("Score: " + str(player.score), True, Globals.WHITE)
        screen.blit(score_text, [15, 1])

        level_text = font.render("Level: " + str(player.level), True, Globals.WHITE)
        screen.blit(level_text, [Globals.WIDTH/2-30, 1])

        pygame.draw.rect(screen, (0,255,0), [Globals.WIDTH-115, 4, 100, 15])
        pygame.draw.rect(screen, (255, 0, 0),
                         [Globals.WIDTH - 115+player.health, 4, 100-player.health, 15])
        pygame.draw.rect(screen, (255, 255, 255), [Globals.WIDTH - 115, 4, 100,15], 2)
