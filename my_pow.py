import unittest


class MyPow(unittest.TestCase):
    def my_pow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # Deal with negative exponents (returns fractions)
        if n < 0:
            x = 1 / x
            n = abs(n)

        # Iterate:
        res = 1
        while n:
            print("\nSTART: N: {} RES: {} X: {}".format(n, res, x))
            if n % 2:
                res = res * x
            x = x * x
            n = n // 2
            print("\nEND: N: {} RES: {} X: {}".format(n, res, x))

        return res

    def test_my_pow(self):
        self.my_pow(2, 10)