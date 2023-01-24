import unittest

class FirstUniqueChar(unittest.TestCase):
    """
    return index of first unique character in a string, else return -1
    """

    def unique_idx(self, s):
        """
        :type s: str
        :rtype: idx
        """
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1


    def test_unique_idx(self):
        s1 = "abba"
        s2 = "bobloblaw"
        self.assertEqual(self.unique_idx(s1), -1)
        self.assertEqual(self.unique_idx(s2), 7)



