import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLReverse(unittest.TestCase):
# reverse linked list and return new head

    def reverse_ll_iterative(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


    def reverse_ll_recursive(self, head):
        if not head or not head.next:
            return head
        node = self.reverse_ll_recursive(head.next)
        print("made recursive call")
        head.next.next = head
        head.next = None
        return node


    def test_is_ll_odd(self):
        input_list = [1, 2, 3, 4, 5]
        ll = linked_list.LinkedList()
        ll.create_linked_list(input_list)
        self.assertEqual(self.reverse_ll_iterative(ll.head).value, 5)
        ll_2 = linked_list.LinkedList()
        ll_2.create_linked_list(input_list)
        self.assertEqual(self.reverse_ll_recursive(ll_2.head).value, 5)






