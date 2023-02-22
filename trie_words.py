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
        # for each char in word
        for c in word:
            # if char is not already in the children of the node
            if c not in node.children:
                # add a new TrieNode to the children of the node for the character
                node.children[c] = TrieNode()
            # update node to be the char node in the current node's children
            node = node.children[c]
        node.word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.word

    def starts_with(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
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