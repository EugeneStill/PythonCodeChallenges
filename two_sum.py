import unittest


class TwoSum(unittest.TestCase):
    """
    return index of first two elements that sum to target
    """
    def two_sum_dic(self, nums: list, target: int) -> dict:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            else:
                seen[n] = i


    def test_two_sum_dic(self):
        nums = [3, 2, 4, 5, 10, 6, 9]
        self.assertEqual(self.two_sum_dic(nums, 15), [3, 4])



