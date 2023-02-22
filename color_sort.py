import unittest


class SortColors(unittest.TestCase):
    """
    Given an array nums with n objects colored red, white, or blue, sort them in-place
    so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.
    https://en.wikipedia.org/wiki/Dutch_national_flag_problem

    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    """
    def sort_colors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1

        # use 3 pointers to track boundaries in list
        after_white, after_red, before_blue = 0, 0, len(nums) - 1
        RED, WHITE, BLUE = 0, 1, 2

        # we will use the middle pointer (after_white) to evaluate when we need to move elements
        while after_white <= before_blue:
            print("\n" + str(nums))
            # FOUND RED. MOVE TO LEFT SIDE OF LIST.
            if nums[after_white] == RED:
                nums[after_red], nums[after_white] = nums[after_white], nums[after_red]
                after_white += 1
                after_red += 1
            # FOUND WHITE.  KEPT IN MIDDLE.
            elif nums[after_white] == WHITE:
                after_white += 1
            # FOUND BLUE.  MOVED TO RIGHT SIDE OF LIST.
            else:
                nums[after_white], nums[before_blue] = nums[before_blue], nums[after_white]
                before_blue -= 1
        return nums

    def test_sort(self):
        self.assertEqual(self.sort_colors([2,0,2,1,1,0]), [0,0,1,1,2,2])

# LOGGING
# [2, 0, 2, 1, 1, 0]
#
# [0, 0, 2, 1, 1, 2]
#
# [0, 0, 2, 1, 1, 2]
#
# [0, 0, 2, 1, 1, 2]
#
# [0, 0, 1, 1, 2, 2]
#
# [0, 0, 1, 1, 2, 2]