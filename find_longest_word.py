import collections
import sys
import unittest


class FindLongestWordInString(unittest.TestCase):
    """
    Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

    Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W,
    without reordering the remaining characters.

    Note: D can appear in any format (list, hash table, prefix tree, etc.

    For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"}
    the correct output would be "apple"

    The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
    The word "bale" is not a subsequence of S because even though S has all the right letters,
    they are not in the right order.
    The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
    """

    def find_longest_word_in_string(self, letters, words):
        letter_positions = collections.defaultdict(list)
        # For each letter in 'letters', collect all the indices at which it appears.
        # O(#letters) space and speed.
        for index, letter in enumerate(letters):
            letter_positions[letter].append(index)
        # For words, in descending order by length since we are looking for the longest word
        # Bails out early on first matched word, and within word on impossible letter/position combinations,
        # but worst case is O(#words # avg-len) * O(#letters / 26) time; constant space.
        for word in sorted(words, key=lambda w: len(w), reverse=True):
            print("CHECKING {}".format(word))
            pos = 0
            for letter in word:
                if letter not in letter_positions:
                    break
            # Find any remaining valid positions in search string where this letter appears.
            # It would be better to do this with binary search, but this is very Python-ic.
            possible_positions = [p for p in letter_positions[letter] if p >= pos]
            if not possible_positions:
                print("NO POSSIBLE POSITIONS")
                continue
            pos = possible_positions[0] + 1
            print(str(possible_positions))
            # We didn't break out of the loop, so all letters have valid positions
            if word is not None:
                return word
            else:
                print("NOTHING")


    def test_lw(self):
        d = {"able", "ale", "apple", "bale", "kangaroo"}
        word = "abppplee"
        self.assertEqual(self.find_longest_word_in_string(word, d), "apple")