import time
import random
from graphics import Cell, Window, Point

LEFT = (-1, 0)
DOWN = (0, 1)
RIGHT = (1, 0)
UP = (0, -1)


class Maze:
    def __init__(self, window: Window = None, rows: int = 16, columns: int = 12, row_size: int = 50, column_size: int = 50, x0: int = 0, y0: int = 0):
        self.__rows = rows
        self.__columns = columns
        self.__cells = []
        self.__window = window
        self.__populate(rows, columns, row_size, column_size, x0, y0)
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_visited()

    def __populate(self, rows, columns, row_size, column_size, x0, y0):
        for i in range(1,rows+1):
            column_cells = []
            for j in range(1,columns+1):
                temp_cell = Cell(Point(x0+(i-1)*row_size, y0+(j-1)*column_size), Point(x0+i*row_size, y0+j*column_size), self.__window)
                column_cells.append(temp_cell)
            self.__cells.append(column_cells)

        self.__draw_cells()

    def __draw_cells(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__window:
            self.__cells[i][j].draw()
            self.__animate()

    def __animate(self):
        self.__window.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].top_wall = False
        self.__draw_cell(0,0)
        self.__cells[-1][-1].bottom_wall = False
        self.__draw_cell(-1,-1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].__visited = True
        while True:
            to_visit = []
            if j-1 >= 0 and not self.__cells[i][j-1].get_visited():
                to_visit.append((i, j-1)) # Up
            if i-1 >= 0 and not self.__cells[i-1][j].get_visited():
                to_visit.append((i-1, j)) # Left
            if j + 1 < self.__columns and not self.__cells[i][j+1].get_visited():
                to_visit.append((i, j+1)) # Down
            if i + 1 < self.__rows and not self.__cells[i+1][j].get_visited():
                to_visit.append((i+1, j)) # Right
            if not to_visit:
                return
            next = random.choice(to_visit)
            self.__cells[next[0]][next[1]].set_visited()
            self.__break_wall(i, j, next[0], next[1])
            self.__break_walls_r(next[0], next[1])

    def __break_wall(self, i, j, x, y):
        if i < x: 
            self.__cells[i][j].right_wall = False
            self.__cells[x][y].left_wall = False
        if i > x:
            self.__cells[i][j].left_wall = False
            self.__cells[x][y].right_wall = False
        if j < y:
            self.__cells[i][j].bottom_wall = False
            self.__cells[x][y].top_wall = False
        if j > y:
            self.__cells[i][j].top_wall = False
            self.__cells[x][y].bottom_wall = False
        self.__draw_cell(i, j)
        self.__draw_cell(x, y)

    def __reset_visited(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__cells[i][j].set_visited(False)
    
    def get_cells(self):
        return self.__cells
