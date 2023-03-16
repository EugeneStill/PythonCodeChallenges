import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLReverse(unittest.TestCase):
# reverse linked list and return new head

    def reverse_ll_iterative(self, head):
        if not head or not head.next:
            return head
        prev, cur = None, head
        # point cur.next to prev and move prev, cur up to cur, cur.next
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


    def reverse_ll_recursive(self, head):
        if not head or not head.next:
            return head
        node = self.reverse_ll_recursive(head.next)
        print("made recursive call")
        head.next.next = head
        head.next = None
        return node


    def test_reverse_ll(self):
        input_list = [1, 2, 3, 4, 5]
        ll = linked_list.LinkedList()
        ll.create_linked_list(input_list)
        self.assertEqual(self.reverse_ll_iterative(ll.head).val, 5)
        ll_2 = linked_list.LinkedList()
        ll_2.create_linked_list(input_list)
        self.assertEqual(self.reverse_ll_recursive(ll_2.head).val, 5)






