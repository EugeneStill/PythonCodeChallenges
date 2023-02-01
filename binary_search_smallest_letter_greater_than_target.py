import unittest


class NextGreatestLetter(unittest.TestCase):
    def next_greatest_letter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        # if the number is out of bound
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        low = 0
        high = len(letters) - 1
        while low <= high:
            mid = (high + low) // 2

            # use >= instead of just > since we want to find the first character greater than target
            if target >= letters[mid]:
                low = mid + 1

            if target < letters[mid]:
                high = mid - 1

        return letters[low]

    def test_ngl(self):
        self.assertEqual(self.next_greatest_letter(["c","f","j"], "c"), "f")
        self.assertEqual(self.next_greatest_letter(["c", "f", "j"], "a"), "c")
        self.assertEqual(self.next_greatest_letter(["c", "f", "j"], "z"), "c")