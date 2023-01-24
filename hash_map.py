import unittest

class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap(object):
    # using list for direct access table
    # using linked list for chaining nodes inside list

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.h = [None] * self.m
        self.NOT_IN_LIST = -1

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.m
        # if node doesn't exist at index, create new node
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                # if key exists, update the value & return
                if cur.pair[0] == key:
                    cur.pair = (key, value)  # update
                    return
                # if end of LL is reached then break while loop
                if cur.next == None:
                    break
                cur = cur.next
            # if key didn't already exist put a new node at end of LL
            cur.next = ListNode(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return self.NOT_IN_LIST

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.m
        cur = prev = self.h[index]
        # if node for key doesn't exist then return
        if not cur:
            return
        # if key is head of LL then point to new head (next)
        if cur.pair[0] == key:
            self.h[index] = cur.next
        # else traverse LL, maintaining pointers for cur & prev until key is found.
        else:
            cur = cur.next
            while cur:
                # when key is found, point prev.next to cur.next removing cur from LL
                if cur.pair[0] == key:
                    prev.next = cur.next
                    return
                else:
                    cur, prev = cur.next, prev.next
        return

class TestHashMap(unittest.TestCase):
    def test_hash_map(self):
        obj = MyHashMap()
        obj.put(20,5)
        self.assertEqual(obj.get(20), 5)
        obj.remove(20)
        self.assertEqual(obj.get(20), obj.NOT_IN_LIST)

