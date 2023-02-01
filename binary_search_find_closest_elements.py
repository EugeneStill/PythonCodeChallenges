import unittest


class FindClosestElements(unittest.TestCase):
    """
    Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
    The result should also be sorted in ascending order.

    An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
    """
    def find_closest_elements(self, arr, k, target):
        """
        :type arr: List[int]
        :type k: int
        :type target: int
        :rtype: List[int]
        """

        # since we need to return k elements, we can reduce length of array to check by k
        low, high = 0, len(arr) - k
        print("\n")
        while low < high:
            mid = (low + high) // 2

            # target is at or before mid
            if target <= arr[mid]:
                high = mid

            # target is at or after mid + k so low becomes mid + 1
            elif arr[mid + k] <= target:
                low = mid + 1

            # target is between mid and mid + k
            else:
                middist = abs(target - arr[mid])
                midkdist = abs(target - arr[mid + k])
                # target is closer to mid, move high to mid
                if middist <= midkdist:
                    high = mid
                # target is closer to mid + k, move low to mid + 1
                else:
                    low = mid + 1
        return arr[low:low + k]

    def test_closest_elements(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        target, k = 6, 4
        self.assertEqual(self.find_closest_elements(arr, k, target), [4, 5, 6, 7])
