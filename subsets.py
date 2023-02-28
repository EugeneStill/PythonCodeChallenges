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
        print("ADDED {} TO RET".format(str(path)))
        ret.append(path)
        for i in range(len(nums)):
            print("I {} NUMS {} NEW PATH {} OLD RET {}".format(str(i), str(nums[i + 1:]), str(path + [nums[i]]), str(ret)))
            self.dfs(nums[i + 1:], path + [nums[i]], ret)


    def test_sub_iter(self):
        input_list = [1, 2, 3]
        output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(sorted(self.subsets_iterative(input_list)), sorted(output))

    def test_sub_recursive(self):
        input_list = [1, 2, 3]
        output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(sorted(self.subsets_recursive(input_list)), sorted(output))

# ITERATIVE LOGGING
# [[]]
# [[], [1]]
# [[], [1], [2], [1, 2]]
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# RECURSIVE LOGGING
# ADDED [] TO RET
# I 0 NUMS [2, 3] NEW PATH [1] OLD RET [[]]
# ADDED [1] TO RET
# I 0 NUMS [3] NEW PATH [1, 2] OLD RET [[], [1]]
# ADDED [1, 2] TO RET
# I 0 NUMS [] NEW PATH [1, 2, 3] OLD RET [[], [1], [1, 2]]
# ADDED [1, 2, 3] TO RET
# I 1 NUMS [] NEW PATH [1, 3] OLD RET [[], [1], [1, 2], [1, 2, 3]]
# ADDED [1, 3] TO RET
# I 1 NUMS [3] NEW PATH [2] OLD RET [[], [1], [1, 2], [1, 2, 3], [1, 3]]
# ADDED [2] TO RET
# I 0 NUMS [] NEW PATH [2, 3] OLD RET [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]
# ADDED [2, 3] TO RET
# I 2 NUMS [] NEW PATH [3] OLD RET [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
# ADDED [3] TO RET