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
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if len(digits) == 0:
            return res
        print("\n")
        self.dfs(digits, 0, '', res, dic)
        return res

    def dfs(self, digits, index, path, res, dic):
        if index >= len(digits):
            res.append(path)
            print("ADDED {} TO RES".format(path))
            return
        string1 = dic[digits[index]]
        for c in string1:
            print("STR {} IDX+1 {} PATH+c {} RES {}".format(string1, index+1, path+c, str(res)))
            self.dfs(digits, index + 1, path + c, res, dic)

    def test_letter_combinations(self):
        expected = sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertEqual(sorted(self.letter_combinations("23")), expected)

# LOGGING
# STR abc IDX+1 1 PATH+c a RES []
# STR def IDX+1 2 PATH+c ad RES []
# ADDED ad TO RES
# STR def IDX+1 2 PATH+c ae RES ['ad']
# ADDED ae TO RES
# STR def IDX+1 2 PATH+c af RES ['ad', 'ae']
# ADDED af TO RES
# STR abc IDX+1 1 PATH+c b RES ['ad', 'ae', 'af']
# STR def IDX+1 2 PATH+c bd RES ['ad', 'ae', 'af']
# ADDED bd TO RES
# STR def IDX+1 2 PATH+c be RES ['ad', 'ae', 'af', 'bd']
# ADDED be TO RES
# STR def IDX+1 2 PATH+c bf RES ['ad', 'ae', 'af', 'bd', 'be']
# ADDED bf TO RES
# STR abc IDX+1 1 PATH+c c RES ['ad', 'ae', 'af', 'bd', 'be', 'bf']
# STR def IDX+1 2 PATH+c cd RES ['ad', 'ae', 'af', 'bd', 'be', 'bf']
# ADDED cd TO RES
# STR def IDX+1 2 PATH+c ce RES ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd']
# ADDED ce TO RES
# STR def IDX+1 2 PATH+c cf RES ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce']
# ADDED cf TO RES