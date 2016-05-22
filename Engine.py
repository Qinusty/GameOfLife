import copy

import pygame
from Board import Board

pygame.init()           ## Init block
display_width = 800
display_height = 800

BLACK = (0,  0,  0)
WHITE = (255,255,255)
RED   = (255,0,  0)
BLUE  = (0,  0,  255)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Conways game of life!")
clock = pygame.time.Clock()

grid_size = (40,40)
board = Board(grid_size)

cycles_per_second = 300
setup = True
saved_board = board
crashed = False
first = True
game_rect = (0, 0, display_width, display_height)
while not crashed:
    ## event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN: # KEYPRESSES
            if event.key == pygame.K_SPACE:
                setup = not setup
            elif event.key == pygame.K_c:
                board = Board(grid_size)
                print("Board Cleared!")
            elif event.key == pygame.K_s:
                saved_board = copy.deepcopy(board)
                print("Grid Saved!")
            elif event.key == pygame.K_l:
                board = copy.deepcopy(saved_board)
                print("Grid Loaded!")

    ## logic
    if setup:
        pygame.display.set_caption("Conways game of life! - PAUSED")
        cycles_per_second = 300
        if pygame.mouse.get_pressed()[0]:
            board.modifyAtScreenPos(game_rect, pygame.mouse.get_pos(), True)
        elif pygame.mouse.get_pressed()[2]:
            board.modifyAtScreenPos(game_rect, pygame.mouse.get_pos(), False)

    if not setup:
        pygame.display.set_caption("Conways game of life!")
        cycles_per_second = 20
        board.do_stuff()

    ## draw
    game_display.fill(WHITE)
    board.draw(game_rect, game_display)


    pygame.display.flip()  ## redraw screen
    clock.tick(cycles_per_second)  ## 1 cycle per second

pygame.quit()

quit()