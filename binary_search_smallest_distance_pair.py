import unittest


class smallestDistancePair(unittest.TestCase):
    """
    The distance of a pair of integers a and b is defined as the absolute difference between a and b.

    Given an integer array nums and an integer k, return the kth smallest distance
    among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

    Input: nums = [1,3,1], k = 1
    Output: 0
    Explanation: Here are all the pairs:
    (1,3) -> 2
    (1,1) -> 0
    (3,1) -> 2
    Then the 1st smallest distance pair is (1,1), and its distance is 0.

    Input: nums = [1,6,1], k = 3
    Output: 5

    """
    def smallest_distance_pair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def enough_pairs(distance):
            pair_count, sp, fp = 0, 0, 0
            print("DISTANCE {}".format(distance))
            while sp < n or fp < n:
                # move fast pointer until difference between numbers at fast pointer and slow pointer > distance
                while fp < n and nums[fp] - nums[sp] <= distance:
                    fp += 1
                # update pair_count total with all of the pairs between fp & sp
                # we count them all because these are contiguous numbers (binary search is on range, not nums)
                pair_count += fp - sp - 1
                print("PC {} FP {} SP {}".format(pair_count, fp, sp))
                # move slow pointer
                sp += 1
            print("ENOUGH ? {}".format(pair_count >=k))
            return pair_count >= k

        nums.sort()
        print("\n{}".format(str(nums)))
        n = len(nums)
        # do binary search on range from 0 to greatest difference of pairs in nums
        # we use 0 since there could be 2 elements in nums with same value and difference for that pair would be 0
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            print("LEFT {} RIGHT {}".format(left, right))
            mid = (right + left) // 2
            if not enough_pairs(mid):
                left = mid + 1
            else:
                right = mid
        return left

    def test_sd(self):
        self.assertEqual(self.smallest_distance_pair([1, 6, 1, 5, 8, 10, 15, 19], 1), 0)
        self.assertEqual(self.smallest_distance_pair([1, 6, 1, 5, 8, 10, 15, 19], 5), 3)