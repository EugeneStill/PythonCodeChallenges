import unittest
import sys

class MinStack(unittest.TestCase):
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.
    """

    def __init__(self):
        self.stack = []
        self.DEFAULT = sys.maxsize

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # whenever we push to stack we add a tuple(value, min value of the stack)
        self.stack.append((val, min(self.getMin(), val)))
        return

    def pop(self):
        """
        :rtype: None
        """
        # even if we pop the current min val, the last element in the stack before it will have the previous min val
        # which now becomes the current min val again
        self.stack.pop()
        return

    def top(self):
        """
        :rtype: int
        """
        # get the element 0 from the last element on the stack
        if self.stack:
            return self.stack[-1][0]
        return self.DEFAULT

    def getMin(self):
        """
        :rtype: int
        """
        # we can always get the min value contained in the stack by checking element 1 of the last element on the stack
        if self.stack:
            return self.stack[-1][1]
        return self.DEFAULT

class TestMinStack(unittest.TestCase):

    def test_min_stack(self):
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        self.assertEqual(ms.getMin(), -3)
        ms.pop()
        self.assertEqual(ms.top(), 0)
        self.assertEqual(ms.getMin(), -2)




