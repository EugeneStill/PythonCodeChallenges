import unittest


class splitArray(unittest.TestCase):
    """
    Given an integer array nums and an integer k, split nums into k non-empty subarrays
    such that the largest sum of any subarray is minimized.

    Return the minimized largest sum of the split.

    A subarray is a contiguous part of the array.
    """
    def split_array(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # we will binary search a range of numbers from largest number in nums to the sum of nums
        lo, hi = max(nums), sum(nums)
        # adjust hi/lo in the range until we arrive at the largest subarray sum (meeting min number of subarrays)
        while lo < hi:
            mid = (lo + hi) // 2
            tot, sub_array_cnt = 0, 1
            # each time we get a new mid, build out subarray totals that are <= mid
            for num in nums:
                if tot + num <= mid:
                    tot += num
                else:
                    tot = num
                    sub_array_cnt += 1
                    print("INCREMENTED COUNT TO {} AND SET TOT {}".format(sub_array_cnt, tot))
            if sub_array_cnt > k:
                print("SUB ARRAYS {} > K, MOVING LO FORWARD".format(sub_array_cnt))
                lo = mid + 1
            else:
                print("SUB ARRAYS {} <= K, MOVING HI BACKWARD".format(sub_array_cnt))
                hi = mid
        print(hi)
        return hi

    def test_split_array(self):
        nums = [7, 2, 5, 10, 8]
        self.split_array(nums, 3)