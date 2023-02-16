import collections
import unittest


class FindWordSquares(unittest.TestCase):
    """
    A “word square” is an ordered sequence of K different words of length K that, when written one word per line,
    reads the same horizontally and vertically. For example:
    BALL
    AREA
    LEAD
    LADY

    First, design a way to return true if a given sequence of words is a word square.

    Second, given an arbitrary list of words, return all the possible word squares it contains. Reordering is allowed.

    For example, the input list

    [AREA, BALL, DEAR, LADY, LEAD, YARD]

    should output

    [(BALL, AREA, LEAD, LADY), (LADY, AREA, DEAR, YARD)]

    Finishing the first task should help you accomplish the second task.
    """
def find_word_squares(words):
    # Preprocess words: O(#words * word-length) time and space
    words_by_letter_position = collections.defaultdict(set)
    for word in words:
        for index, letter in enumerate(word):
            words_by_letter_position[(index,letter)].add(word)
    # For each word, see if we can make a square.  O(#words * word-length^2/2)
    for word in words:
        # Initialize a set of incomplete possible squares;
        # each item is an N-tuple of words that are valid but incomplete word squares.
        possible_squares = set([(word,)])
    # As long as we have any incomplete squares:
    while possible_squares:
        square = possible_squares.pop()
        # When matching an incomplete square with N words already present,
        # we need to match any prospective words to the tuples formed by
        # (N, Nth character in word 0), (N, Nth character in word 1), ...
        # Only words which satisfy all of those restrictions can be added.
        keys = [(i, square[i][len(square)]) for i in range(len(square))]
        possible_matches = [words_by_letter_position[key] for key in keys]
        for valid_word in set.intersection(*possible_matches):
            valid_square = square + (valid_word,)
            # Save valid square in 'ret' if it's complete, or save it as a work-to-do item if it's not.
            if len(valid_square) == len(word):
                yield valid_square
            else:
                possible_squares.add(valid_square)



# if __name__ == '__main__':
#     for square in find_word_squares(sys.argv[1:]):
#         print '
# '.join(square)
#         print