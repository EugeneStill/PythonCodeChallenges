import unittest


class Permute(unittest.TestCase):
    """
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        stack = [(nums, [])]
        res = []
        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                stack.append((newNums, path+[nums[i]]))
        return res

    def test_permutations(self):
        nums = [1, 2, 3]
        output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(sorted(self.permute(nums)), sorted(output))