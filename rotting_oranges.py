import unittest
from collections import deque


class OrangesRotting(unittest.TestCase):
    """
    You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

    Return minimum number of minutes that must pass until no cell has a fresh orange. If this is impossible, return -1.

    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: Bottom left corner (row 2, column 0) is never rotten, bc rotting only happens 4-directionally.
    """
    def oranges_rotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # Time complexity: O(rows * cols) -> each cell is visited at least once
        # Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue

        rows = len(grid)
        if rows == 0:  # check if grid is empty
            return -1

        EMPTY, FRESH, ROTTEN = 0, 1, 2
        cols, fresh_cnt, minutes_passed, rotten = len(grid[0]), 0, 0, deque()

        # visit each cell in the grid & update fresh count & rotten queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ROTTEN:
                    rotten.append((r, c))
                elif grid[r][c] == FRESH:
                    fresh_cnt += 1

        # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
        while rotten and fresh_cnt > 0:

            # update the number of minutes for each level pass
            minutes_passed += 1

            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                row, col = rotten.popleft()

                # visit all the valid adjacent cells
                for new_row, new_col in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
                    if not 0 <= new_row < rows or not 0 <= new_col < cols or grid[new_row][new_col] != FRESH:
                        continue

                    # update the fresh count, mark cell rotten and add to queue
                    fresh_cnt -= 1
                    grid[new_row][new_col] = ROTTEN
                    rotten.append((new_row, new_col))

        return minutes_passed if fresh_cnt == 0 else -1

    def test_ro(self):
        grid1 = [[2,1,1],[1,1,0],[0,1,1]]
        grid2 = [[2,1,1],[0,1,1],[1,0,1]]
        self.assertEqual(self.oranges_rotting(grid1), 4)
        self.assertEqual(self.oranges_rotting(grid2), -1)