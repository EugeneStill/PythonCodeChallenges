import unittest


class MyAtoi(unittest.TestCase):
    """
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

    The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'.
    Read this character in if it is either. This determines if the final result is negative or positive respectively.
    Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached.
    The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
    If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp it so that it remains in the range.
    Integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.
    Note:
    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
    """
    def my_atoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        MAX_NUM = 2 ** 31 - 1  # 2147483647 (8 is why we check curr_digit > 7 below)
        MIN_NUM = -2 ** 31

        # trim the leading white space first
        s = s.strip()
        sign = 1
        index = 0
        num = 0
        if not s:
            return num

        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        while index < len(s) and s[index].isdigit():
            curr_digit = int(s[index])
            # could use ord instead of int
            # curr_digit = ord(s[index]) - ord('0')  # use ord 0 to get expected int value
            # ('0', 48), ('1', 49), ('2', 50), ('3', 51), ('4', 52),
            # ('5', 53), ('6', 54), ('7', 55), ('8', 56), ('9', 57)

            if num > MAX_NUM // 10 or (num == MAX_NUM // 10 and curr_digit > 7):
                return MAX_NUM if sign == 1 else MIN_NUM
            num = num * 10 + curr_digit
            index += 1

        num = sign * num
        return num

    def test_string_to_num(self):
        self.assertEqual(self.my_atoi("-42"), -42)
        self.assertEqual(self.my_atoi("   +42"), 42)
        self.assertEqual(self.my_atoi("   +42with words"), 42)
        self.assertEqual(self.my_atoi("8147483648"), 2147483647)
        self.assertEqual(self.my_atoi("-8147483648"), -2147483648)
