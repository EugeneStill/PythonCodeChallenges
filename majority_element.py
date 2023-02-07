import unittest


class MajorityElement(unittest.TestCase):
    """
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    """
    def majority_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = len(nums) / 2
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
            if dic[n] > majority:
                return n

    def test_majority(self):
        nums1 = [3,2,3]
        nums2 = [2,2,1,1,1,2,2]
        self.assertEqual(self.majority_element(nums1), 3)
        self.assertEqual(self.majority_element(nums2), 2)
