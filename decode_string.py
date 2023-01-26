import unittest

class DecodeString(unittest.TestCase):
    """
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
    Note that k is guaranteed to be a positive integer.

    You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
    Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
    For example, there will not be input like 3a or 2[4].

    Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

    Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

    Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
    """
    def decode_string(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []; cur_num = 0; cur_string = ''
        for c in s:
            if c == '[':
                # each time a new bracket opens, put cur_string & cur_num on stack then reset values
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = ''
                cur_num = 0
            elif c == ']':
                # when bracket closes pop the num and prev_string from stack then update cur_string
                num = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + num*cur_string
            elif c.isdigit():
                # use multiplication to handle digits > 1 char in length
                cur_num = cur_num*10 + int(c)
            else:
                # increment string while c is not digit or bracket
                cur_string += c
        return cur_string


    def test_min_stack(self):
        s = "3[a12[c]]"
        self.assertEqual(self.decode_string(s), "accccccccccccaccccccccccccacccccccccccc")
        s = "3[a2[c]]"
        self.assertEqual(self.decode_string(s), "accaccacc")
        s = "2[abc]3[cd]ef"
        self.assertEqual(self.decode_string(s), "abcabccdcdcdef")





