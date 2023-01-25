import unittest


class NumberOfSquares(unittest.TestCase):
    """
    Given an integer n, return the least number of perfect square numbers that sum to n.

    A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
    For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
    """

    def num_squares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        squares = []
        i = 1
        while i * i <= n:
            squares.append( i * i )
            i += 1

        count = 0
        layer_values = {n}
        # perform a BFS, getting new values to check at each layer by subtracting square values from values of upper layer
        while layer_values:
            count += 1
            temp = set()
            for val in layer_values:
                for square in squares:
                    if val == square:
                        return count
                    if val < square:
                        break
                    temp.add(val-square)
            layer_values = temp

        return count

    def test_open_lock(self):
        self.assertEqual(self.num_squares(12), 3)
        self.assertEqual(self.num_squares(3), 3)
        self.assertEqual(self.num_squares(5), 2)



# LOGGING
# updated count 1
# X: 12 COUNT 1
# CHECKING Y 1
# ADDING 11 TO TEMP
# CHECKING Y 4
# ADDING 8 TO TEMP
# CHECKING Y 9
# ADDING 3 TO TEMP
# TC {8, 3, 11}
# updated count 2
# X: 8 COUNT 2
# CHECKING Y 1
# ADDING 7 TO TEMP
# CHECKING Y 4
# ADDING 4 TO TEMP
# CHECKING Y 9
# X: 3 COUNT 2
# CHECKING Y 1
# ADDING 2 TO TEMP
# CHECKING Y 4
# X: 11 COUNT 2
# CHECKING Y 1
# ADDING 10 TO TEMP
# CHECKING Y 4
# ADDING 7 TO TEMP
# CHECKING Y 9
# ADDING 2 TO TEMP
# TC {2, 10, 4, 7}
# updated count 3
# X: 2 COUNT 3
# CHECKING Y 1
# ADDING 1 TO TEMP
# CHECKING Y 4
# X: 10 COUNT 3
# CHECKING Y 1
# ADDING 9 TO TEMP
# CHECKING Y 4
# ADDING 6 TO TEMP
# CHECKING Y 9
# ADDING 1 TO TEMP
# X: 4 COUNT 3
# CHECKING Y 1
# ADDING 3 TO TEMP
# CHECKING Y 4
# PASSED