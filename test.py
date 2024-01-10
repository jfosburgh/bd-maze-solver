import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        cols = 8
        rows = 10
        m1 = Maze(rows=rows, columns=cols)
        self.assertEqual(
            len(m1.get_cells()),
            rows
        )
        self.assertEqual(
            len(m1.get_cells()[0]),
            cols
        )


if __name__ == '__main__':
    unittest.main()
