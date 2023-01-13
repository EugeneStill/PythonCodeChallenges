import unittest

class LongPalSub(unittest.TestCase):

    def lps(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = ''
        for i in range(len(s)):
            # handles even values like 'abba'
            p1 = self.get_palindrome(s, i, i + 1)
            # handles odd values like 'aba'
            p2 = self.get_palindrome(s, i, i)
            p = max([p, p1, p2], key=len)
            print("p is {}".format(p))
        return p

    def get_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    def test_lps(self):
        self.assertEqual(self.lps('a'), 'a')



