import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLMerge(unittest.TestCase):

    def merge_sorted_lists_iterative(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # cur and dummy will start at the same place, cur will move forward but dummy will not
        # this allows to return dummy.next which will point to the root of the merged linked list
        # because cur already traversed the list and established that root
        cur = dummy = nd.Node()
        while l1 and l2:
            # set curr.next to point to lowest value in l1 or l2
            # move l1 or l2 forward
            # set cur to cur.next so that we can build out the merged list as we progress
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # extend merged list if l1 or l2 has run out of nodes
        cur.next = l1 or l2
        return dummy.next

    def merge_sorted_lists_recursive(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.merge_sorted_lists_recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_sorted_lists_recursive(l1, l2.next)
            return l2

    def test_merge(self):
        ll_1 = linked_list.LinkedList()
        ll_2 = linked_list.LinkedList()
        ll_1.create_linked_list([2, 4, 5, 7, 8])
        ll_2.create_linked_list([1, 3, 6, 9, 10])
        expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        new_ll = self.merge_sorted_lists_iterative(ll_1.head, ll_2.head)
        actual_list = [new_ll.val]
        while new_ll.next:
            actual_list.append(new_ll.next.val)
            new_ll = new_ll.next
        self.assertEqual(expected_list, actual_list)

    def test_merge_recursive(self):
        ll_1 = linked_list.LinkedList()
        ll_2 = linked_list.LinkedList()
        ll_1.create_linked_list([2, 4, 5, 7, 8])
        ll_2.create_linked_list([1, 3, 6, 9, 10])
        expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        new_ll = self.merge_sorted_lists_recursive(ll_1.head, ll_2.head)
        actual_list = [new_ll.val]
        while new_ll.next:
            actual_list.append(new_ll.next.val)
            new_ll = new_ll.next
        self.assertEqual(expected_list, actual_list)






