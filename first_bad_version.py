# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import unittest


class FirstBadVersion():
    """
    You are a product manager and currently leading a team to develop a new product.
    Unfortunately, the latest version of your product fails the quality check.
    Since each version is developed based on the previous version, all the versions after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
    which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which returns whether version is bad.
    Implement a function to find the first bad version. You should minimize the number of calls to the API.
    """
    def __init__(self, versions):
        self.versions = versions

    def is_bad_version(self, version):
        return self.versions[version] == "bad"

    def first_bad_version(self):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, len(self.versions) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_bad = self.is_bad_version(mid)
            if mid_bad and not self.is_bad_version(mid-1):
                return mid
            elif mid_bad:
                r = mid - 1
            else:
                l = mid + 1


class TestFBS(unittest.TestCase):
    def test_fbv(self):
        versions = ['good', 'good', 'good', 'good', 'good', 'bad', 'bad']
        fbv = FirstBadVersion(versions)
        self.assertEqual(fbv.first_bad_version(), 5)
