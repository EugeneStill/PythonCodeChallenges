import unittest

class NearbyDuplicates(unittest.TestCase):
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
    such that nums[i] == nums[j] and abs(i - j) <= k.
    """

    def check_nearby_dupes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # if len(l2) < 2:
        #     return False
        seen = {}
        for i, n in enumerate(nums):
            if n in seen and abs(seen[n] - i) <= k:
                    return True
            seen[n] = i
        return False

    def test_nearby_dupes(self):
        l1 = [1, 8, 2, 3, 4, 4, 6]
        l2 = [1, 6, 5, 10, 3, 1]
        l3 = [5]
        self.assertTrue(self.check_nearby_dupes(l1, 1))
        self.assertFalse(self.check_nearby_dupes(l1, 0))
        self.assertTrue(self.check_nearby_dupes(l2, 5))
        self.assertFalse(self.check_nearby_dupes(l2, 4))
        self.assertFalse(self.check_nearby_dupes(l3, 1))




