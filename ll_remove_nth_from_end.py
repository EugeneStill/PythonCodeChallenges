import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLRemoveNthFromEnd(unittest.TestCase):

    def remove_nth_from_end(self, head, n):
        # given the head of a linked list, remove the nth node from the end of the list and return its head.
        # Constraints:
        # The number of nodes in the list is sz.
        # 1 <= sz <= 30
        # 0 <= Node.val <= 100
        # 1 <= n <= sz
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        # handle cases where original head needs to be removed
        if not fast:
            return None
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    def test_is_ll_odd(self):
        input_list = [2, 4, 5, 7, 8]
        ll = linked_list.LinkedList()
        ll.create_linked_list(input_list)
        self.assertEqual(self.remove_nth_from_end(ll.head, 2), ll.head)
        input_list_2 = [2, 4]
        ll_2 = linked_list.LinkedList()
        ll_2.create_linked_list(input_list_2)
        self.assertEqual(self.remove_nth_from_end(ll_2.head, 2), None)







