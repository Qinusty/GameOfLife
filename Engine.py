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

board = Board((8,8))

cycles_per_second = 5
setup = True
last_mouse_state = pygame.MOUSEBUTTONDOWN
crashed = False
first = True
while not crashed:
    ## event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        # if setup:
        #     if event.type == pygame.MOUSEBUTTONDOWN and last_mouse_state == pygame.MOUSEBUTTONDOWN:
        #         last_mouse_state == event.type

    ## logic
    board.do_stuff()
    ## draw
    game_display.fill(WHITE)
    board.draw((0, 0, display_width, display_height), game_display)


    pygame.display.flip()  ## redraw screen
    clock.tick(cycles_per_second)  ## 1 cycle per second

pygame.quit()

quit()