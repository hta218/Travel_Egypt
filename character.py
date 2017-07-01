import pygame

class Character:
    def __init__(self, x, y, image, correct_pos):
        self.x = x
        self.y = y
        self.image = image
        self.correct_pos = correct_pos

    def move(self, screen, game):
        dx = game.blank_block["x"] - self.x
        dy = game.blank_block["y"] - self.y
        x = self.x * game.size + (game.size - self.image.get_width()) / 2
        y = self.y * game.size + (game.size - self.image.get_height()) / 2
        if dx != 0:
            for i in range(int(game.size)):
                x += dx
                screen.blit(game.background, (game.blank_block["x"] * game.size + game.map.dx, \
                          game.blank_block["y"] * game.size + game.map.dy))
                screen.blit(game.background, (self.x * game.size + game.map.dx, \
                              self.y * game.size + game.map.dy))
                screen.blit(self.image, (x + game.map.dx, y + game.map.dy))
                pygame.display.flip()
        else:
            for i in range(int(game.size)):
                y += dy
                screen.blit(game.background, (game.blank_block["x"] * game.size + game.map.dx, \
                          game.blank_block["y"] * game.size + game.map.dy))
                screen.blit(game.background, (self.x * game.size + game.map.dx, \
                                  self.y * game.size + game.map.dy))
                screen.blit(self.image, (x + game.map.dx, y + game.map.dy))
                pygame.display.flip()

        game.blank_block["x"] -= dx
        game.blank_block["y"] -= dy
        self.x += dx
        self.y += dy

    def able_to_move(self, game):
        able = False
        if abs(self.x - game.blank_block["x"]) + abs(self.y - game.blank_block["y"]) == 1:
            able = True
        return able