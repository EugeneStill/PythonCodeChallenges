import unittest


class PascalsTriangle(unittest.TestCase):
    """
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it.
    """
    def build_triangle(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pt = [[1]*(i+1) for i in range(numRows)]

        for row in range(2, numRows):
            for col in range(1, row):
                pt[row][col] = pt[row-1][col-1] + pt[row-1][col]
        return pt

    def test_pascals_triangle(self):
        five_rows = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertTrue(self.build_triangle(5), five_rows)