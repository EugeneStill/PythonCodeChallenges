import unittest


class MaxSubArray(unittest.TestCase):
    """
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
    """
    def max_sub_array(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

    def test_msa(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(self.max_sub_array(nums), 6)