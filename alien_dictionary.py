from collections import defaultdict
from typing import List


class Solution:
    """
    Suppose you are given a list of strings words and a string order.
    You need to determine if the given words are sorted lexicographically according to the given order.
    You can assume that no two words are the same.

    Order is a string of unique lowercase English letters.
    You can assume that order has length at most 26, and that no character of order appears in words.
    Order is given by the relation that a < b means letter a comes before letter b in order.

    words = ["wrt","wrf","er","ett","rftt"]
    order = "wertf"
    True
    """
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        graph = defaultdict(set)

        # Create graph
        for i in range(len(order)):
            if i < len(order) - 1:
                graph[order[i]].add(order[i + 1])

        # Perform topological sort
        visited = set()
        order = []

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            order.append(node)

        for node in graph:
            if node not in visited:
                dfs(node)

        order.reverse()

        # Check if words are sorted lexicographically
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order.index(word1[j]) > order.index(word2[j]):
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False

        return True