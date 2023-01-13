import unittest

class BinarySearch(unittest.TestCase):

    def bin_search(self, sl, target) -> int:
        start = 0
        end = len(sl) - 1
        while end >= start:
            mid = start + ((end - start) // 2)
            if sl[mid] == target:
                return mid
            if sl[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        return -1

    def test_bin_search(self):
        sl = [3, 5, 7, 13, 18, 23, 35, 41, 50, 65, 70, 88]
        self.assertEqual(self.bin_search(sl, 70), 10)
        self.assertEqual(self.bin_search(sl, 2), -1)
        self.assertEqual(self.bin_search(sl, 3), 0)
        self.assertEqual(self.bin_search(sl, 88), 11)
        self.assertEqual(self.bin_search(sl, 90), -1)



# 5 / 2 will return 2.5
# 5 // 2 will return 2
# The former is floating point division, and the latter is floor division, sometimes also called integer division