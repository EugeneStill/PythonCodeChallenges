import unittest


class BinarySearchOrNextSmallest(unittest.TestCase):
    """
    Given an array of positive sorted integers, and a target integer return the target integer if found,
    or the next smallest integer in the list.  Return -1 for all other cases.
    """

    def binary_search_or_next_smallest(self, a, target):
        """
        :type a: List[int]
        :type target: int
        :rtype: int
        """

        if not a or target < a[0]:
            return -1

        left, right = 0, len(a) -1
        while left < right:
            mid = (left + right) // 2
            if a[mid] == target:
                return target
            elif a[mid] < target:
                left = mid +1
            else:
                right = mid -1
        return a[right]


    def test_binary_search_or_next_smallest(self):
        a = [3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21]
        self.assertEqual(self.binary_search_or_next_smallest(a, 2), -1)
        self.assertEqual(self.binary_search_or_next_smallest(None, 3), -1)
        self.assertEqual(self.binary_search_or_next_smallest([], 3), -1)
        self.assertEqual(self.binary_search_or_next_smallest(a, 3), 3)
        self.assertEqual(self.binary_search_or_next_smallest(a, 21), 21)
        self.assertEqual(self.binary_search_or_next_smallest(a, 22), 21)
        self.assertEqual(self.binary_search_or_next_smallest(a, 13), 12)
        self.assertEqual(self.binary_search_or_next_smallest(a, 12), 12)