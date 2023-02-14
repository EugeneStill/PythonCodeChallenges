import unittest
import collections

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    """
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

    Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists.
    Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
    evict the least recently used key.
    The functions get and put must each run in O(1) average time complexity.
    """

    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key not in self.cache.keys():
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, val):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

    # IMPLEMENTATION WITH DLL & DICT
    # def __init__(self, capacity):
    #     self.capacity = capacity
    #     self.dic = dict()
    #     self.head = Node(0, 0)
    #     self.tail = Node(0, 0)
    #     self.head.next = self.tail
    #     self.tail.prev = self.head
    #
    # def get(self, key):
    #     if key in self.dic:
    #         n = self.dic[key]
    #         self._remove(n)
    #         self._add(n)
    #         return n.val
    #     return -1
    #
    # def put(self, key, value):
    #     if key in self.dic:
    #         self._remove(self.dic[key])
    #     n = Node(key, value)
    #     self._add(n)
    #     self.dic[key] = n
    #     if len(self.dic) > self.capacity:
    #         n = self.head.next
    #         self._remove(n)
    #         del self.dic[n.key]
    #
    # def _remove(self, node):
    #     p = node.prev
    #     n = node.next
    #     p.next = n
    #     n.prev = p
    #
    # def _add(self, node):
    #     p = self.tail.prev
    #     p.next = node
    #     self.tail.prev = node
    #     node.prev = p
    #     node.next = self.tail


class TestLRU(unittest.TestCase):

    def test_lru(self):
        lruc = LRUCache(2);
        lruc.put(1, 1) # cache is {1=1}
        lruc.put(2, 2) # cache is {1=1, 2=2}
        self.assertEqual(lruc.get(1), 1)
        lruc.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(lruc.get(2), -1)
        lruc.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(lruc.get(1), -1)
        self.assertEqual(lruc.get(3), 3)
        self.assertEqual(lruc.get(4), 4)

