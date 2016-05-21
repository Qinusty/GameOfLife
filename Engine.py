import pygame

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

board = Board()

cycles_per_second = 10
setup = True
last_mouse_state = pygame.MOUSEBUTTONDOWN
crashed = False
while not crashed:
    ## event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if setup:
            if event.type == pygame.MOUSEBUTTONDOWN and last_mouse_state == pygame.MOUSEBUTTONDOWN:
                last_mouse_state == event.type
                

    pygame.display.flip()  ## redraw screen
    clock.tick(cycles_per_second)  ## 1 cycle per second

pygame.quit()

quit()