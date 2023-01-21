import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class AddNumbers(unittest.TestCase):
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807
    """

    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # dummy will point to start of new list, cur will build the new list
        dummy = cur = nd.Node(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = nd.Node(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next

    def test_add_two_numbers(self):
        ll_1 = linked_list.LinkedList()
        ll_2 = linked_list.LinkedList()
        ll_1.create_linked_list([2, 4, 3])
        ll_2.create_linked_list([5, 6, 4])
        expected_result = 807
        total = power = 0
        new_ll = self.add_two_numbers(ll_1.head, ll_2.head)
        while new_ll:
            if new_ll.val > 0:
                total += new_ll.val * (10 ** power)
            new_ll = new_ll.next
            power += 1
        self.assertEqual(total, expected_result)






