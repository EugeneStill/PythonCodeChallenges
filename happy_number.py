import unittest

class HappyNumber(unittest.TestCase):
    """
    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat process until number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    """
    def is_happy(self, n):
        """
        :param n: int
        :return: bool
        """
        seen = {}
        while n not in seen:
            seen[n] = 1
            n = sum([int(d) ** 2 for d in str(n)])
        return n == 1

    def test_is_happy(self):
        self.assertTrue(self.is_happy(19))
        self.assertFalse(self.is_happy(17))



