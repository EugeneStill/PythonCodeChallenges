import unittest
import helpers.trie as trie

class TrieReplaceWords(unittest.TestCase):
    """if prefix from dictionary found in word in sentence then replace that word with its prefix"""
    def replace_words(self, dictionary, sentence):
        sentence = sentence.split()
        t = trie.Trie()
        for dic in dictionary:
            t.insert(dic)

        mapping = {}

        for s in set(sentence):
            mapping[s] = t.replace_with(s)

        for i, s in enumerate(sentence):
            sentence[i] = mapping[s]

        return " ".join(sentence)

    def test_replace_words(self):
        dictionary_1 = ["cat","bat","rat"]
        sentence_1 = "the cattle was rattled by the battery"
        result_1 = "the cattle was rat by the bat"
        dictionary_2 = ["gnat","bat","rat"]
        sentence_2 = "the cattle was rattled by the battery"
        result_2 = "the cattle was rat by the bat"
        self.assertTrue(self.replace_words(dictionary_1, sentence_1), result_1)
        self.assertTrue(self.replace_words(dictionary_2, sentence_2), result_2)



