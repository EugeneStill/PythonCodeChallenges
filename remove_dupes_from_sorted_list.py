import unittest

class TestNoDupes(unittest.TestCase):

    def rd(self, nums) -> int:
        # nums is sorted list
        # problem asks us to move non-duplicated elements to front of list
        # return length of non-duplicated values
        left = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i]
                left += 1
        return left

    def test_rd(self):
        self.assertEqual(self.rd([1, 1, 2]), 2)



