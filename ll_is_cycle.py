import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLCycle(unittest.TestCase):

    def is_ll_cycle(self, ll):
        # does linked list have a cycle (eg. tail points to node inside list)
        slow = fast = ll.head
        # if ll has no cycle then when there is no fast.next we will be at end of list
        # if ll has a cycle we need to use 2 pointers since there is no end.
        # the 2 pointers are like 2 runners on a track. we will know there is a cycle when the pointers meet
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: return True

        return False

    def test_is_ll_odd(self):
        input_list = [2, 4, 5, 7, 8]
        ll_no_cycle = linked_list.LinkedList()
        ll_no_cycle.create_linked_list(input_list)
        self.assertFalse(self.is_ll_cycle(ll_no_cycle))
        ll_with_cycle = linked_list.LinkedList()
        ll_with_cycle.create_linked_list(input_list)
        # create new node with a pointer to a preceding node and add it to end of linked list
        new_tail = nd.Node(9, ll_with_cycle.head.next.next)
        ll_with_cycle.append(new_tail)
        self.assertTrue(self.is_ll_cycle(ll_with_cycle))






