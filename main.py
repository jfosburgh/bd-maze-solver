from maze import Maze
from graphics import Window


def main():
    rows, columns = 16, 12
    row_size, column_size = 50, 50
    window = Window(rows*row_size+50, columns*column_size+50)
    maze = Maze(window, x0=25, y0=25)

    input()


if __name__ == '__main__':
    main()
    
