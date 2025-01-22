from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    point_A = Point(100, 100)
    point_B = Point(150, 150)
    point_C = Point(50, 150)
    line_ab = Line(point_A, point_B)
    line_ac = Line(point_A, point_C)
    line_bc = Line(point_B, point_C)
    line_color = "black"
    win.draw_line(line_ab, line_color)
    win.draw_line(line_ac, line_color)
    win.draw_line(line_bc, line_color)
    win.wait_for_close()


main()
