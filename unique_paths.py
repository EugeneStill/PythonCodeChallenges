import unittest
import math

class UniquePaths(unittest.TestCase):
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
    The robot can only move either down or right at any point in time.

    Given 2 integers m and n, return the number of unique paths that the robot can take to reach the bottom-right corner

    The test cases are generated so that the answer will be less than or equal to 2 * 109.
    """

    # 2. Math solution
    # Note, that we need to make overall n + m - 2 steps, and exactly m - 1 of them need to be right moves and n - 1 down steps. By definition this is numbef of combinations to choose n - 1 elements from n + m - 2.

    # Complexity: time complexity is O(m+n), space complexity is O(1).

    def unique_paths(self, rows, cols):
        dp = [1] * cols
        print("\n" + str(dp))
        for row in range(1, rows):
            print("CHECKING ROW {}".format(row))
            for col in range(1, cols):
                dp[col] = dp[col - 1] + dp[col]
                print(str(dp))
        return dp[-1] if rows and cols else 0

    # 2. Math solution
    # Note, that we need to make overall n + m - 2 steps, and exactly m - 1 of them need to be right moves
    # and n - 1 down steps. By definition this is number of combinations to choose n - 1 elements from n + m - 2.

    # Complexity: time complexity is O(m+n), space complexity is O(1).
    def unique_paths_math(self, m, n):
        print("FACT MN {}".format(math.factorial(m+n-2)))
        print("FACT M {}".format(math.factorial(m -1)))
        print("FACT N {}".format(math.factorial(n - 1)))
        return math.factorial(m+n-2)//math.factorial(m-1)//math.factorial(n-1)

    def test_unique_paths(self):
        print(self.unique_paths(3, 7))
        
# LOGGING
# [1, 1, 1, 1, 1, 1, 1] # INIT ARRAY FOR ROW 0 with 1's
# CHECKING ROW 1 # FROM HERE OUT, ADD COL[COL-1] TO COL TO UPDATE EACH COL VALUE
# [1, 2, 1, 1, 1, 1, 1]
# [1, 2, 3, 1, 1, 1, 1]
# [1, 2, 3, 4, 1, 1, 1]
# [1, 2, 3, 4, 5, 1, 1]
# [1, 2, 3, 4, 5, 6, 1]
# [1, 2, 3, 4, 5, 6, 7]
# CHECKING ROW 2
# [1, 3, 3, 4, 5, 6, 7]
# [1, 3, 6, 4, 5, 6, 7]
# [1, 3, 6, 10, 5, 6, 7]
# [1, 3, 6, 10, 15, 6, 7]
# [1, 3, 6, 10, 15, 21, 7]
# [1, 3, 6, 10, 15, 21, 28]