import unittest

class BinarySearch(unittest.TestCase):

    def bin_search(self, nums, target) -> int:
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # End Condition: left > right
        return -1

    def test_bin_search(self):
        sl = [3, 5, 7, 13, 18, 23, 35, 41, 50, 65, 70, 88]
        self.assertEqual(self.bin_search(sl, 70), 10)
        self.assertEqual(self.bin_search(sl, 2), -1)
        self.assertEqual(self.bin_search(sl, 3), 0)
        self.assertEqual(self.bin_search(sl, 88), 11)
        self.assertEqual(self.bin_search(sl, 90), -1)



# 5 / 2 will return 2.5
# 5 // 2 will return 2
# The former is floating point division, and the latter is floor division, sometimes also called integer division

# Binary Search Alt Methods w/ Post Processing
# def binarySearch(nums, target):
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


# def binarySearch(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     if len(nums) == 0:
#         return -1
#
#     left, right = 0, len(nums) - 1
#     while left + 1 < right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid
#         else:
#             right = mid
#
#     # Post-processing:
#     # End Condition: left + 1 == right
#     if nums[left] == target: return left
#     if nums[right] == target: return right
#     return -1