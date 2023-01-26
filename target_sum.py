import unittest
import collections

class TargetSum(unittest.TestCase):
    """
    given an integer array nums and an integer target.

    build an expression out of nums by adding one of the symbols '+' and '-' before each integer
    then concatenate all the integers.

    EG, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 & concatenate to build the expression "+2-1".
    Return the number of different expressions that you can build, which evaluates to target.

    Example 1:
    Input: nums = [1,1,1,1,1], target = 3
    Output: 5
    Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3

    Example 2:
    Input: nums = [1], target = 1
    Output: 1

    Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000
    """


    def target_sum_combos(self, nums, S):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = collections.defaultdict(int)
        count[0] = 1
        # for each iteration of x, the count values double
        # store the sum of iterative +/- x nums in the count as keys and the actual count of each of those sums as value
        for x in nums:
            print("\nX: {}".format(x))
            step = collections.defaultdict(int)
            for y in count:
                print("Y VAL: {} Y COUNT: {}".format(y, count[y]))
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
            print("COUNT " + str(count))
        return count[S]


    def test_target_sum(self):
        self.target_sum_combos([1,1,1,1,1], 3)


# LOGGING
# target_sum.py::TargetSum::test_target_sum
# X: 1
# Y VAL: 0 Y COUNT: 1
# COUNT defaultdict(<class 'int'>, {1: 1, -1: 1})
#
# X: 1
# Y VAL: 1 Y COUNT: 1
# Y VAL: -1 Y COUNT: 1
# COUNT defaultdict(<class 'int'>, {2: 1, 0: 2, -2: 1})
#
# X: 1
# Y VAL: 2 Y COUNT: 1
# Y VAL: 0 Y COUNT: 2
# Y VAL: -2 Y COUNT: 1
# COUNT defaultdict(<class 'int'>, {3: 1, 1: 3, -1: 3, -3: 1})
#
# X: 1
# Y VAL: 3 Y COUNT: 1
# Y VAL: 1 Y COUNT: 3
# Y VAL: -1 Y COUNT: 3
# Y VAL: -3 Y COUNT: 1
# COUNT defaultdict(<class 'int'>, {4: 1, 2: 4, 0: 6, -2: 4, -4: 1})
#
# X: 1
# Y VAL: 4 Y COUNT: 1
# Y VAL: 2 Y COUNT: 4
# Y VAL: 0 Y COUNT: 6
# Y VAL: -2 Y COUNT: 4
# Y VAL: -4 Y COUNT: 1
# COUNT defaultdict(<class 'int'>, {5: 1, 3: 5, 1: 10, -1: 10, -3: 5, -5: 1})


