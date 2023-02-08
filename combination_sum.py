import unittest


class CombinationSum(unittest.TestCase):
    def combination_sum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        print("\n")
        def dfs(target, index, path):
            if target < 0:
                return  # backtracking to check path with next num in candidates
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                # use path + candidates[i] so that we get a new unique path for each dfs call
                # would not work if we tried to use append since the same path would be used for all dfs calls
                dfs(target - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return res

    def test_combination_sum(self):
        self.combination_sum([2,3,5], 8)

# LOGGING
# PATH IS []
# CALLING DFS FOR TARGET 6 I 0 PATH [2]
# PATH IS [2]
# CALLING DFS FOR TARGET 4 I 0 PATH [2, 2]
# PATH IS [2, 2]
# CALLING DFS FOR TARGET 2 I 0 PATH [2, 2, 2]
# PATH IS [2, 2, 2]
# CALLING DFS FOR TARGET 0 I 0 PATH [2, 2, 2, 2]
# PATH IS [2, 2, 2]
# CALLING DFS FOR TARGET -1 I 1 PATH [2, 2, 2, 3]
# SKIPPED TARGET -1
# PATH IS [2, 2, 2]
# CALLING DFS FOR TARGET -3 I 2 PATH [2, 2, 2, 5]
# SKIPPED TARGET -3
# PATH IS [2, 2]
# CALLING DFS FOR TARGET 1 I 1 PATH [2, 2, 3]
# PATH IS [2, 2, 3]
# CALLING DFS FOR TARGET -2 I 1 PATH [2, 2, 3, 3]
# SKIPPED TARGET -2
# PATH IS [2, 2, 3]
# CALLING DFS FOR TARGET -4 I 2 PATH [2, 2, 3, 5]
# SKIPPED TARGET -4
# PATH IS [2, 2]
# CALLING DFS FOR TARGET -1 I 2 PATH [2, 2, 5]
# SKIPPED TARGET -1
# PATH IS [2]
# CALLING DFS FOR TARGET 3 I 1 PATH [2, 3]
# PATH IS [2, 3]
# CALLING DFS FOR TARGET 0 I 1 PATH [2, 3, 3]
# PATH IS [2, 3]
# CALLING DFS FOR TARGET -2 I 2 PATH [2, 3, 5]
# SKIPPED TARGET -2
# PATH IS [2]
# CALLING DFS FOR TARGET 1 I 2 PATH [2, 5]
# PATH IS [2, 5]
# CALLING DFS FOR TARGET -4 I 2 PATH [2, 5, 5]
# SKIPPED TARGET -4
# PATH IS []
# CALLING DFS FOR TARGET 5 I 1 PATH [3]
# PATH IS [3]
# CALLING DFS FOR TARGET 2 I 1 PATH [3, 3]
# PATH IS [3, 3]
# CALLING DFS FOR TARGET -1 I 1 PATH [3, 3, 3]
# SKIPPED TARGET -1
# PATH IS [3, 3]
# CALLING DFS FOR TARGET -3 I 2 PATH [3, 3, 5]
# SKIPPED TARGET -3
# PATH IS [3]
# CALLING DFS FOR TARGET 0 I 2 PATH [3, 5]
# PATH IS []
# CALLING DFS FOR TARGET 3 I 2 PATH [5]
# PATH IS [5]
# CALLING DFS FOR TARGET -2 I 2 PATH [5, 5]
# SKIPPED TARGET -2
# [[2, 2, 2, 2], [2, 3, 3], [3, 5]]