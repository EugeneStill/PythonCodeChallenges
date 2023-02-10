import unittest


class LetterCombinations(unittest.TestCase):
    """
    Given a string of digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    Return the answer in any order.

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    """
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if len(digits) == 0:
            return res

        self.dfs(digits, 0, '', res)
        return res

    def dfs(self, digits, index, path, res):
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if index >= len(digits):
            res.append(path)
            return
        string1 = dic[digits[index]]
        for c in string1:
            self.dfs(digits, index + 1, path + c, res)

    def test_letter_combinations(self):
        expected = sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertEqual(sorted(self.letter_combinations("23")), expected)

# LOGGING
# GOT DFS FOR NUMS 23 IDX 0 RES []
# STRING abc
# MAKING DFS CALL FOR a
#
# GOT DFS FOR NUMS 23 IDX 1 RES []
# STRING def
# MAKING DFS CALL FOR d
#
# GOT DFS FOR NUMS 23 IDX 2 RES []
# UPDATING RES
# MAKING DFS CALL FOR e
#
# GOT DFS FOR NUMS 23 IDX 2 RES ['ad']
# UPDATING RES
# MAKING DFS CALL FOR f
#
# GOT DFS FOR NUMS 23 IDX 2 RES ['ad', 'ae']
# UPDATING RES
# MAKING DFS CALL FOR b
#
# GOT DFS FOR NUMS 23 IDX 1 RES ['ad', 'ae', 'af']
# STRING def
# MAKING DFS CALL FOR d
#
# GOT DFS FOR NUMS 23 IDX 2 RES ['ad', 'ae', 'af']
# UPDATING RES
# MAKING DFS CALL FOR e
#
# GOT DFS FOR NUMS 23 IDX 2 RES ['ad', 'ae', 'af', 'bd']
# UPDATING RES
# MAKING DFS CALL FOR f
#
# GOT DFS FOR NUMS 23 IDX 2 RES ['ad', 'ae', 'af', 'bd', 'be']
# UPDATING RES
# MAKING DFS CALL FOR c
#
# GOT DFS FOR NUMS 23 IDX 1 RES ['ad', 'ae', 'af', 'bd', 'be', 'bf']
# STRING def
# MAKING DFS CALL FOR d
#
# GOT DFS FOR NUMS 23 IDX 2 RES ['ad', 'ae', 'af', 'bd', 'be', 'bf']
# UPDATING RES
# MAKING DFS CALL FOR e
#
# GOT DFS FOR NUMS 23 IDX 2 RES ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd']
# UPDATING RES
# MAKING DFS CALL FOR f
#
# GOT DFS FOR NUMS 23 IDX 2 RES ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce']
# UPDATING RES
