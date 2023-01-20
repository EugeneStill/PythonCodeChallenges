import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLReorderOddEnd(unittest.TestCase):

    def reorder_linked_list(self, head):
    # Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices,
    # and return the reordered list.
    # The first node is considered odd, and the second node is even, and so on.
    # Note that the relative order inside both the even and odd groups should remain as it was in the input.
        if not head:
            return head

        odd = head
        even = head.next
        # keep track of start of even links
        e_head = even

        while even and even.next:
            # relink pointers for each section of the list
            odd.next = odd.next.next
            even.next = even.next.next
            # keep going with next odd & even numbers
            odd = odd.next
            even = even.next

        # point end of odd link to start of even link
        odd.next = e_head
        return head

    def test_is_ll_odd(self):
        input_list = [2, 4, 5, 7, 8, 9]
        expected_list = [2, 5, 8, 4, 7, 9]
        ll = linked_list.LinkedList()
        ll.create_linked_list(input_list)
        new_head = self.reorder_linked_list(ll.head)
        print("got new head")
        result_list = [new_head.value]
        current = new_head
        while current.next:
            result_list.append(current.next.value)
            current = current.next
        self.assertEqual(expected_list, result_list)







