import unittest


class PowerOfThree(unittest.TestCase):
    """
    is the number a power of 3?
    """
    def is_pow_three(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while(n % 3 == 0):
            n /= 3
        return n == 1

    def test_pow_three(self):
        self.assertTrue(self.is_pow_three(27))
        self.assertFalse(self.is_pow_three(28))
        self.assertTrue(self.is_pow_three(-27))
        self.assertFalse(self.is_pow_three(-28))
        self.assertFalse(self.is_pow_three(0))