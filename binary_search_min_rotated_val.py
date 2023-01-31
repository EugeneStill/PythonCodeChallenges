import unittest


class FindMin(unittest.TestCase):
    """
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
    For example, the array nums = [0,1,2,4,5,6,7] might become:
        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.

    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in:
        [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    """
    def find_min(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        # force left and right to converge to the minimum index;
        # DO NOT use left <= right because that would loop forever
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # we KNOW the pivot must be to the right of the middle:
                # example:  [3,4,5,6,7,8,9,1,2]
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] > nums[right], we know pivot is some point to the right of mid,
                left = mid + 1

            else:
                # we KNOW the pivot must be at mid or to the left of mid:
                # example: [8,9,1,2,3,4,5,6,7]
                # in the first iteration, when we start with mid index = 4, right index = 9.
                # if nums[mid] <= nums[right], we know the numbers continued increasing
                right = mid

        # at this point, left and right converge to a single index (for minimum value) since
        # our if/else forces the bounds of left/right to shrink each iteration:
        # so we shrink the left/right bounds to one value, never disqualifying a possible minimum
        return nums[left]

    def test_find_min(self):
        self.assertEqual(self.find_min([8, 9, 10, 3, 5, 6, 7]), 3)
        self.assertEqual(self.find_min([7, 8, 9, 10, 3, 5, 6, 7]), 3)