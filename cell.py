from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        line = Line(Point(x1, y1), Point(x1, y2))
        fill = "black" if self.has_left_wall else "white"
        self._win.draw_line(line, fill)

        line = Line(Point(x1, y1), Point(x2, y1))
        fill = "black" if self.has_top_wall else "white"
        self._win.draw_line(line, fill)

        line = Line(Point(x2, y1), Point(x2, y2))
        fill = "black" if self.has_right_wall else "white"
        self._win.draw_line(line, fill)

        line = Line(Point(x1, y2), Point(x2, y2))
        fill = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(line, fill)

    def draw_move(self, to_cell, undo=False):
        fill_color = "gray" if undo else "red"

        point_a = self.get_center_point()
        point_b = to_cell.get_center_point()

        line_ab = Line(point_a, point_b)
        self._win.draw_line(line_ab, fill_color)

    def get_center_point(self):
        if self._x1 is None or self._x2 is None or self._y1 is None or self._y2 is None:
            return

        x = abs(self._x1 + self._x2) // 2
        y = abs(self._y1 + self._y2) // 2
        return Point(x, y)
