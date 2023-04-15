import unittest


class HouseRobber(unittest.TestCase):
    """
    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them
    is that adjacent houses have security systems connected and it will automatically contact the police
    if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house,
    return the maximum amount of money you can rob tonight without alerting the police.

    HINT: in some cases more money can be made by skipping more than one house
    """
    def house_robber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = now = 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

    def test_house_robber(self):
        nums1 = [2,7,9,3,1]
        nums2 = [2, 7, 9, 3, 1, 6]
        self.assertEqual(self.house_robber(nums1), 12)
        self.assertEqual(self.house_robber(nums2), 17)

# OUTPUT
# [2, 7, 9, 3, 1]
# LAST0 NOW2
# LAST2 NOW7
# LAST7 NOW11
# LAST11 NOW11
# LAST11 NOW12
#
# [2, 7, 9, 3, 1, 6]
# LAST0 NOW2
# LAST2 NOW7
# LAST7 NOW11
# LAST11 NOW11
# LAST11 NOW12
# LAST12 NOW17