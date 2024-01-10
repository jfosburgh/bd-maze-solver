from maze import Maze
from graphics import Window
import sys
from math import floor

sys.setrecursionlimit(10000)

def main(rows, columns):
    width = 2100
    row_size = floor(width/(rows+1))
    offset = (width-row_size*rows)
    column_size = row_size
    window = Window(width, columns*column_size+offset)
    maze = Maze(window, x0=offset/2, y0=offset/2, rows=rows, row_size=row_size, columns=columns, column_size=column_size)
    maze.solve()

    input()


if __name__ == '__main__':
    if len(sys.argv)-1 != 2:
        print('Usage: python main.py <num_columns> <num_rows>')
        sys.exit()
    rows = int(sys.argv[1])
    columns = int(sys.argv[2])
    main(rows, columns)
    
