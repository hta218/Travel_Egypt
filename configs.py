import pygame

pygame.init()
welcome = pygame.image.load('Map/Background/welcome.jpg')

font = pygame.font.SysFont("Arial", 20, True, False)

bg = pygame.image.load('Map/Background/background.jpg')
game_status = pygame.image.load('Map/game_status.png')

mode = pygame.image.load('Map/Game mode/Game mode.jpg')
easy = pygame.image.load('Map/Game mode/Easy.png')
easy_click = pygame.image.load('Map/Game mode/Easy_click.png')

medium = pygame.image.load('Map/Game mode/Medium.png')
medium_click = pygame.image.load('Map/Game mode/Medium_click.png')

hard = pygame.image.load('Map/Game mode/Hard.png')
hard_click = pygame.image.load('Map/Game mode/Hard_click.png')

next = pygame.image.load('Map/Button/Next.png')
next_click = pygame.image.load('Map/Button/Next_click.png')

back = pygame.image.load('Map/Button/Back.png')
back_click = pygame.image.load('Map/Button/Back_click.png')

quit = pygame.image.load('Map/Button/Quit.png')
quit_click = pygame.image.load('Map/Button/Quit_click.png')

letsgo = pygame.image.load('Map/Button/letsgo.png')
letsgo_click = pygame.image.load('Map/Button/letsgo_click.png')

block_44 = pygame.image.load('Map/block 4x4.png')
block_55 = pygame.image.load('Map/block 5x5.png')

#### victory
final_01 = pygame.image.load('Map/Victory/final 01.jpg')
final_02 = pygame.image.load('Map/Victory/final 02.jpg')
final_03 = pygame.image.load('Map/Victory/final 03.jpg')
final_04 = pygame.image.load('Map/Victory/final 04.jpg')
final_05 = pygame.image.load('Map/Victory/final 05.jpg')
final_06 = pygame.image.load('Map/Victory/final 06.jpg')
final_07 = pygame.image.load('Map/Victory/final 07.jpg')
final_08 = pygame.image.load('Map/Victory/final 08.jpg')

troll_01 = pygame.image.load('Map/Victory/Troll 01.jpg')
troll_02 = pygame.image.load('Map/Victory/Troll 02.jpg')

end_game = pygame.image.load('Map/Victory/End.jpg')

final = [final_01, final_02, final_03, final_04, final_05, final_06, final_07, final_08]

troll = [troll_01, troll_02]