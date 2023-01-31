import unittest

class MySqRt(unittest.TestCase):

    def my_sq_rt(self, x):
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x < (mid + 1)  * (mid + 1):
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1

    def test_my_sq_rt(self):
        self.assertEqual(self.my_sq_rt(15), 3)
        self.assertEqual(self.my_sq_rt(16), 4)
        self.assertEqual(self.my_sq_rt(17), 4)
        self.assertEqual(self.my_sq_rt(25), 5)
        self.assertEqual(self.my_sq_rt(26), 5)

