import unittest
import collections


class MinWindow(unittest.TestCase):
    """
    Given 2 strings s & t of lengths m and n, return the minimum window substring of s such that every character in t
    (including duplicates) is included in the window. If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.
    s and t consist of uppercase and lowercase English letters

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    """
    def min_window(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start, min_window, chars_needed = 0, '', len(t)
        char_count = {}
        for c in t:
            char_count[c] = char_count.get(c, 0)+ 1

        # print("\n" + s)
        # set end pointer to loop from start of string to end
        for end in range(len(s)):
            # print("CHECKING END {}".format(end))
            if char_count.get(s[end], 0) > 0:
                chars_needed -= 1
            if s[end] in char_count.keys():
                char_count[s[end]] -= 1

            print('CHAR COUNT DIC',char_count)
            # any time we don't need more characters for substring then see if we can shorten min_window
            # update chars needed (if found) & move start forward
            while chars_needed == 0:
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
                    min_window = s[start:end + 1]
                    # print("MIN WINDOW {}".format(min_window))

                if s[start] in char_count.keys():
                    char_count[s[start]] += 1
                if char_count.get(s[start], 0) > 0:
                    chars_needed += 1
                start += 1
                # print('START {} END {} TOTAL CHARS NEEDED {}'.format(start, end, chars_needed))

        return min_window

    def test_min_win(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        output = "BANC"
        self.assertEqual(self.min_window(s, t), output)

