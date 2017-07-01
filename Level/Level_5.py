import pygame
from character import Character
from copy import copy

block_00 = Character(0, 0, pygame.image.load('Map/Level 5/00.jpg'), {"x" : 0, "y" : 0})
block_01 = Character(1, 0, pygame.image.load('Map/Level 5/01.jpg'), {"x" : 1, "y" : 0})
block_02 = Character(2, 0, pygame.image.load('Map/Level 5/02.jpg'), {"x" : 2, "y" : 0})
block_03 = Character(3, 0, pygame.image.load('Map/Level 5/03.jpg'), {"x" : 3, "y" : 0})
block_04 = Character(4, 0, pygame.image.load('Map/Level 5/04.jpg'), {"x" : 4, "y" : 0})

block_10 = Character(0, 1, pygame.image.load('Map/Level 5/10.jpg'), {"x" : 0, "y" : 1})
block_11 = Character(1, 1, pygame.image.load('Map/Level 5/11.jpg'), {"x" : 1, "y" : 1})
block_12 = Character(2, 1, pygame.image.load('Map/Level 5/12.jpg'), {"x" : 2, "y" : 1})
block_13 = Character(3, 1, pygame.image.load('Map/Level 5/13.jpg'), {"x" : 3, "y" : 1})
block_14 = Character(4, 1, pygame.image.load('Map/Level 5/14.jpg'), {"x" : 4, "y" : 1})

block_20 = Character(0, 2, pygame.image.load('Map/Level 5/20.jpg'), {"x" : 0, "y" : 2})
block_21 = Character(1, 2, pygame.image.load('Map/Level 5/21.jpg'), {"x" : 1, "y" : 2})
block_22 = Character(2, 2, pygame.image.load('Map/Level 5/22.jpg'), {"x" : 2, "y" : 2})
block_23 = Character(3, 2, pygame.image.load('Map/Level 5/23.jpg'), {"x" : 3, "y" : 2})
block_24 = Character(4, 2, pygame.image.load('Map/Level 5/24.jpg'), {"x" : 4, "y" : 2})

block_30 = Character(0, 3, pygame.image.load('Map/Level 5/30.jpg'), {"x" : 0, "y" : 3})
block_31 = Character(1, 3, pygame.image.load('Map/Level 5/31.jpg'), {"x" : 1, "y" : 3})
block_32 = Character(2, 3, pygame.image.load('Map/Level 5/32.jpg'), {"x" : 2, "y" : 3})
block_33 = Character(3, 3, pygame.image.load('Map/Level 5/33.jpg'), {"x" : 3, "y" : 3})
block_34 = Character(4, 3, pygame.image.load('Map/Level 5/34.jpg'), {"x" : 4, "y" : 3})

block_41 = Character(1, 4, pygame.image.load('Map/Level 5/41.jpg'), {"x" : 1, "y" : 4})
block_42 = Character(2, 4, pygame.image.load('Map/Level 5/42.jpg'), {"x" : 2, "y" : 4})
block_43 = Character(3, 4, pygame.image.load('Map/Level 5/43.jpg'), {"x" : 3, "y" : 4})
block_44 = Character(4, 4, pygame.image.load('Map/Level 5/44.jpg'), {"x" : 4, "y" : 4})

level_5 = [
                [block_00, block_01, block_02, block_03, block_04],
                [block_10, block_11, block_12, block_13, block_14],
                [block_20, block_21, block_22, block_23, block_24],
                [block_30, block_31, block_32, block_33, block_34],
                [None, block_41, block_42, block_43, block_44]
            ]

win = pygame.image.load('Map/Level 5/win.jpg')
win_click = pygame.image.load('Map/Level 5/win_click.jpg')
hint = pygame.image.load('Map/Level 5/hint.jpg')

sound_path = 'Sound/Level/Level 5.mp3'

class Level_5:
    def __init__(self):
        self.blocks = self.create_new_blocks()
        self.win_images = [win, win_click, hint]
        self.sound_path = sound_path
        self.item_x = 340
        self.item_y = 538
        self.item_width = 225
        self.item_height = 118

    def create_new_blocks(self):
        blocks = []
        for y in range(5):
            blocks.append([])
            for x in range(5):
                if level_5[y][x] is not None:
                    blocks[y].append(copy(level_5[y][x]))
                    print(blocks[y][x].x, blocks[y][x].y)
                else:
                    blocks[y].append(None)
        return blocks
