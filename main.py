# Import a library of functions called 'pygame'
import pygame
from objects import Player
from framework import Globals, Handler, HUD


class Game:
    def __init__(self):
        print("INIT")
        self.game_state = Globals.MENU
        self.screen = pygame.display.set_mode(Globals.SIZE)
        pygame.display.set_caption("Game Name")
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('./res/sound/mario_elevator.mp3')
        pygame.mixer.music.play(-1)
        self.shootSound = pygame.mixer.Sound("./res/sound/Laser_Shoot.wav")
        self.hud = HUD.HUD()
        self.player = Player.Player()
        self.handler = Handler.Handler(self.player, self.hud)
        for counter in range(0, 5):
            self.handler.add_new_enemy()
        self.background = pygame.image.load("./res/background.png").convert()


    def run(self):
        running = True
        while running:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.handler.player.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.handler.player.move_right()
                elif event.key == pygame.K_SPACE:
                    self.shootSound.play()
                    self.handler.add_laser(self.player.shoot())
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.handler.player.stop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_selected = self.handler.menu.get_clicked()
                if button_selected:
                    print("Button that was clicked is:", button_selected.text)
                    if button_selected.text == Globals.NEW_GAME:
                        self.game_state = Globals.GAME_RUNNING

            if self.game_state == Globals.MENU:
                self.menu_main()
            elif self.game_state == Globals.GAME_RUNNING:
                self.game_play()
                if self.player.health <= 0:
                    self.game_state=Globals.GAME_OVER
            elif self.game_state/'' \
                                 '' == Globals.GAME_OVER:
                self.menu_main()
            else:
                print("ERROR ERROR ERROR GAME STATE OUT OF RANGE!")

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            self.clock.tick(60)

    def menu_main(self):
        self.handler.menu.draw_all(self.screen)
        self.handler.menu.update()

    def menu_high_score(self):
        print("menu high score")

    def menu_credits(self):
        print("menu high score")

    def game_play(self):
        # UPDATE CODE GOES HERE
        self.handler.update()

        # DRAWING CODE GOES HERE
        self.screen.blit(self.background, (0, 0))
        self.handler.draw_objects(self.screen)

    def game_over(self):
        font = pygame.font.SysFont("Calibri", 42, True, False)
        score_text = font.render("GAME OVER", True, Globals.WHITE)
        self.screen.blit(score_text, [Globals.WIDTH / 2 - 75, Globals.HEIGHT / 2 - 10])


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
