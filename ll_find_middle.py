import unittest

import helpers.linked_list as linked_list
class MiddleNode(unittest.TestCase):
    """
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.
    """
    def middle_node(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head

    def test_mid(self):
        l1_input = [1, 2, 3, 4, 5]
        l2_input = [1, 2, 3, 4, 5, 6]
        ll1 = linked_list.LinkedList()
        ll2 = linked_list.LinkedList()
        ll1.create_linked_list(l1_input)
        ll2.create_linked_list(l2_input)
        self.assertEqual(self.middle_node(ll1.head).val, 3)
        self.assertEqual(self.middle_node(ll2.head).val, 4)