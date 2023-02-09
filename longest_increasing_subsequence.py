import unittest


class LongestIncreasingSubsequence(unittest.TestCase):
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

    subsequences can be consecutive or not what matters is their order
    on the other hand sub-array must be consecutive.

    "LeetIsCode"
    sub-Sequence: "LeetCode"
    Sub-Array: "LeetIs" or "IsCode"
    """
    def length_of_lis(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            l, r = 0, size
            while l != r:
                m = (l + r) // 2
                if tails[m] < num:
                    l = m + 1
                else:
                    r = m
            tails[l] = num
            size = max(size, l + 1)
        return size

    def test_list(self):
        self.assertEqual(self.length_of_lis([10,9,2,5,3,7,101,18]), 4)

