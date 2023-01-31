import unittest

class FindPeakElement(unittest.TestCase):
    """
    A peak element is an element that is strictly greater than its neighbors.

    Given a 0-indexed integer array nums, find a peak element, and return its index.
    If the array contains multiple peaks, return the index to any of the peaks.

    You may imagine that nums[-1] = nums[n] = -∞.
    In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

    You must write an algorithm that runs in O(log n) time.
    """
    def find_peak_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1

        return left

    def test_peak_element(self):
        self.assertIn(self.find_peak_element([1,2,1,3,5,6,4]), [1,5])
