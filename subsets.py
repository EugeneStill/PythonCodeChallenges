import unittest


class Subsets(unittest.TestCase):
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.
    """

    def subsets_iterative(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        print("\n" + str(subsets))
        for n in nums:
            subsets += [s + [n] for s in subsets]
            print(str(subsets))
        return subsets
    def subsets_recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        print("\n")
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            print("I " + str(i) + str(ret))
            self.dfs(nums[i + 1:], path + [nums[i]], ret)


    def test_sub_iter(self):
        input = [1, 2, 3]
        output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(sorted(self.subsets_iterative(input)), sorted(output))

    # def test_sub_recursive(self):
    #     input = [1, 2, 3]
    #     output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    #     self.assertEqual(sorted(self.subsets_recursive(input)), sorted(output))

# ITERATIVE LOGGING
# [[]]
# [[], [1]]
# [[], [1], [2], [1, 2]]
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]