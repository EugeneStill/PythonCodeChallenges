import unittest

class PlusOne(unittest.TestCase):
    """
    for a number represented by the elements of a list,
    add 1 to that number and return the new number in a similarly formatted list
    """
    def plus_one(self, digits):
        """
        :type digits: list[int]
        :rtype: list[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits) - 1 - i)
        return [int(i) for i in str(num + 1)]

    def test_plus_one(self):
        input_list = [9]
        output_list = [1,0]
        input_list1 = [4,3,2,1]
        output_list2 = [4,3,2,2]
        self.assertEqual(self.plus_one(input_list), output_list)
        self.assertEqual(self.plus_one(input_list1), output_list2)
