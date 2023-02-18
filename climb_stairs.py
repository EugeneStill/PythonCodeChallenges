import unittest


class ClimbStairs(unittest.TestCase):
    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # memoization
        # memo = {}
        # memo[1] = 1
        # memo[2] = 2
        #
        # def climb(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = climb(n - 1) + climb(n - 2)
        #         return memo[n]
        #
        # return climb(n)


        a, b = 1, 1
        print("\n")
        for i in range(n):
            a, b = b, a + b
            print("A {} B {}".format(a, b))
        return a

    def test_stairs(self):
        self.assertEqual(self.climb_stairs(10), 89)

# LOGGING
# A 1 B 2
# A 2 B 3
# A 3 B 5
# A 5 B 8
# A 8 B 13
# A 13 B 21
# A 21 B 34
# A 34 B 55
# A 55 B 89
# A 89 B 144