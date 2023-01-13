import unittest

class BinarySearchRecursion(unittest.TestCase):

    def bin_search_recursion(self, sl, start, end, target) -> int:
        if end < start:
            return -1
        else:
            mid = start + ((end - start) // 2)
            print("mid is {}".format(mid))
        if sl[mid] > target:
            return self.bin_search_recursion(sl, start, mid -1, target)
        elif sl[mid] < target:
            return self.bin_search_recursion(sl, mid + 1, end, target)
        else:
            return mid

    def test_bsr(self):
        sl = [3, 5, 7, 13, 18, 23, 35, 41, 50, 65, 70, 88]
        self.assertEqual(self.bin_search_recursion(sl, 0, len(sl) -1, 90), -1)



# 5 / 2 will return 2.5
# 5 // 2 will return 2
# The former is floating point division, and the latter is floor division, sometimes also called integer division