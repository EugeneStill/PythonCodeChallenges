# Selection sort in Python
# time complexity O(n*n)
# sorting by finding min_index
import unittest


class SelectionSort(unittest.TestCase):
    """
    The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

    1) The subarray which is already sorted.

    2) Remaining subarray which is unsorted. In every iteration of selection sort,
    the minimum element (considering ascending order) from the unsorted subarray is picked & moved to sorted subarray.
    """

    def selection_sort(self, array):
        size = len(array)
        print("\n" + str(array))
        for ind in range(size):
            print("\nCHECKING IND {}".format(ind))
            min_index = ind

            for j in range(ind + 1, size):
                print("CHECKING J {}".format(j))
                # select the minimum element in every iteration
                if array[j] < array[min_index]:
                    print("SETTING MIN INDEX AS J {}".format(j))
                    min_index = j
            # swapping the elements to sort the array
            (array[ind], array[min_index]) = (array[min_index], array[ind])
            print(str(array))
        return array


    def test_ss(self):
        arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
        output = [-202, -97, -9, -2, 0, 11, 45, 88, 747]
        self.assertEqual(self.selection_sort(arr), output)

# LOGGING
# [-2, 45, 0, 11, -9, 88, -97, -202, 747]
#
# CHECKING IND 0
# CHECKING J 1
# CHECKING J 2
# CHECKING J 3
# CHECKING J 4
# SETTING MIN INDEX AS J 4
# CHECKING J 5
# CHECKING J 6
# SETTING MIN INDEX AS J 6
# CHECKING J 7
# SETTING MIN INDEX AS J 7
# CHECKING J 8
# [-202, 45, 0, 11, -9, 88, -97, -2, 747]
#
# CHECKING IND 1
# CHECKING J 2
# SETTING MIN INDEX AS J 2
# CHECKING J 3
# CHECKING J 4
# SETTING MIN INDEX AS J 4
# CHECKING J 5
# CHECKING J 6
# SETTING MIN INDEX AS J 6
# CHECKING J 7
# CHECKING J 8
# [-202, -97, 0, 11, -9, 88, 45, -2, 747]
#
# CHECKING IND 2
# CHECKING J 3
# CHECKING J 4
# SETTING MIN INDEX AS J 4
# CHECKING J 5
# CHECKING J 6
# CHECKING J 7
# CHECKING J 8
# [-202, -97, -9, 11, 0, 88, 45, -2, 747]
#
# CHECKING IND 3
# CHECKING J 4
# SETTING MIN INDEX AS J 4
# CHECKING J 5
# CHECKING J 6
# CHECKING J 7
# SETTING MIN INDEX AS J 7
# CHECKING J 8
# [-202, -97, -9, -2, 0, 88, 45, 11, 747]
#
# CHECKING IND 4
# CHECKING J 5
# CHECKING J 6
# CHECKING J 7
# CHECKING J 8
# [-202, -97, -9, -2, 0, 88, 45, 11, 747]
#
# CHECKING IND 5
# CHECKING J 6
# SETTING MIN INDEX AS J 6
# CHECKING J 7
# SETTING MIN INDEX AS J 7
# CHECKING J 8
# [-202, -97, -9, -2, 0, 11, 45, 88, 747]
#
# CHECKING IND 6
# CHECKING J 7
# CHECKING J 8
# [-202, -97, -9, -2, 0, 11, 45, 88, 747]
#
# CHECKING IND 7
# CHECKING J 8
# [-202, -97, -9, -2, 0, 11, 45, 88, 747]
#
# CHECKING IND 8
# [-202, -97, -9, -2, 0, 11, 45, 88, 747]