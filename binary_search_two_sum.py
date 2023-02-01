import unittest


class TwoSumBinarySearch(unittest.TestCase):
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
    find two numbers such that they add up to a specific target number.
    Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2].

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
    """

    def two_sum(self, numbers, target):
        """
        binary search approach, but still think 2 pointers is more efficient
        """
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = (r+l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1

    def test_two_sum(self):
        self.assertEqual(self.two_sum([2,7,11,15], 9), [1,2])