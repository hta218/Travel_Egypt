import pygame
from time import sleep
import os
from game import Game
from map import Map

################################################# init pyGame
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20, 40)
pygame.init()
screen = pygame.display.set_mode((1050, 700))
pygame.display.set_caption("Travel Egypt")
pygame.mixer.music.load("Sound/Background/egypt.mp3")
pygame.mixer.music.play(-1)

playing = True
#################################################

map = Map(4, 4, 0)
game = Game(map)
game.start(screen)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.victory is True:
                game.quit()
            elif game.welcome is True:
                game.let_go(event, screen)
            elif game.selected_mode is False:
                game.select_mode(event, screen)
            else:
                if game.preload is not True:
                    game.pre_load(screen)
                elif game.is_win():
                    if game.selected_level(event, screen) is True:
                        NEXT = 1
                        sleep(1)
                        game.get_to_level(screen, NEXT)
                else:
                    game.loop(screen, event)

    pygame.display.flip()


