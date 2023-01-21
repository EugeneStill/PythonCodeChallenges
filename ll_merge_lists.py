import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLMerge(unittest.TestCase):

    def merge_sorted_lists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # create dummy node that will point to new head of list and curr pointer that we can use to build new list
        cur = dummy = nd.Node()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2
        # return dummy.next since that is still pointing to the beginning of the merged list
        return dummy.next

    def test_is_ll_odd(self):
        ll_1 = linked_list.LinkedList()
        ll_2 = linked_list.LinkedList()
        ll_1.create_linked_list([2, 4, 5, 7, 8])
        ll_2.create_linked_list([1, 3, 6, 9, 10])
        expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        new_ll = self.merge_sorted_lists(ll_1.head, ll_2.head)
        actual_list = [new_ll.val]
        while new_ll.next:
            actual_list.append(new_ll.next.val)
            new_ll = new_ll.next
        self.assertEqual(expected_list, actual_list)






