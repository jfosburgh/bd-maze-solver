import time
from graphics import Point, Window, Cell


class Maze:
    def __init__(self, window: Window = None, rows: int = 16, columns: int = 12, row_size: int = 50, column_size: int = 50, x0: int = 0, y0: int = 0):
        self.__rows = rows
        self.__columns = columns
        self.__cells = []
        self.__window = window
        self.__populate(rows, columns, row_size, column_size, x0, y0)
        self.__break_entrance_and_exit()

    def __populate(self, rows, columns, row_size, column_size, x0, y0):
        for i in range(1,rows+1):
            column_cells = []
            for j in range(1,columns+1):
                temp_cell = Cell(Point(x0+(i-1)*row_size, y0+(j-1)*column_size), Point(x0+i*row_size, y0+j*column_size), self.__window)
                column_cells.append(temp_cell)
            self.__cells.append(column_cells)

        if self.__window:
            self.__draw_cells()

    def __draw_cells(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
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

    def get_cells(self):
        return self.__cells
