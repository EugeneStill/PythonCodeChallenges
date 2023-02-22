import unittest

# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# Assume all four edges of the grid are surrounded by water.

class NumbefOfIslands(unittest.TestCase):

    def num_islands(self, grid):
        if not grid:
            return 0
        VISITED, LAND, ROWS, COLS, islands = '#', '1', len(grid), len(grid[0]), 0

        def dfs(row, col):
            if not 0 <= row < ROWS or not 0 <= col < COLS or grid[row][col] != LAND:
                return
            grid[row][col] = VISITED
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == LAND:
                    dfs(row, col)
                    islands += 1

        return islands

    def test_num_islands(self):
        grid_1 = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        grid_2 = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        # self.assertEqual(self.num_islands(grid_1), 1)
        self.assertEqual(self.num_islands(grid_2), 3)
