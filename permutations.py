import unittest


class Permute(unittest.TestCase):
    """
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    """
    def permute_iterative(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        stack = [(nums, [])]
        res = []
        print("\n")
        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                stack.append((newNums, path+[nums[i]]))
        return res

    def permute_rescursive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path+[nums[i]])
        res = []
        dfs(nums, [])
        return res

    def test_permutations(self):
        nums = [1, 2, 3]
        output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(sorted(self.permute_iterative(nums)), sorted(output))
        self.assertEqual(sorted(self.permute_rescursive(nums)), sorted(output))