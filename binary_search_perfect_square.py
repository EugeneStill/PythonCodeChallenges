import unittest


class IsPerfectSquare(unittest.TestCase):
    def is_perfect_square(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l <= r:
            mid = (l + r) //2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid -1
        return False

    def test_perfect_square(self):
        self.assertFalse(self.is_perfect_square(15))
        self.assertTrue(self.is_perfect_square(16))
        self.assertFalse(self.is_perfect_square(24))
        self.assertTrue(self.is_perfect_square(25))