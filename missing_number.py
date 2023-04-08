import unittest


class MissingNumber(unittest.TestCase):
    """
    find the missing number in an unordered list where the full range of numbers is from 0 to length of list
    """
    def missing_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums) * (len(nums) + 1))//2 - sum(nums)

    def test_missing_number(self):
        input1 = [9,6,4,2,3,5,7,0,1]
        self.assertEqual(self.missing_number(input1), 8)