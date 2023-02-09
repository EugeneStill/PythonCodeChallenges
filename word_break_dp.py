import unittest


class WordBreak(unittest.TestCase):
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented
    into a space-separated sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.

    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false

    """
    def word_break(self, s, words):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp
        d = [False] * len(s)
        for i in range(len(s)):
            for w in words:
                # does current word at end at i
                # (AND was index before i True (meaning a valid word ended right before i)
                # OR is i beginning of list (meaning its ok that there was no valid word before it))
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]

    def test_word_break(self):
        words = ["cats","dog","sand","and","cat", "pen", "apple"]
        good_string = "applepenapple"
        bad_string = "catsandog"
        self.assertTrue(self.word_break(good_string, words))
        self.assertFalse(self.word_break(bad_string, words))


