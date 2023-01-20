import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LLIntersection(unittest.TestCase):

    def get_ll_intersection(self, head_a, head_b):
        # return node where 2 linked lists intersect (same node, not same value), else return null
        p1, p2 = head_a, head_b
        while p1 != p2:
            # switching heads when there is no intersection: once you hit the end of the longer list you have gone through
            # len(longer list) - len(smaller list) nodes in the longest list
            # means that in the longer list you have the same number of nodes remaining as the length of smaller list
            # p1 & p2 will both hit tail at same time as a result
            p1 = head_b if not p1 else p1.next
            p2 = head_a if not p2 else p2.next
        return p1

    def test_do_ll_intersect(self):
        input_list_1 = [3, 10, 5, 7, 8]
        ll_1 = linked_list.LinkedList()
        ll_1.create_linked_list(input_list_1)
        input_list_2 = [3, 10, 11, 12, 15, 19, 18]
        ll_2 = linked_list.LinkedList()
        ll_2.create_linked_list(input_list_2)
        self.assertEqual(self.get_ll_intersection(ll_1.head, ll_2.head), None)
        new_node = nd.Node(4)
        input_list_3 = [3, 10, 5, 7, 8]
        ll_3 = linked_list.LinkedList()
        ll_3.create_linked_list(input_list_1)
        ll_3.insert(new_node, 2)
        input_list_4 = [3, 10, 11, 12, 15, 19, 18]
        ll_4 = linked_list.LinkedList()
        ll_4.create_linked_list(input_list_2)
        ll_4.insert(new_node, 4)
        self.assertTrue(self.get_ll_intersection(ll_3.head, ll_4.head) is not None)






