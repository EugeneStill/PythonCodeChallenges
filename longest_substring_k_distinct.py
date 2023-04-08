import unittest
from collections import defaultdict


class LongestSubstringKDistinct(unittest.TestCase):
    """
    Given a string s and an integer k, return the length of the longest substring of s that contains
    at most k distinct characters.
    Input: s = "eceba", k = 2
    Output: 3
    Explanation: The substring is "ece" with length 3.
    """
    def longest_substring_k_distinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k == 0:
            return 0
        left = 0
        max_len = 0
        char_freq = defaultdict(int)
        for right in range(len(s)):
            # add the current character to the frequency dictionary
            # char_freq[s[right]] += char_freq.get(s[right], 0) + 1
            char_freq[s[right]] += 1
            # if the number of distinct characters in the dictionary is greater than k,
            # remove the leftmost character and update the dictionary accordingly
            while len(char_freq) > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]]
                left += 1
            # update the maximum length if a longer substring is found
            max_len = max(max_len, right - left + 1)
        return max_len

    def test_longest_substring_k_distinct(self):
        self.assertEqual(self.longest_substring_k_distinct("eceba", 2), 3)
        self.assertEqual(self.longest_substring_k_distinct("aaaaaaaaaaaaaa", 1), 14)