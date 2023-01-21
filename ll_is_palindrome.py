import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLPalindrome(unittest.TestCase):

    def is_ll_palindrome(self, head):
        # are values of linked list a palindrome
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        back_node = None
        # consider renaming the while loop variables for clarity
        while slow:
            nxt = slow.next
            slow.next = back_node
            back_node = slow
            slow = nxt
        # compare the first and second half nodes
        while back_node: # while node and head:
            if back_node.value != head.value:
                return False
            back_node = back_node.next
            head = head.next
        return True


    def test_is_ll_palindrome(self):
        pal_list = linked_list.LinkedList()
        one_val_list = linked_list.LinkedList()
        not_pal_list = linked_list.LinkedList()
        pal_list.create_linked_list([1, 2, 3, 2, 1])
        one_val_list.create_linked_list([1])
        not_pal_list.create_linked_list([1, 2, 3, 2, 4])
        self.assertTrue(self.is_ll_palindrome(pal_list.head))
        self.assertTrue(self.is_ll_palindrome(one_val_list.head))
        self.assertFalse(self.is_ll_palindrome(not_pal_list.head))







