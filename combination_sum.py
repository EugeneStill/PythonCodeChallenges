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
            print("GOT TARGET {} IDX {} PATH {}".format(target, index, path))
            # backtrack to check path with next num in candidates
            if target < 0:
                return  # backtracking to check path with next num in candidates
            # add path to result then return to check path with next num in candidates
            if target == 0:
                print("ADDING PATH {} TO RESULT".format(path))
                res.append(path)
                return
            for i in range(index, len(candidates)):
                # use path + candidates[i] so that we get a new unique path for each dfs call
                # would not work if we tried to use append since the same path would be used for all dfs calls
                print("MAKING NEW CALL FOR TARGET {} IDX {} PATH {}".format(target - candidates[i], i, path + [candidates[i]]))
                dfs(target - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return res

    def test_combination_sum(self):
        self.combination_sum([2,3,5], 8)


# LOGGING
# GOT TARGET 8 IDX 0 PATH []
# MAKING NEW CALL FOR TARGET 6 IDX 0 PATH [2]
# GOT TARGET 6 IDX 0 PATH [2]
# MAKING NEW CALL FOR TARGET 4 IDX 0 PATH [2, 2]
# GOT TARGET 4 IDX 0 PATH [2, 2]
# MAKING NEW CALL FOR TARGET 2 IDX 0 PATH [2, 2, 2]
# GOT TARGET 2 IDX 0 PATH [2, 2, 2]
# MAKING NEW CALL FOR TARGET 0 IDX 0 PATH [2, 2, 2, 2]
# GOT TARGET 0 IDX 0 PATH [2, 2, 2, 2]
# ADDING PATH [2, 2, 2, 2] TO RESULT
# MAKING NEW CALL FOR TARGET -1 IDX 1 PATH [2, 2, 2, 3]
# GOT TARGET -1 IDX 1 PATH [2, 2, 2, 3]
# MAKING NEW CALL FOR TARGET -3 IDX 2 PATH [2, 2, 2, 5]
# GOT TARGET -3 IDX 2 PATH [2, 2, 2, 5]
# MAKING NEW CALL FOR TARGET 1 IDX 1 PATH [2, 2, 3]
# GOT TARGET 1 IDX 1 PATH [2, 2, 3]
# MAKING NEW CALL FOR TARGET -2 IDX 1 PATH [2, 2, 3, 3]
# GOT TARGET -2 IDX 1 PATH [2, 2, 3, 3]
# MAKING NEW CALL FOR TARGET -4 IDX 2 PATH [2, 2, 3, 5]
# GOT TARGET -4 IDX 2 PATH [2, 2, 3, 5]
# MAKING NEW CALL FOR TARGET -1 IDX 2 PATH [2, 2, 5]
# GOT TARGET -1 IDX 2 PATH [2, 2, 5]
# MAKING NEW CALL FOR TARGET 3 IDX 1 PATH [2, 3]
# GOT TARGET 3 IDX 1 PATH [2, 3]
# MAKING NEW CALL FOR TARGET 0 IDX 1 PATH [2, 3, 3]
# GOT TARGET 0 IDX 1 PATH [2, 3, 3]
# ADDING PATH [2, 3, 3] TO RESULT
# MAKING NEW CALL FOR TARGET -2 IDX 2 PATH [2, 3, 5]
# GOT TARGET -2 IDX 2 PATH [2, 3, 5]
# MAKING NEW CALL FOR TARGET 1 IDX 2 PATH [2, 5]
# GOT TARGET 1 IDX 2 PATH [2, 5]
# MAKING NEW CALL FOR TARGET -4 IDX 2 PATH [2, 5, 5]
# GOT TARGET -4 IDX 2 PATH [2, 5, 5]
# MAKING NEW CALL FOR TARGET 5 IDX 1 PATH [3]
# GOT TARGET 5 IDX 1 PATH [3]
# MAKING NEW CALL FOR TARGET 2 IDX 1 PATH [3, 3]
# GOT TARGET 2 IDX 1 PATH [3, 3]
# MAKING NEW CALL FOR TARGET -1 IDX 1 PATH [3, 3, 3]
# GOT TARGET -1 IDX 1 PATH [3, 3, 3]
# MAKING NEW CALL FOR TARGET -3 IDX 2 PATH [3, 3, 5]
# GOT TARGET -3 IDX 2 PATH [3, 3, 5]
# MAKING NEW CALL FOR TARGET 0 IDX 2 PATH [3, 5]
# GOT TARGET 0 IDX 2 PATH [3, 5]
# ADDING PATH [3, 5] TO RESULT
# MAKING NEW CALL FOR TARGET 3 IDX 2 PATH [5]
# GOT TARGET 3 IDX 2 PATH [5]
# MAKING NEW CALL FOR TARGET -2 IDX 2 PATH [5, 5]
# GOT TARGET -2 IDX 2 PATH [5, 5]