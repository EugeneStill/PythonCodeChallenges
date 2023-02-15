import unittest


class QuickSort(unittest.TestCase):
    """
    QuickSort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around
    the picked pivot. There are many different versions of quickSort that pick pivot in different ways:

    Always pick the first element as a pivot
    Always pick the last element as a pivot
    Pick a random element as a pivot
    Pick median as a pivot

    Here we will be picking the last element as a pivot. The key process in quickSort is partition().
    Target of partitions is, given an array and an element ‘x’ of array as a pivot, put x at its correct position
    in a sorted array and put all smaller elements (smaller than x) before x, and put all greater elements
    (greater than x) after x. All this should be done in linear time.

    This implementation utilizes pivot as the last element in the nums list
    It has a pointer to keep track of the elements smaller than the pivot
    At the very end of partition() function, the pointer is swapped with the pivot
    to come up with a "sorted" nums relative to the pivot

    """


    def partition(self, array, low, high):
        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements & compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # If element smaller than pivot, increment i then swap smaller element with the greater element at new i
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
                print(str(array))

        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        print(str(array))

        # Return the position from where partition is done
        return i + 1

    def quick_sort(self, array, low, high):
        print("LOW {} HIGH {}".format(low, high))
        if low < high:
            # Find pivot element where element smaller than pivot are on the left
            # element greater than pivot are on the right
            pivot = self.partition(array, low, high)

            # Recursive call on the left of pivot
            self.quick_sort(array, low, pivot - 1)

            # Recursive call on the right of pivot
            self.quick_sort(array, pivot + 1, high)
        return array


    def test_quick_sort(self):
        input = [1, 7, 4, 1, 10, 9, -2]
        output = [-2, 1, 1, 4, 7, 9, 10]
        print("\n" + str(input))
        self.assertEqual(self.quick_sort(input, 0, 6), output)



