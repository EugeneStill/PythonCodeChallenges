import unittest
import heapq

class MinHeap(object):
    def __init__(self, val=None):
        self.heap = []
        if val:
            self.push(val)

    def push(self, val):
        heapq.heappush(self.heap, val)
        return


    def pop(self, val=None):
        # hacker rank challenge was set to up to pop a specific element from list, not just min value
        idx = 0
        if val is not None:
            idx = self.heap.index(val)
        val = self.heap[idx]
        self.heap[idx] = self.heap[-1]
        self.heap.pop()
        if idx < len(self.heap):
            heapq._siftup(self.heap, idx)
            heapq._siftdown(self.heap, 0, idx)
        return val

    def print_root(self):
        print(self.heap[0])
        return self.heap[0]

    def print_all(self):
        print(str(self.heap))
        return

class test_heap(unittest.TestCase):

    def test_min_heap(self):
        mh = MinHeap(5)
        mh.push(4)
        mh.push(9)
        mh.print_all()
        self.assertEqual(mh.print_root(), 4)
        self.assertEqual(mh.pop(), 4)
        mh.print_all()
        self.assertEqual(mh.pop(9), 9)
        mh.print_all()
        self.assertEqual(mh.print_root(), 5)





