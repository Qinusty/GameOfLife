import pygame
import copy


class Board(object):

    def __init__(self, size):
        super().__init__()
        self.size = size
        self.state = State(size)
        ## test settings
        self.state.grid[int(size[0] / 2) - 1][int(size[1] / 2)] = True
        self.state.grid[int(size[0] / 2)][int(size[1] / 2)] = True
        self.state.grid[int(size[0] / 2) + 1][int(size[1] / 2)] = True

    def do_stuff(self):
        neighbours = []
        for x in range(self.size[0]):
            col = []
            for y in range(self.size[1]):
                col.append(self.state.neighbours((x,y)))
            neighbours.append(col)

        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.state.grid[x][y]: ## if this pos alive
                    if neighbours[x][y] >= 4 or neighbours[x][y] <= 1:
                        self.state.grid[x][y] = False
                elif neighbours[x][y] == 3:
                    self.state.grid[x][y] = True

    def draw(self, rect, display):
        left,top,w,h = rect
        box_w = int(w / self.size[0])
        box_h = int(h / self.size[1])
        for x in range(0,self.size[0]):
            for y in range(0,self.size[1]):
                colour = (230,230,230)
                if self.state.grid[x][y]:
                    colour = (40,230,40)
                draw_rect = (left + (box_w * x),
                             top + (box_h * y),
                             box_w, box_h)
                pygame.draw.rect(display, colour, draw_rect, 0)


class State(object):

    def __init__(self, size, initial_grid = []):
        super().__init__()
        self.grid = initial_grid.copy()
        if self.grid == []:
            self.grid = [[False for y in range(size[1])] for x in range(size[0])]

    def neighbours(self, xy):
        num_neighbours = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if not (x == 0 and y == 0):
                    check_x = xy[0] + x
                    check_y = xy[1] + y
                    if check_x in range(len(self.grid)):
                        if check_y in range(len(self.grid[check_x])):
                            if self.grid[check_x][check_y]:
                                num_neighbours += 1
        return num_neighbours
        

