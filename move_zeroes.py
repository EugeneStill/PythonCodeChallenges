import unittest


class MoveZeroes(unittest.TestCase):
    """
    move all zeroes to end of list of numbers while preserving order of other numbers in list
    """
    def move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, end = 0, len(nums)

        while i < end:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                end -= 1
            else:
                i += 1
        return nums

    def test_move_zeroes(self):
        input1 = [0,1,0,3,12]
        output1 = [1, 3, 12, 0, 0]
        input2 = [0]
        output2 = [0]
        self.assertEqual(self.move_zeroes(input1), output1)
        self.assertEqual(self.move_zeroes(input2), output2)