import unittest


class IncreasingTriplet(unittest.TestCase):
    """
    Given an integer array nums, return true if there exists a triple of indices (i, j, k)
    such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
    """
    def increasing_triplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

    def test_increasing_triplets(self):
        nums1 = [1,2,3,4,5]
        nums2 = reversed(nums1)
        self.assertTrue(self.increasing_triplet(nums1))
        self.assertFalse(self.increasing_triplet(nums2))