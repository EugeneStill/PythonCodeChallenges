import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLRemoveAllOccurrences(unittest.TestCase):

    def test_ll_rao(self, val=10):
        ll = linked_list.LinkedList()
        ll.create_linked_list([10, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        while ll.head and ll.head.val == val:
            ll.head = ll.head.next

        current = ll.head

        # Second loop
        while current:
            while current and current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next
        ll.print()
        return ll.head


