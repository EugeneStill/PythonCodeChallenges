import unittest


class FindDuplicate(unittest.TestCase):
    """
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.
    """
    def find_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use the numbers from 1 to len(nums) -1 as values for binary search, not the input array
        l, r = 1, len(nums) - 1

        while l + 1 <= r:
            mid, count = (l + r) // 2, 0
            # go through each num in input. each time num <= than mid, increase count
            for num in nums:
                if num <= mid:
                    count += 1
                    # use count to determine if we should look left or right in range of numbers
            if count <= mid:
                l = mid + 1
            else:
                r = mid
        return r
    def test_dupe(self):
        self.assertEqual(self.find_duplicate([1,3,4,2,2]), 2)
