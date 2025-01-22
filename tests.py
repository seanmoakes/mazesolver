import unittest
from maze import Maze
from cell import Cell


class Tests(unittest.TestCase):
    def setUp(self):
        self.num_cols = 12
        self.num_rows = 10
        self.m1 = Maze(0, 0, self.num_rows, self.num_cols, 10, 10)

    def test_maze_create_cells(self):
        self.assertEqual(
            len(self.m1._cells),
            self.num_cols,
        )
        self.assertEqual(
            len(self.m1._cells[0]),
            self.num_rows,
        )

    def test_break_entrance(self):
        self.m1._break_entrance_and_exit()
        entrance_wall = self.m1._cells[0][0].has_top_wall
        self.assertFalse(entrance_wall)

    def test_break_exit(self):
        self.m1._break_entrance_and_exit()
        exit_wall = self.m1._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall
        self.assertFalse(exit_wall)


if __name__ == "__main__":
    unittest.main()
