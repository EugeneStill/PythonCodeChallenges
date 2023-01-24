import unittest

class GroupAnagrams(unittest.TestCase):
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
    """

    def group_anagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in dic:
                dic[ss].append(s)
            else:
                dic[ss] = [s]
        return dic.values()

    def test_anagram_groups(self):
        l1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
        res1 =  [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        l2 = [""]
        res2 = [[""]]
        l3 = ["a"]
        res3 =[["a"]]
        self.assertTrue(self.group_anagrams(l1), res1)
        self.assertTrue(self.group_anagrams(l2), res2)
        self.assertTrue(self.group_anagrams(l3), res3)




