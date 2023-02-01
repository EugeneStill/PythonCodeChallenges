import unittest


class SearchRange(unittest.TestCase):
    """
    Given an array of integers sorted in non-decreasing order, find the starting & ending position of a target value.

    If target is not found in the array, return [-1, -1].
    """
    def search_range(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target + 1) - 1

        if lo <= hi:
            return [lo, hi]

        return [-1, -1]

    def test_search_range(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        self.assertEqual(self.search_range(nums, target), [3, 4])
        nums = [5, 7, 7, 8, 9, 10]
        self.assertEqual(self.search_range(nums, target), [3, 3])
        nums = [5, 7, 7, 7, 9, 10]
        self.assertEqual(self.search_range(nums, target), [-1, -1])