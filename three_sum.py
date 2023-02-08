import unittest


class ThreeSum(unittest.TestCase):
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
    and j != k, and nums[i] + nums[j] + nums[k] == 0.

    The solution set must not contain duplicate triplets.

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    """
    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]: # this step makes sure that we do not have any duplicates in our result output
                continue
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum < 0:
                    mid += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]: # Another conditional for not calculating duplicates
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                        right -= 1
                    mid += 1
                    right -= 1
        return result

    def test_three_sum(self):
        input = [-1,0,1,2,-1,-4]
        output = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(self.three_sum(input), output)