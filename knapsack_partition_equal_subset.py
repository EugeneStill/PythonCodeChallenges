import unittest


class CanPartition(unittest.TestCase):
    """
    return true if you can partition array nums into two subsets where sum of elements in both subsets is equal
    return false otherwise.
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].
    ****** DEBUG THIS ONE MORE
    """
    def can_partition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        # if sum isn't even it can't be split evenly
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            print("\nCHECKING NUM {}".format(num))
            if num > target:
                return False
            for i in range(target, num - 1, -1):
                print("CHECKING i {}".format(i))
                if dp[target]:
                    return True
                dp[i] = dp[i] or dp[i - num]
                print(str(dp))
        return dp[target]

    def test_partition(self):
        self.can_partition([1,5,8,3,5])

