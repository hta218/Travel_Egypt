import sys
import random
from map import Map
from time import sleep
from configs import *
import pygame

pygame.init()
MOUSE_LEFT = 1
BLACK = (0, 0, 0)

letgo_sound = pygame.mixer.Sound('Sound/Special/letgo.wav')
select_mode = pygame.mixer.Sound('Sound/Click/select_mode.wav')
move_level = pygame.mixer.Sound('Sound/Click/move_level.wav')
block_move = pygame.mixer.Sound('Sound/Click/block_move.wav')
nope = pygame.mixer.Sound('Sound/Special/nope.wav')
quit_sound = pygame.mixer.Sound('Sound/Special/quit.wav')

class Game:
    def __init__(self, map):
        self.map = map
        self.background = block_44
        self.size = 155
        self.blank_block = {
            "x" : 0,
            "y" : 3
        }

        self.welcome = True
        self.preload = False
        self.music_playing = False
        self.selected_mode = False
        self.victory = False

        self.level = self.map.level_no
        self.active_level = 0
        self.mode = {
            "easy"      :   20,
            "medium"    :   40,
            "hard"      :   60
        }
        self.mode_choosed = self.mode["easy"]

    def start(self, screen):
        screen.blit(welcome, (0, 0))
        screen.blit(letsgo, (450, 253))

    def quit(self):
        quit_sound.play()
        sleep(6)
        pygame.quit()
        sys.exit(1)

    def print_mode(self, screen):
        screen.blit(mode, (0, 0))
        screen.blit(easy, (180, 473))
        screen.blit(medium, (430, 473))
        screen.blit(hard, (680, 473))
        pygame.display.flip()

    def select_mode(self, event, screen):
        if event.button == MOUSE_LEFT:
            x, y = pygame.mouse.get_pos()
            if (180 <= x <= 180 + 201 and 473 <= y <= 473 + 83):    # easy
                screen.blit(easy_click, (180, 473))
                self.mode_choosed = self.mode["easy"]
                self.selected_mode = True
            elif (430 <= x <= 430 + 201 and 473 <= y <= 473 + 83):  #medium
                screen.blit(medium_click, (430, 473))
                self.mode_choosed = self.mode["medium"]
                self.selected_mode = True
            elif (680 <= x <= 680 + 201 and 473 <= y <= 473 + 83):  #hard
                screen.blit(hard_click, (680, 473))
                self.mode_choosed = self.mode["hard"]
                self.selected_mode = True
        if self.selected_mode is True:
            pygame.display.flip()
            select_mode.play()
            sleep(1)
            self.pre_load(screen)

    def pre_load(self, screen):
        self.set_blocks_pos()
        screen.blit(bg, (0, 0))
        screen.blit(self.map.win_images[2], (870, 450))
        screen.blit(next, (817, 294))
        screen.blit(back, (817, 345))
        screen.blit(quit, (840, 630))
        self.print_map(screen)
        self.print_game_status(screen)
        if self.music_playing is not True:
            pygame.mixer.music.load(self.map.sound_path)
            pygame.mixer.music.play(-1)
            self.music_playing = True
        self.preload = True

    def print_game_status(self, screen):
        move = font.render(str(self.map.move), True, BLACK)
        level = font.render(str(self.level + 1) + "/8", True, BLACK)
        screen.blit(game_status, (808, 202))
        if self.map.move < 10:
            screen.blit(move, (940, 210))
        elif self.map.move < 100:
            screen.blit(move, (934, 210))
        else:
            screen.blit(move, (930, 210))
        screen.blit(level, (934, 257))

    def let_go(self, event, screen):
        if event.button == MOUSE_LEFT:
            x, y = pygame.mouse.get_pos()
            if (450 <= x <= 450 + 198 and 253 <= y <= 253 + 75):
                self.welcome = False
                screen.blit(letsgo_click, (450, 253))
                pygame.display.flip()
                letgo_sound.play()
                sleep(1)
        if self.welcome is False:
            self.print_mode(screen)

    def print_map(self, screen):
        if self.level >= 4:
            self.background = block_55
        else:
            self.background = block_44
        for y in range(self.map.size_y):
            for x in range(self.map.size_x):
                screen.blit(self.background, (x * self.size + self.map.dx, \
                                  y * self.size + self.map.dy))
                if x != self.blank_block["x"] or y != self.blank_block["y"]:
                    block = self.map.blocks[y][x]
                    if block is None:
                        block = self.map.get_block(x, y)
                    self.draw_image_center(block.image, block.x, block.y, screen)

    def set_blocks_pos(self):
        count = 0
        complete = False
        while not complete:
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            if (0 <= self.blank_block["x"] + dx <= self.map.size_x - 1) \
                and (0 <= self.blank_block["y"] + dy <= self.map.size_y - 1) \
                    and abs(dx) + abs(dy) == 1:
                self.blank_block["x"] += dx     # x = 1
                self.blank_block["y"] += dy

                temp = self.map.blocks[self.blank_block["y"]][self.blank_block["x"]]    # [3][1]
                self.map.blocks[self.blank_block["y"]][self.blank_block["x"]] = None
                self.map.blocks[self.blank_block["y"] - dy][self.blank_block["x"] - dx] = temp

                self.map.blocks[self.blank_block["y"] - dy][self.blank_block["x"] - dx].x -= dx
                self.map.blocks[self.blank_block["y"] - dy][self.blank_block["x"] - dx].y -= dy
                count += 1

            if count == self.mode_choosed:
                complete = True

    def handle_input(self, event, screen):
        NEXT = 1
        PREVIOUS = -1
        block = None
        if event.button == MOUSE_LEFT:
            x, y = pygame.mouse.get_pos()
            if 0 < x < self.map.size_x * self.size + self.map.dx and \
                    self.map.dy < y < self.map.size_y * self.size + self.map.dy:
                x = (x - self.map.dx) // self.size
                y = (y - self.map.dy) // self.size
                block = self.map.get_block(x, y)
                return block
            elif 817 <= x <= 817 + next.get_width() and 294 <= y <= 294 + next.get_height():
                if self.level < 7 and self.level < self.active_level:
                    move_level.play()
                    screen.blit(next_click, (817, 294))
                    pygame.display.flip()
                    sleep(0.3)
                    self.get_to_level(screen, NEXT)
                else:
                    nope.play()

            elif 817 <= x <= 817 + back.get_width() and 345 <= y <= 345 + back.get_height():
                if self.level > 0:
                    move_level.play()
                    screen.blit(back_click, (817, 345))
                    pygame.display.flip()
                    sleep(0.3)
                    self.get_to_level(screen, PREVIOUS)
                else:
                    nope.play()
            elif 840 <= x <= 840 + quit.get_width() and 630 <= y <= 630 + quit.get_height():
                block_move.play()
                screen.blit(quit_click, (840, 630))
                pygame.display.flip()
                sleep(0.3)
                self.quit()
        return block

    def draw_image_center(self, img, x, y, screen):
        w = (self.size - img.get_width()) / 2 + (x * self.size) + self.map.dx
        h = (self.size - img.get_height()) / 2 + (y * self.size) + self.map.dy
        screen.blit(img, (w, h))

    def selected_level(self, event, screen):
        if self.level < 7:
            if event.button == MOUSE_LEFT:
                x, y = pygame.mouse.get_pos()
                if self.map.level.item_x < x < self.map.level.item_x + \
                        self.map.level.item_width and \
                    self.map.level.item_y < y < self.map.level.item_y + \
                                self.map.level.item_height:
                    screen.blit(self.map.win_images[1], (0, 0))
                    pygame.display.flip()
                    select_mode.play()
                    return True
        return False

    def get_to_level(self, screen, delta):
        pygame.mixer.music.stop()
        self.music_playing = False
        self.level += delta
        if self.level < 4:
            map = Map(4, 4, self.level)
            map.blocks = map.level.create_new_blocks()
            self.blank_block["x"] = 0
            self.blank_block["y"] = 3
            self.size = 155
        else:
            map = Map(5, 5, self.level)
            map.blocks = map.level.create_new_blocks()
            self.blank_block["x"] = 0
            self.blank_block["y"] = 4
            self.size = 125
            self.mode = {
                "easy"  : 30,
                "medium": 50,
                "hard"  : 70
            }
        self.map = map
        self.pre_load(screen)

    def loop(self, screen, event):
        block = self.handle_input(event, screen)
        if block is not None and block.able_to_move(self):
            block_move.play()
            self.map.move += 1
            self.print_game_status(screen)
            block.move(screen, self)
        if self.is_win():
            if self.level == 7:
                self.end(screen)
            else:
                screen.blit(self.map.win_images[0], (0, 0))
                pygame.display.flip()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/level pass.mp3')
                pygame.mixer.music.play()
                if self.level == self.active_level:
                    self.active_level += 1

    def is_win(self):
        for blocks in self.map.blocks:
            for block in blocks:
                if block is not None:
                    if (block.x != block.correct_pos["x"] or block.y != block.correct_pos["y"]):
                        return False
        return True

    def end(self, screen):
        print("Victory")
        pygame.mixer.music.load('Sound/cheer.mp3')
        pygame.mixer.music.play()
        screen.blit(self.map.win_images[0], (0, 0))
        pygame.display.flip()
        sleep(3)

        pygame.mixer.music.load('Sound/Special/Heaven.mp3')
        pygame.mixer.music.play()
        for final_item in final:
            screen.blit(final_item, (0, 0))
            pygame.display.flip()
            sleep(2)

        sleep(3)

        pygame.mixer.music.load('Sound/Special/John Cena.mp3')
        pygame.mixer.music.play()
        sleep(2)
        for i in range(50):
            screen.blit(troll[i % 2], (0, 0))
            pygame.display.flip()
            sleep(0.2)

        screen.blit(end_game, (0, 0))
        pygame.display.flip()
        self.victory = True
