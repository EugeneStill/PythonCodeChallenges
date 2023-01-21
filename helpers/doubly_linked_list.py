import unittest

class Node(object):

    def __init__(self, val=None, next=None, prev=None, child=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.child = child


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        if head is not None:
            self.size += 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        n = Node(val)
        if not self.head:
            self.head = self.tail = n
        else:
            self.head.prev = n
            n.next = self.head
            self.head = n
        self.size += 1
        return

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        n = Node(val)
        if not self.head:
            self.head = self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            n = Node(val)
            n.prev = cur.prev
            n.next = cur
            cur.prev.next = n
            cur.prev = n
            self.size += 1
        return

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        if self.size == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head.next.prev, self.head = None, self.head.next
        elif index == self.size - 1:
            self.tail.prev.next, self.tail = None, self.tail.prev
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            cur.next.prev, cur.prev.next = cur.prev, cur.next
        self.size -= 1
        return

    def build_dll(self, input_list):
        for i in input_list:
            self.addAtTail(i)
        return

class TestDLL(unittest.TestCase):

    def test_dll(self):
        myLinkedList = LinkedList()
        myLinkedList.addAtHead(1)
        myLinkedList.addAtTail(3)
        myLinkedList.addAtIndex(1, 2)
        self.assertEqual(myLinkedList.get(1), 2)
        myLinkedList.deleteAtIndex(1)
        self.assertEqual(myLinkedList.get(1), 3)
