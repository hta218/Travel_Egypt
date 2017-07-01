import pygame
from character import Character
from copy import copy

block_00 = Character(0, 0, pygame.image.load('Map/Level 4/00.jpg'), {"x" : 0, "y" : 0})
block_01 = Character(1, 0, pygame.image.load('Map/Level 4/01.jpg'), {"x" : 1, "y" : 0})
block_02 = Character(2, 0, pygame.image.load('Map/Level 4/02.jpg'), {"x" : 2, "y" : 0})
block_03 = Character(3, 0, pygame.image.load('Map/Level 4/03.jpg'), {"x" : 3, "y" : 0})

block_10 = Character(0, 1, pygame.image.load('Map/Level 4/10.jpg'), {"x" : 0, "y" : 1})
block_11 = Character(1, 1, pygame.image.load('Map/Level 4/11.jpg'), {"x" : 1, "y" : 1})
block_12 = Character(2, 1, pygame.image.load('Map/Level 4/12.jpg'), {"x" : 2, "y" : 1})
block_13 = Character(3, 1, pygame.image.load('Map/Level 4/13.jpg'), {"x" : 3, "y" : 1})

block_20 = Character(0, 2, pygame.image.load('Map/Level 4/20.jpg'), {"x" : 0, "y" : 2})
block_21 = Character(1, 2, pygame.image.load('Map/Level 4/21.jpg'), {"x" : 1, "y" : 2})
block_22 = Character(2, 2, pygame.image.load('Map/Level 4/22.jpg'), {"x" : 2, "y" : 2})
block_23 = Character(3, 2, pygame.image.load('Map/Level 4/23.jpg'), {"x" : 3, "y" : 2})

block_31 = Character(1, 3, pygame.image.load('Map/Level 4/31.jpg'), {"x" : 1, "y" : 3})
block_32 = Character(2, 3, pygame.image.load('Map/Level 4/32.jpg'), {"x" : 2, "y" : 3})
block_33 = Character(3, 3, pygame.image.load('Map/Level 4/33.jpg'), {"x" : 3, "y" : 3})

level_4 = [
                [block_00, block_01, block_02, block_03],
                [block_10, block_11, block_12, block_13],
                [block_20, block_21, block_22, block_23],
                [None, block_31, block_32, block_33]
            ]

win = pygame.image.load('Map/Level 4/win.jpg')
win_click = pygame.image.load('Map/Level 4/win_click.jpg')
hint = pygame.image.load('Map/Level 4/hint.jpg')

sound_path = 'Sound/Level/Level 4.mp3'

class Level_4:
    def __init__(self):
        self.blocks = self.create_new_blocks()
        self.win_images = [win, win_click, hint]
        self.sound_path = sound_path
        self.item_x = 135
        self.item_y = 547
        self.item_width = 135
        self.item_height = 144

    def create_new_blocks(self):
        blocks = []
        for y in range(4):
            blocks.append([])
            for x in range(4):
                if level_4[y][x] is not None:
                    blocks[y].append(copy(level_4[y][x]))
                    print(blocks[y][x].x, blocks[y][x].y)
                else:
                    blocks[y].append(None)
        return blocks