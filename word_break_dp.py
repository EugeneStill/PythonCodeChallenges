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
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in words:
                # does current word end at i
                # (AND dp[idx_before_word] is True (meaning a valid word ended right before this word)
                # OR idx_before_word == -1 (meaning its ok that there was no valid word before it))
                idx_before_word = i - len(w)
                if w == s[idx_before_word + 1:i + 1] and (dp[idx_before_word] or idx_before_word == -1):
                    dp[i] = True
        return dp[-1]

    def test_word_break(self):
        words = ["cats","dog","sand","and","cat", "pen", "apple"]
        good_string = "applepenapple"
        bad_string = "catsandog"
        self.assertTrue(self.word_break(good_string, words))
        self.assertFalse(self.word_break(bad_string, words))


