import unittest


class SpiralOrder(unittest.TestCase):
    """
    Given an m x n matrix, return all elements of the matrix in spiral order.
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
    """
    def spiral_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(matrix[0]), len(matrix)
        row, col, d_row, d_col = 0, 0, 1, 0
        ans = []

        for _ in range(cols * rows):
            ans.append(matrix[col][row])
            matrix[col][row] = "*"

            # Check next cell to determine whether to keep going or rotate
            if (not 0 <= row + d_row < rows  # row out of bounds
                    or not 0 <= col + d_col < cols  # col out of bounds
                    or matrix[col + d_col][row + d_row] == "*"):  # next cell is already visited
                d_row, d_col = -d_col, d_row  # change direction

            row, col = row + d_row, col + d_col  # move to next cell

        return ans


    def test_spiral(self):
        input = [[1,2,3],[4,5,6],[7,8,9]]
        output = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(self.spiral_order(input), output)

