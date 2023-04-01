import unittest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end_of_word

class WordBreak(unittest.TestCase):
    def word_break(self, s, wordDict):
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and trie.search(s[j:i]):
                    dp[i] = True
                    break

        return dp[n]

    def test_word_break(self):
        words = ["cats","dog","sand","and","cat", "pen", "apple"]
        good_string = "applepenapple"
        bad_string = "catsandog"
        self.assertTrue(self.word_break(good_string, words))
        self.assertFalse(self.word_break(bad_string, words))


