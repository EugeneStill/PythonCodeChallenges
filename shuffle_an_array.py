import random


class ShuffleArray(object):
    """
    Given an integer array nums, design an algorithm to randomly shuffle the array.
    All permutations of the array should be equally likely as a result of the shuffling.

    Implement the Solution class:

    Solution(int[] nums) Initializes the object with the integer array nums.
    int[] reset() Resets the array to its original configuration and returns it.
    int[] shuffle() Returns a random shuffling of the array.
    """

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        :rtype: List[int]
        """
        ans = self.nums[:]
        for i in range(len(ans) - 1, 0, -1):
            j = random.randrange(0, i + 1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans