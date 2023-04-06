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
        res = []
        self.dfs(nums, [], 0, res)
        return res

    def dfs(self, nums, path, start, res):
        # use [:] to create shallow copy of path
        res.append(path[:])
        # we use start to decrease the number of subsets being generated
        for i in range(start, len(nums)):
            # add nums[i] to path here
            path.append(nums[i])
            self.dfs(nums, path, i + 1, res)
            # pop the num from path to backtrack to previous state
            path.pop()


# The path.pop() method is being called to backtrack to the previous state of the path list,
# after a valid subset has been generated.
#
# In the dfs function, we add elements to path to generate the current subset,
# and then recursively call dfs to generate the next subset.
# Once all valid subsets have been generated from the current state of path,
# we need to backtrack to the previous state of path to generate more subsets.


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