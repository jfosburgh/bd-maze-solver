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

    def test_maze_visits_and_resets(self):
        cols = 8
        rows = 10
        m1 = Maze(rows=rows, columns=cols)
        cells = m1.get_cells()
        for i in range(rows):
            for j in range(cols):
                self.assertFalse(cells[i][j].get_visited())

if __name__ == '__main__':
    unittest.main()
