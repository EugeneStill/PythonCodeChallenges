import unittest
from queue import PriorityQueue
import helpers.linked_list as linked_list



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MergeKLists(unittest.TestCase):
    """
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6
    """

    def mergeKLists(self, lists):
        # Initialize the min-heap
        heap = PriorityQueue()
        # we are adding and maintaining i in case the heap contains identical list vals.
        # that way i can be used as a tie breaker to determine which element is at the top of the priority queue
        for i, lst in enumerate(lists):
            if lst:
                heap.put((lst.val, i, lst))

        print(heap.qsize())
        # Initialize the result linked list
        dummy = ListNode(-1)
        curr = dummy

        # Extract the minimum node from the heap and add its next node to the heap
        while not heap.empty():
            val, i, node = heap.get()
            curr.next = node
            curr = curr.next
            if node.next:
                heap.put((node.next.val, i, node.next))

        return dummy.next

    def test_mkl(self):
        l1 = [1,4,5]
        l2 = [1,3,4]
        l3 = [2,6]
        ll1 = linked_list.LinkedList()
        ll2 = linked_list.LinkedList()
        ll3 = linked_list.LinkedList()
        ll1.create_linked_list(l1)
        ll2.create_linked_list(l2)
        ll3.create_linked_list(l3)
        output = [1,1,2,3,4,4,5,6]
        d = self.merge_k_lists([ll1.head, ll2.head, ll3.head])
        curr = d
        vals = [curr.val]
        while curr.next:
            vals.append(curr.next.val)
            curr = curr.next
        self.assertEqual(vals,output)


    ## ALT SOLUTION
    # def mergeKLists(self, lists):
    #     if not lists:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #     mid = len(lists) // 2
    #     l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
    #     return self.merge(l, r)

    # def merge(self, l, r):
    #     dummy = p = ListNode()
    #     while l and r:
    #         if l.val < r.val:
    #             p.next = l
    #             l = l.next
    #         else:
    #             p.next = r
    #             r = r.next
    #         p = p.next
    #     p.next = l or r
    #     return dummy.next

    # def merge(self, l, r):
    #     if not l or not r:
    #         return l or r
    #     if l.val< r.val:
    #         l.next = self.merge(l.next, r)
    #         return l
    #     r.next = self.merge(l, r.next)
    #     return r
