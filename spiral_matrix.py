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
        rows, cols = len(matrix), len(matrix[0])
        row, col, row_dir, col_dir, ans = 0, 0, 0, 1, []
        VISITED = '*'

        for _ in range(rows*cols):
            ans.append(matrix[row][col])
            matrix[row][col] = VISITED

            new_row, new_col = row + row_dir, col + col_dir
            if (not 0 <= new_row < rows or not 0 <= new_col < cols or matrix[new_row][new_col] == VISITED):
                row_dir, col_dir = col_dir, -row_dir

            row, col = row + row_dir, col + col_dir
        return ans


    def test_spiral(self):
        input = [[1,2,3],[4,5,6],[7,8,9]]
        output = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(self.spiral_order(input), output)

