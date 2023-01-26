import unittest
import collections

class MyStack(object):
    def __init__(self):
        self.queue = None

    def push(self, x):
        q = collections.deque()
        q.append(x)
        q.append(self.queue)
        self.queue = q

    def pop(self):
        elem = self.queue.popleft()
        # have to pop a 2nd time since when we push, we pushed a value, but then we also pushed an instance of deque
        self.queue = self.queue.popleft()
        return elem

    def top(self):
        return self.queue[0]

    def empty(self):
        return not self.queue

class test_stack(unittest.TestCase):

    def test_my_stack(self):
        ms = MyStack()
        ms.push(1)
        ms.push(2)
        self.assertEqual(ms.top(), 2)
        self.assertEqual(ms.pop(), 2)
        self.assertEqual(ms.top(), 1)
        self.assertFalse(ms.empty())




