import unittest
import sys


class MinHeap:

    def __init__(self, maxsize):
        """
            this geeks for geeks implementation is offsetting the root by 1
            this offset impacts the algo for finding left, right, parent & leaf.
        """
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        """ return index of parent node based on current position """
        return pos // 2

    def left_child(self, pos):
        """ return index of left child for current position """
        return 2 * pos

    def right_child(self, pos):
        """ return index of right child for current position """
        return 2 * pos + 1

    def is_leaf(self, pos):
        """ is current position a leaf """
        return pos * 2 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
        return

    def min_heapify(self, pos):
        """ heapify the node at position """
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.is_leaf(pos):
            if (self.Heap[pos] > self.Heap[self.left_child(pos)] or
                    self.Heap[pos] > self.Heap[self.right_child(pos)]):

                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.left_child(pos)] < self.Heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))
        return

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        return


    def print_heap(self):
        for i in range(self.FRONT, (self.size // 2) + 1):
            print("PARENT: {} LEFT: {} RIGHT {}".format(self.Heap[i], self.Heap[self.left_child(i)],
                self.Heap[self.right_child(i)]))
        return


    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.min_heapify(pos)
        return


    def remove(self):
        """ remove root, make last element new root, decrease size then heapify"""
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.min_heapify(self.FRONT)
        return popped


class test_heap(unittest.TestCase):

    def test_min_heap(self):
        print('The minHeap is ')
        minHeap = MinHeap(15)
        minHeap.insert(5)
        minHeap.insert(3)
        minHeap.insert(17)
        minHeap.insert(10)
        minHeap.insert(84)
        minHeap.insert(19)
        minHeap.insert(6)
        minHeap.insert(22)
        minHeap.insert(9)
        minHeap.print_heap()
        self.assertEqual(minHeap.remove(), 3)
