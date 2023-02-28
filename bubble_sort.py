import unittest


class bubbleSort(unittest.TestCase):
    """
    According to Wikipedia "Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that
    repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are
    in the wrong order. The pass through the list is repeated until no swaps are needed,
    which indicates that the list is sorted. The algorithm, which is a comparison sort, is named for the way
    smaller elements "bubble" to the top of the list. Although the algorithm is simple, it is too slow and
    impractical for most problems even when compared to insertion sort. It can be practical if the input is
    usually in sort order but may occasionally have some out-of-order elements nearly in position.
    """
    def bubble_sort(self, nums):
        print("\n")
        # decrement passes from end of nums length
        for passnum in range(len(nums) - 1, 0, -1):
            print("IN PASSNUM {}".format(passnum))
            # increment i from 0 to end of passnum value
            for i in range(passnum):
                print("CHECKING I {}".format(i))
                if nums[i]>nums[i + 1]:
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
                print(str(nums))
        return nums

    def test_bubble_sort(self):
        input_list = [14, 46, 43, 27, 57, 41, 45, 21, 70, 4, 2]
        output = [2, 4, 14, 21, 27, 41, 43, 45, 46, 57, 70]
        self.assertEqual(self.bubble_sort(input_list), output)


# LOGGING
# IN PASSNUM 10
# CHECKING I 0
# [14, 46, 43, 27, 57, 41, 45, 21, 70, 4, 2]
# CHECKING I 1
# [14, 43, 46, 27, 57, 41, 45, 21, 70, 4, 2]
# CHECKING I 2
# [14, 43, 27, 46, 57, 41, 45, 21, 70, 4, 2]
# CHECKING I 3
# [14, 43, 27, 46, 57, 41, 45, 21, 70, 4, 2]
# CHECKING I 4
# [14, 43, 27, 46, 41, 57, 45, 21, 70, 4, 2]
# CHECKING I 5
# [14, 43, 27, 46, 41, 45, 57, 21, 70, 4, 2]
# CHECKING I 6
# [14, 43, 27, 46, 41, 45, 21, 57, 70, 4, 2]
# CHECKING I 7
# [14, 43, 27, 46, 41, 45, 21, 57, 70, 4, 2]
# CHECKING I 8
# [14, 43, 27, 46, 41, 45, 21, 57, 4, 70, 2]
# CHECKING I 9
# [14, 43, 27, 46, 41, 45, 21, 57, 4, 2, 70]
# IN PASSNUM 9
# CHECKING I 0
# [14, 43, 27, 46, 41, 45, 21, 57, 4, 2, 70]
# CHECKING I 1
# [14, 27, 43, 46, 41, 45, 21, 57, 4, 2, 70]
# CHECKING I 2
# [14, 27, 43, 46, 41, 45, 21, 57, 4, 2, 70]
# CHECKING I 3
# [14, 27, 43, 41, 46, 45, 21, 57, 4, 2, 70]
# CHECKING I 4
# [14, 27, 43, 41, 45, 46, 21, 57, 4, 2, 70]
# CHECKING I 5
# [14, 27, 43, 41, 45, 21, 46, 57, 4, 2, 70]
# CHECKING I 6
# [14, 27, 43, 41, 45, 21, 46, 57, 4, 2, 70]
# CHECKING I 7
# [14, 27, 43, 41, 45, 21, 46, 4, 57, 2, 70]
# CHECKING I 8
# [14, 27, 43, 41, 45, 21, 46, 4, 2, 57, 70]
# IN PASSNUM 8
# CHECKING I 0
# [14, 27, 43, 41, 45, 21, 46, 4, 2, 57, 70]
# CHECKING I 1
# [14, 27, 43, 41, 45, 21, 46, 4, 2, 57, 70]
# CHECKING I 2
# [14, 27, 41, 43, 45, 21, 46, 4, 2, 57, 70]
# CHECKING I 3
# [14, 27, 41, 43, 45, 21, 46, 4, 2, 57, 70]
# CHECKING I 4
# [14, 27, 41, 43, 21, 45, 46, 4, 2, 57, 70]
# CHECKING I 5
# [14, 27, 41, 43, 21, 45, 46, 4, 2, 57, 70]
# CHECKING I 6
# [14, 27, 41, 43, 21, 45, 4, 46, 2, 57, 70]
# CHECKING I 7
# [14, 27, 41, 43, 21, 45, 4, 2, 46, 57, 70]
# IN PASSNUM 7
# CHECKING I 0
# [14, 27, 41, 43, 21, 45, 4, 2, 46, 57, 70]
# CHECKING I 1
# [14, 27, 41, 43, 21, 45, 4, 2, 46, 57, 70]
# CHECKING I 2
# [14, 27, 41, 43, 21, 45, 4, 2, 46, 57, 70]
# CHECKING I 3
# [14, 27, 41, 21, 43, 45, 4, 2, 46, 57, 70]
# CHECKING I 4
# [14, 27, 41, 21, 43, 45, 4, 2, 46, 57, 70]
# CHECKING I 5
# [14, 27, 41, 21, 43, 4, 45, 2, 46, 57, 70]
# CHECKING I 6
# [14, 27, 41, 21, 43, 4, 2, 45, 46, 57, 70]
# IN PASSNUM 6
# CHECKING I 0
# [14, 27, 41, 21, 43, 4, 2, 45, 46, 57, 70]
# CHECKING I 1
# [14, 27, 41, 21, 43, 4, 2, 45, 46, 57, 70]
# CHECKING I 2
# [14, 27, 21, 41, 43, 4, 2, 45, 46, 57, 70]
# CHECKING I 3
# [14, 27, 21, 41, 43, 4, 2, 45, 46, 57, 70]
# CHECKING I 4
# [14, 27, 21, 41, 4, 43, 2, 45, 46, 57, 70]
# CHECKING I 5
# [14, 27, 21, 41, 4, 2, 43, 45, 46, 57, 70]
# IN PASSNUM 5
# CHECKING I 0
# [14, 27, 21, 41, 4, 2, 43, 45, 46, 57, 70]
# CHECKING I 1
# [14, 21, 27, 41, 4, 2, 43, 45, 46, 57, 70]
# CHECKING I 2
# [14, 21, 27, 41, 4, 2, 43, 45, 46, 57, 70]
# CHECKING I 3
# [14, 21, 27, 4, 41, 2, 43, 45, 46, 57, 70]
# CHECKING I 4
# [14, 21, 27, 4, 2, 41, 43, 45, 46, 57, 70]
# IN PASSNUM 4
# CHECKING I 0
# [14, 21, 27, 4, 2, 41, 43, 45, 46, 57, 70]
# CHECKING I 1
# [14, 21, 27, 4, 2, 41, 43, 45, 46, 57, 70]
# CHECKING I 2
# [14, 21, 4, 27, 2, 41, 43, 45, 46, 57, 70]
# CHECKING I 3
# [14, 21, 4, 2, 27, 41, 43, 45, 46, 57, 70]
# IN PASSNUM 3
# CHECKING I 0
# [14, 21, 4, 2, 27, 41, 43, 45, 46, 57, 70]
# CHECKING I 1
# [14, 4, 21, 2, 27, 41, 43, 45, 46, 57, 70]
# CHECKING I 2
# [14, 4, 2, 21, 27, 41, 43, 45, 46, 57, 70]
# IN PASSNUM 2
# CHECKING I 0
# [4, 14, 2, 21, 27, 41, 43, 45, 46, 57, 70]
# CHECKING I 1
# [4, 2, 14, 21, 27, 41, 43, 45, 46, 57, 70]
# IN PASSNUM 1
# CHECKING I 0
# [2, 4, 14, 21, 27, 41, 43, 45, 46, 57, 70]
# PASSED

