import unittest

# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# Assume all four edges of the grid are surrounded by water.

class NumbefOfIslands(unittest.TestCase):
    def num_islands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # since recursion is changing adjacent '1' values to '#' we only find a new '1' if a new island starts
                if grid[i][j] == '1':
                    print("making new call for dfs, for row: {} col: {}".format(i, j))
                    self.dfs(grid, i, j)
                    print("count is updated")
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            print("returning")
            return
        grid[i][j] = '#'
        print("\nCHECKED Row {}, Col {}".format(i, j))
        print(str(grid))
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

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
