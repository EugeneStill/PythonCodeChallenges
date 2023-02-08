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

        """
        We are classifying the array into four groups: red, white, unclassified, and blue. 
        Initially we group all elements into unclassified. 
        We iterate from the beginning as long as the white pointer is less than the blue pointer.
        If the white pointer is red (0) we swap with the red pointer and move both white and red pointer forward. 
        If the pointer is white (1) element is in correct place. don't swap, just move the white pointer forward. 
        If the white pointer is blue, we swap with the latest unclassified element.
        """
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
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