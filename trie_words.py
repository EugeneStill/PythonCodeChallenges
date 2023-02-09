import unittest


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word = False
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode()
    def __repr__(self):
        def recur(node, indent):
            return "".join(indent + key + ("$" if child.word else "")
                                  + recur(child, indent + "  ")
                for key, child in node.children.items())
        return recur(self.root, "\n")
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word

    def starts_with(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True

class test_trie(unittest.TestCase):

    def test_trie(self):
        t = Trie()
        t.insert("apple")
        t.insert("arrow")
        t.insert("bring")
        t.insert("brush")
        t.insert("bred")
        t.insert("bread")
        t.starts_with("add")
        # print(str(t.root.children.keys()))
        self.assertTrue(t.starts_with("arr"))
        self.assertFalse(t.search("array"))
        self.assertTrue(t.search("apple"))


# LOGGING
# test_trie dict_keys(['a', 'b'])
# a
#   p
#     p
#       l
#         e$
#   r
#     r
#       o
#         w$
# b
#   r
#     i
#       n
#         g$
#     u
#       s
#         h$
#     e
#       d$
#       a
#         d$