import unittest


class GreatestCommonDivisor(unittest.TestCase):
    """
    Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

    The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

    https://en.wikipedia.org/wiki/Euclidean_algorithm
    """
    def greatest_common_divisor(self, nums):
        a, b = min(nums), max(nums)
        while a:
            a, b = b % a, a
        return b

    def greatest_common_divisor_recursive(self, nums):
        a, b = min(nums), max(nums)
        if a < 1:
            return 0

        def euc(a, b):
            if a == 0:
                return b
            a, b = b % a, a
            return a, b
        return euc(a, b)

    def test_gcd(self):
        nums = [2, 3, 5, 7, 10]
        self.assertEqual(self.greatest_common_divisor(nums), 2)
        self.assertEqual(self.greatest_common_divisor_recursive(nums)[1], 2)