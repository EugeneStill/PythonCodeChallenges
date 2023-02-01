import unittest


class TwoSum(unittest.TestCase):
    """
    return index of first two elements that sum to target
    """
    def two_sum_dic(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            else:
                seen[n] = i

    def two_sum_two_pointers(self, nums, target):
        r, l = 0, len(nums) -1
        while r < l:
            if nums[r] + nums[l] == target:
                return [r, l]
            r += 1
            l -= 1
        return [-1, -1]

    def test_two_sum_dic(self):
        nums = [3, 2, 4, 5, 10, 11, 12]
        bad_nums = [1, 4, 6, 7, 9, 19]
        self.assertEqual(self.two_sum_dic(nums, 15), [3, 4])
        self.assertEqual(self.two_sum_two_pointers(nums, 15), [0, 6])
        self.assertEqual(self.two_sum_two_pointers(bad_nums, 150), [-1, -1])



