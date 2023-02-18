import unittest
import collections

class Matrix01(unittest.TestCase):
    """
    Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

    The distance between two adjacent cells is 1.

    Instead of invoking BFS for each land cell to see how far we can get away from that source, we flip the problem.
    The flipped problem is to start from target (sea) and to figure our the closest source (land)
    This allows us to run a single BFS search that emerges from different places (all the targets aka all the zero cells) in the grid
    Add all the targets (all zero cells) into the queue. While you're at it, also mark those targets as visited (add to a visited set)
    Run a single BFS on the pre-processed queue and investigate neighbors.
    if neighbor cell has not been visited --> then it must bea land cell (since all the sea cells have been marked visited):
    append the neighbour cell into the queue and mutate the gird
    """

    def matrix_01(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        q = collections.deque()
        visited = set()
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        while q:
            row, col = q.popleft()
            for new_row, new_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                    matrix[new_row][new_col] = matrix[row][col] + 1
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))
        return matrix

    def test_matrix(self):
        self.assertEqual(self.matrix_01([[0,0,0],[0,1,0],[1,1,1]]), [[0,0,0],[0,1,0],[1,2,1]])







