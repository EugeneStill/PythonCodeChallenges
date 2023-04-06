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

    # class Solution(object):
    #     def longestPalindrome(self, s):
    #         """
    #         :type s: str
    #         :rtype: str
    #         """
    #         # Preprocess the input string by adding special characters between
    #         # each character and at the beginning and end of the string.
    #         t = "#" + "#".join(s) + "#"
    #
    #         # Initialize variables for the center of the palindrome and its right edge.
    #         center = 0
    #         right = 0
    #
    #         # Initialize an array to store the lengths of the palindromes centered at each position.
    #         p = [0] * len(t)
    #
    #         # Iterate over each position in the input string.
    #         for i in range(1, len(t) - 1):
    #             # Mirror the index i around the center to find the corresponding index j.
    #             j = 2 * center - i
    #
    #             # If i is within the right edge of the palindrome centered at center,
    #             # use the value of p[j] to initialize p[i].
    #             if right > i:
    #                 p[i] = min(right - i, p[j])
    #
    #             # Expand the palindrome centered at i as far as possible.
    #             while t[i + p[i] + 1] == t[i - p[i] - 1]:
    #                 p[i] += 1
    #
    #             # If the right edge of the palindrome centered at i extends beyond the
    #             # right edge of the palindrome centered at center, update center and right.
    #             if i + p[i] > right:
    #                 center = i
    #                 right = i + p[i]
    #
    #         # Find the longest palindrome in t and return it without the special characters.
    #         max_len = max(p)
    #         center_index = p.index(max_len)
    #         return s[(center_index - max_len) // 2: (center_index + max_len) // 2]

    def test_lps(self):
        self.assertEqual(self.lps('a'), 'a')
        self.assertEqual(self.lps('racecar'), 'racecar')
        self.assertEqual(self.lps('hghottohnbd'), 'hottoh')



