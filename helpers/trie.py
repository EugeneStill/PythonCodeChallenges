class TreeNode:
    def __init__(self, val, children=None, isEnd=False):
        self.val = val
        self.children = children
        self.isEnd = isEnd


class Trie:
    def __init__(self):
        self.root = TreeNode("", {})

    def insert(self, string):
        root = self.root
        for c in string:
            if c not in root.children:
                root.children[c] = TreeNode(c, {})
            root = root.children[c]
        root.isEnd = True

    def replace_with(self, string):
        """if prefix is in trie and is a prefix of the string then replace string with prefix"""
        root = self.root
        prefix = root.val
        for c in string:
            if c not in root.children:
                return string
            if root.children[c].isEnd:
                prefix = prefix + root.children[c].val
                return prefix
            prefix = prefix + root.children[c].val
            root = root.children[c]
        return prefix