import unittest
import collections

class FindAnagrams(unittest.TestCase):
    """
    Given two strings s and p, return an array of all the start indices of p's anagrams in s.
    You may return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    """

    def find_anagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        char_freqs, indices, len_p, len_s = collections.defaultdict(int), [], len(p), len(s)

        # s cannot have p anangrams if len(p) > len(s)
        if len_p > len_s:
            return indices

        # build map of character frequencies in p
        for char in p:
            char_freqs[char] += 1
        # print("\nAFTER P {}".format(str(char_freqs)))

        # initial pass through window, except last element which we will check when we slide window through s
        for i in range(len_p - 1):
            if s[i] in char_freqs:
                char_freqs[s[i]] -= 1
        # print("AFTER PASS 1 {}".format(str(char_freqs)))

        # slide the window through the rest of s, starting by adding the last element to the initial window
        for i in range(len_p - 1, len_s):
            # j is element before start of current window
            j = i - len_p
            # print("I {} J {}".format(i, j))

            # if s[j] was in p, increment it by 1 so that the current window evaluates the count correctly
            if j >= 0 and s[j] in char_freqs:
                char_freqs[s[j]] += 1
                # print("ADDING TO CF FOR J")
            # if s[i] is in p then decrement it for current window
            if s[i] in char_freqs:
                # print("REMOVING FROM CF FOR I")
                char_freqs[s[i]] -= 1
            # any time all counts are 0 we have found an anagram
            if all(v == 0 for v in char_freqs.values()):
                # print("FOUND ANAGRAM AT {}".format(j + 1))
                indices.append(j + 1)

        return indices

    def test_anagrams(self):
        # s = "cbaebabacd"
        # p = "abc"
        s = "abab"
        p = "ab"
        output = [0, 1, 2]
        self.assertEqual(self.find_anagrams(s, p), output)

# LOGGING
# AFTER P defaultdict(<class 'int'>, {'a': 1, 'b': 1})
# AFTER PASS 1 defaultdict(<class 'int'>, {'a': 0, 'b': 1})
# I 1 J -1
# REMOVING FROM CF FOR I
# FOUND ANAGRAM AT 0
# I 2 J 0
# ADDING TO CF FOR J
# REMOVING FROM CF FOR I
# FOUND ANAGRAM AT 1
# I 3 J 1
# ADDING TO CF FOR J
# REMOVING FROM CF FOR I
# FOUND ANAGRAM AT 2