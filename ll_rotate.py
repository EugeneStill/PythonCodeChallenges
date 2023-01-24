import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLRotate(unittest.TestCase):

    def ll_rotate(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        last, n = head, 1
        while last.next:
            last = last.next
            n += 1

        # smaller number % larger number = smaller number
        # if k > n and k % n is 0 then we end up rotating back to head
        if k % n == 0:
            return head

        middle = head
        for _ in range(n - k % n - 1):
            middle = middle.next

        # set new head to node after middle, point end of old node to original head, set middle.next to None since it is new tail
        new_head = middle.next
        last.next = head
        middle.next = None
        return new_head

    def test_ll_rotate(self):
        input_list = [1, 2, 3, 4, 5]
        expected_result = [3, 4, 5, 1, 2]
        ll = linked_list.LinkedList()
        ll.create_linked_list(input_list)
        new_head = self.ll_rotate(ll.head, 3)
        actual_result = [new_head.val]
        current = new_head
        while current.next:
            actual_result.append(current.next.val)
            current = current.next
        self.assertEqual(expected_result, actual_result)







