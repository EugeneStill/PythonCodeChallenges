import unittest
import helpers.linked_list as linked_list

class SwapPairs(unittest.TestCase):
    """
    Given a linked list, swap every two adjacent nodes and return its head.
    Do not modify the values in the list's nodes (i.e., only nodes themselves may be changed.)

    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
    """
    def swap_pairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swap_pairs(second.next)
        second.next = head
        return second

    def test_swap_pairs(self):
        ll = linked_list.LinkedList()
        ll.create_linked_list([1,2,3,4])
        self.assertEqual(self.swap_pairs(ll.head).val, 2)