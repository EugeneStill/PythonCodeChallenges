import unittest

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
        q = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = -1
        print("\nMAT " + str(matrix))
        print("Q " + str(q))
        for x, y in q:
            print("checking x, y: {} {}".format(x, y))
            for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == -1:
                    matrix[r][c] = matrix[x][y] + 1
                    q.append((r, c))
                    print("added r, c {} {}".format(r, c))
        return matrix

    def test_matrix(self):
        self.assertEqual(self.matrix_01([[0,0,0],[0,1,0],[1,1,1]]), [[0,0,0],[0,1,0],[1,2,1]])







