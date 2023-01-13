import unittest

import helpers.node as nd
import helpers.linked_list as linked_list

class LinkedListExercises(unittest.TestCase):

    def test_lle(self):
        ll = linked_list.LinkedList()
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for a in arr:
            new_node = nd.Node(a)
            ll.append(new_node)
        nn = nd.Node(0)
        ll.insert(nn, 1)
        ll.delete(8)
        ll.print()
        return


