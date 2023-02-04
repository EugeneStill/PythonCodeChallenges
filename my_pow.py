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

    def my_pow_recursive(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # Deal with negative power:
        if n < 0:
            x = 1 / x
            n = abs(n)

        def pow_recursive(x, n, res):
            if n == 0:
                return res
            if n % 2:
                res = res * x
            x = x * x
            n = n // 2
            return pow_recursive(x, n, res)

        return pow_recursive(x, n, 1)

    def test_my_pow(self):
        self.assertEqual(self.my_pow(2, 10), 1024)
        self.assertEqual(self.my_pow_recursive(2, 10), 1024)