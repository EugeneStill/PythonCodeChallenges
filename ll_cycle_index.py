import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLCycle(unittest.TestCase):

    def get_ll_index(self, ll):
        # return node where tail points if found, else return null
        slow = fast = ll.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = ll.head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow
        return

    def test_is_ll_odd(self):
        input_list = [2, 4, 5, 7, 8]
        ll_no_cycle = linked_list.LinkedList()
        ll_no_cycle.create_linked_list(input_list)
        self.assertEqual(self.get_ll_index(ll_no_cycle), None)
        ll_with_cycle = linked_list.LinkedList()
        ll_with_cycle.create_linked_list(input_list)
        # create new node with a pointer to a preceding node and add it to end of linked list
        new_tail = nd.Node(9, ll_with_cycle.head.next.next)
        ll_with_cycle.append(new_tail)
        self.assertEqual(self.get_ll_index(ll_with_cycle), ll_with_cycle.head.next.next)






