import unittest
import collections


class LadderLength(unittest.TestCase):
    """
    A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
    beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
    Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
    transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
    """
    def ladder_length(self, begin_word, end_word, word_list):
        """
        :type begin_word: str
        :type end_word: str
        :type word_list: List[str]
        :rtype: int
        """
        word_list = set(word_list)
        char_set = {w for word in word_list for w in word}
        queue = collections.deque([[begin_word, 1]])
        while queue:
            word, length = queue.popleft()
            print("\nWORD: {} LEN: {}".format(word, length))
            if word == end_word:
                return length
            for i in range(len(word)):
                for c in char_set:
                    next_word = word[:i] + c + word[i+1:]
                    print("CHECKING {}".format(next_word))
                    if next_word in word_list:
                        print("REMOVED {}".format(next_word))
                        word_list.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

    def test_ladder_lengh(self):
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(self.ladder_length(begin_word, end_word, word_list), 5)

# LOGGING
# WORD: hit LEN: 1
# CHECKING hit
# CHECKING dit
# CHECKING oit
# CHECKING cit
# CHECKING tit
# CHECKING lit
# CHECKING git
# CHECKING hht
# CHECKING hdt
# CHECKING hot
# REMOVED hot
# CHECKING hct
# CHECKING htt
# CHECKING hlt
# CHECKING hgt
# CHECKING hih
# CHECKING hid
# CHECKING hio
# CHECKING hic
# CHECKING hit
# CHECKING hil
# CHECKING hig
#
# WORD: hot LEN: 2
# CHECKING hot
# CHECKING dot
# REMOVED dot
# CHECKING oot
# CHECKING cot
# CHECKING tot
# CHECKING lot
# REMOVED lot
# CHECKING got
# CHECKING hht
# CHECKING hdt
# CHECKING hot
# CHECKING hct
# CHECKING htt
# CHECKING hlt
# CHECKING hgt
# CHECKING hoh
# CHECKING hod
# CHECKING hoo
# CHECKING hoc
# CHECKING hot
# CHECKING hol
# CHECKING hog
#
# WORD: dot LEN: 3
# CHECKING hot
# CHECKING dot
# CHECKING oot
# CHECKING cot
# CHECKING tot
# CHECKING lot
# CHECKING got
# CHECKING dht
# CHECKING ddt
# CHECKING dot
# CHECKING dct
# CHECKING dtt
# CHECKING dlt
# CHECKING dgt
# CHECKING doh
# CHECKING dod
# CHECKING doo
# CHECKING doc
# CHECKING dot
# CHECKING dol
# CHECKING dog
# REMOVED dog
#
# WORD: lot LEN: 3
# CHECKING hot
# CHECKING dot
# CHECKING oot
# CHECKING cot
# CHECKING tot
# CHECKING lot
# CHECKING got
# CHECKING lht
# CHECKING ldt
# CHECKING lot
# CHECKING lct
# CHECKING ltt
# CHECKING llt
# CHECKING lgt
# CHECKING loh
# CHECKING lod
# CHECKING loo
# CHECKING loc
# CHECKING lot
# CHECKING lol
# CHECKING log
# REMOVED log
#
# WORD: dog LEN: 4
# CHECKING hog
# CHECKING dog
# CHECKING oog
# CHECKING cog
# REMOVED cog
# CHECKING tog
# CHECKING log
# CHECKING gog
# CHECKING dhg
# CHECKING ddg
# CHECKING dog
# CHECKING dcg
# CHECKING dtg
# CHECKING dlg
# CHECKING dgg
# CHECKING doh
# CHECKING dod
# CHECKING doo
# CHECKING doc
# CHECKING dot
# CHECKING dol
# CHECKING dog
#
# WORD: log LEN: 4
# CHECKING hog
# CHECKING dog
# CHECKING oog
# CHECKING cog
# CHECKING tog
# CHECKING log
# CHECKING gog
# CHECKING lhg
# CHECKING ldg
# CHECKING log
# CHECKING lcg
# CHECKING ltg
# CHECKING llg
# CHECKING lgg
# CHECKING loh
# CHECKING lod
# CHECKING loo
# CHECKING loc
# CHECKING lot
# CHECKING lol
# CHECKING log
#
# WORD: cog LEN: 5