import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class IsLLOdd(unittest.TestCase):

    def is_ll_odd(self, input_list):
        # is linked list length odd
        ll = linked_list.LinkedList()
        ll.create_linked_list(input_list)
        count = 1
        current = ll.head
        while current.next:
            count += 1
            current = current.next
        return count % 2

    def test_is_ll_odd(self):
        self.assertEqual(self.is_ll_odd([1]), 1)
        self.assertEqual(self.is_ll_odd([1, 2]), 0)
        self.assertEqual(self.is_ll_odd([1, 2, 3]), 1)
        self.assertEqual(self.is_ll_odd([1, 2, 3, 4]), 0)


