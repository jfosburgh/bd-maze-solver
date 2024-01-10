from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack()


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title = 'Python Maze Solver'
        self.__canvas = Canvas(width=width, height=height, bg='white')
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def is_running(self):
        return self.__running


class Cell:
    def __init__(self, p1: Point, p3: Point, window: Window = None, color: str = 'black'):
        self.__p1 = p1
        self.__p2 = Point(p1.x, p3.y)
        self.__p3 = p3
        self.__p4 = Point(p3.x, p1.y)
        self.__window = window
        self.__color = color
        self.left_wall, self.right_wall, self.top_wall, self.bottom_wall = True, True, True, True

    def draw(self):
        self.__window.draw_line(Line(self.__p1, self.__p2), self.__color if self.left_wall else 'white')
        self.__window.draw_line(Line(self.__p2, self.__p3), self.__color if self.bottom_wall else 'white')
        self.__window.draw_line(Line(self.__p3, self.__p4), self.__color if self.right_wall else 'white')
        self.__window.draw_line(Line(self.__p4, self.__p1), self.__color if self.top_wall else 'white')


    def get_center(self):
        x = (self.__p4.x - self.__p1.x) / 2 + self.__p1.x
        y = (self.__p2.y - self.__p1.y) / 2 + self.__p1.y
        return Point(int(x), int(y))

    def draw_move(self, to, undo=False):
        color = 'gray' if undo else 'red'
        self.__window.draw_line(Line(self.get_center(), to.get_center()), color)

