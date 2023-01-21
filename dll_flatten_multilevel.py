import unittest

import helpers.doubly_linked_list as dll

class DLLFlattenMultiLevel(unittest.TestCase):

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        self.travel(head)
        return head

    def travel(self, cur):
        while cur:
            # have to store next node in case cur.next gets overridden to point to child node.
            # will use this to connect the child level back to current level
            next_node = cur.next
            # reached the last node in current level, assign it to 'tail' for return
            if not next_node:
                tail = cur

            # if the current node contains a child node, this if clause will handle the child
            # node's level and any more child nodes that it spawns
            if cur.child:
                cur.child.prev = cur
                cur.next = cur.child

                #returns tail after traversing the child node's level
                child_tail = self.travel(cur.child)

                # if there exists a node in the prior level, connect its prev pointer
                # to the child node's tail. if there is none, then no need
                if next_node:
                    next_node.prev = child_tail

                # have to connect child_tail back to prior level regardless if next node is null or not
                child_tail.next = next_node

                # clearing child pointers
                cur.child = None  # clearing child pointers

            # this will either begin traversing cur's child node level (if exists) or resume
            # traversing cur's current level
            cur = cur.next

        # returns tail node of level
        return tail

    def test_flatten(self):
        ll_1 = dll.LinkedList()
        ll_2 = dll.LinkedList()
        ll_3 = dll.LinkedList()
        ll_1.build_dll([1, 2, 3, 4, 5, 6])
        ll_2.build_dll([7, 8, 9, 10])
        ll_3.build_dll([11, 12])
        ll_2.head.next.child = ll_3.head
        ll_1.head.next.next.child = ll_2.head
        expected_list = [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]
        new_ll = self.flatten(ll_1.head)
        actual_list = [new_ll.val]
        while new_ll.next:
            actual_list.append(new_ll.next.val)
            new_ll = new_ll.next
        self.assertEqual(expected_list, actual_list)






