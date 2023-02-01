import unittest
class BinSearchRotation(unittest.TestCase):
    """
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
    such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
    or -1 if it is not in nums.

    To solve, determine which direction the array has been rotated in each iteration of the search:
    NOT ROTATED:
    1 2 3 4 5 6 7
         mid

    LEFT ROTATED:
    pivot at the left side of the origin sorted array, A[mid] >= A[left]
    3 4 5 6 7 1 2
         mid
    search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side

    RIGHT ROTATED:
    pivot at the right side of the origin sorted array, A[mid] < A[left]
    6 7 1 2 3 4 5
         mid
    search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
    """
    def bin_search_rotation(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        print("\n SEARCHING FOR {}".format(target))
        while left <= right:
            mid = (left + right) // 2
            # if found target value, return the index
            if nums[mid] == target:
                return mid

            # left rotated or not rotated
            if nums[mid] >= nums[left]:
                print("checking lr")
                # in ascending order side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right rotated
            else:
                print("checking rr")
                # in ascending order side
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # cannot find the target value
        return -1

    def bin_search_find_min(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

    def bin_search_find_min_with_dupes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        print("\n")
        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[hi] != nums[mid]:
                hi = mid
            # when num[mid] == num[hi], min could be in mid's left or right, so reduce upper bound to check again.
            else:
                hi -= 1
        return nums[lo]

    def test_rotation(self):
        left_rotated = [3, 4, 5, 6, 7, 1, 2]
        rotated_with_dupes = [4,5,6,7,0,1,4]
        self.assertEqual(self.bin_search_rotation(left_rotated, 8), -1)
        self.assertEqual(self.bin_search_rotation(left_rotated, 0), -1)
        self.assertEqual(self.bin_search_rotation(left_rotated, 3), 0)
        self.assertEqual(self.bin_search_rotation(left_rotated, 4), 1)
        self.assertEqual(self.bin_search_rotation(left_rotated, 5), 2)
        self.assertEqual(self.bin_search_rotation(left_rotated, 6), 3)
        self.assertEqual(self.bin_search_rotation(left_rotated, 7), 4)
        self.assertEqual(self.bin_search_rotation(left_rotated, 1), 5)
        self.assertEqual(self.bin_search_rotation(left_rotated, 2), 6)
        self.assertEqual(self.bin_search_find_min(left_rotated), 1)
        self.assertEqual(self.bin_search_find_min_with_dupes(rotated_with_dupes), 0)


# def binarySearchPostProcessing(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     if len(nums) == 0:
#         return -1
#
#     left, right = 0, len(nums) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#
#     # Post-processing:
#     # End Condition: left == right
#     if left != len(nums) and nums[left] == target:
#         return left
#     return -1


