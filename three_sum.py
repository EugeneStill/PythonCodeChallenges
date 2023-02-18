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
        nums_length, result = len(nums), []

        for i in range(nums_length):
            # make sure we are past start of list then skip any repeated values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # determine target
            target = nums[i] * -1
            # set left, right for sliding window
            left, right = i + 1, nums_length - 1
            while left < right:
                # if target found, update result and move sliding window forward
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # continue sliding window forward if duplicate elements are found
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                # if target not found, slide window forward/back depending on whether sum of left+right elements < or > target
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -=1
        return result

    def test_three_sum(self):
        input = [-1,0,1,2,-1,-4]
        output = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(self.three_sum(input), output)