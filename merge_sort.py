import unittest

class MergeSort(unittest.TestCase):

    def merge_sort(self, myList):
        print("\n{}".format(str(myList)))
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            # Recursive call on each half
            self.merge_sort(left)
            self.merge_sort(right)

            # 2 iterators for traversing the two halves & 1 iterator for traversing the whole list
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # The value from the left half has been used
                    myList[k] = left[i]
                    # Move the iterator forward
                    i += 1
                    print("UPDATED I {}".format(str(myList)))
                else:
                    myList[k] = right[j]
                    j += 1
                    print("UPDATED J {}".format(str(myList)))
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1
                print("UPDATING REMAINING LEFT {}".format(str(myList)))
            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1
                print("UPDATING REMAINING RIGHT {}".format(str(myList)))

    def test_ms(self):
        myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.merge_sort(myList)
        print(myList)