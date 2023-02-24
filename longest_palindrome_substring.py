import unittest

class LongPalSub(unittest.TestCase):

    def lps(self, s):
        """
        :type s: str
        :rtype: str
        """
        # handles even values like 'abba'
        # p1 = self.get_palindrome(s, i, i + 1)
        # handles odd values like 'aba'
        # p2 = self.get_palindrome(s, i, i)
        p = ''
        for i in range(len(s)):
            p = max([p, self.get_palindrome(s, i, i), self.get_palindrome(s, i, i+1)], key=len)
        return p

    def get_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def test_lps(self):
        self.assertEqual(self.lps('a'), 'a')
        self.assertEqual(self.lps('racecar'), 'racecar')
        self.assertEqual(self.lps('hghottohnbd'), 'hottoh')



