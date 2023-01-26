import unittest


class MyQueue(object):
    """
    implement queue using 2 stacks
    """
    def __init__(self):
        """
        initialize your data structures here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        return self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack)

    def move(self):
        """
        :rtype nothing
        """
        # if outStack is empty then move all values from inStack to outStack
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

class test_q(unittest.TestCase):

    def test_my_q(self):
        q = MyQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.pop(), 1)
        self.assertFalse(q.empty())




