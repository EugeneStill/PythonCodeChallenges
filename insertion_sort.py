import unittest


class InsertionSort(unittest.TestCase):
    """
    CHECKING I 1
    UPDATED ARR [12, 12, 13, 5, 6]
    UPDATED ARR [11, 12, 13, 5, 6]

    CHECKING I 2
    UPDATED ARR [11, 12, 13, 5, 6]

    CHECKING I 3
    UPDATED ARR [11, 12, 13, 13, 6]
    UPDATED ARR [11, 12, 12, 13, 6]
    UPDATED ARR [11, 11, 12, 13, 6]
    UPDATED ARR [5, 11, 12, 13, 6]

    CHECKING I 4
    UPDATED ARR [5, 11, 12, 13, 13]
    UPDATED ARR [5, 11, 12, 12, 13]
    UPDATED ARR [5, 11, 11, 12, 13]
    UPDATED ARR [5, 6, 11, 12, 13]
    """
    def insertion_sort(self, arr):
        arr_len = len(arr)
        if arr_len <= 1:
            return

        for i in range(1, arr_len):
            print("\nCHECKING I {}".format(i))
            target = arr[i]
            # Move elements that are greater than target, to one position ahead of their current position
            j = i - 1
            while j >= 0 and target < arr[j]:
                arr[j + 1] = arr[j]
                print("UPDATED ARR {}".format(str(arr)))
                j -= 1
            arr[j + 1] = target
            print("UPDATED ARR {}".format(str(arr)))
        return arr

    def test_insertion_sort(self):
        arr = [12, 11, 13, 5, 6]
        output = [5, 6, 11, 12, 13]
        self.assertEqual(self.insertion_sort(arr), output)