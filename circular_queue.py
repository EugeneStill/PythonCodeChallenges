import unittest

# Implement the MyCircularQueue class:
#
# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.

class CircularQueue():

    def __init__(self, k):
        self.size = 0
        self.max_size = k
        self.t = [None] * k
        self.front = self.rear = -1

    def enqueue(self, value):
        if self.size == self.max_size:
            return False
        else:
            if self.rear == -1:
                self.rear = self.front = 0
            else:
                self.rear = (self.rear + 1) % self.max_size
            self.t[self.rear] = value
            self.size += 1
            return True

    def dequeue(self):
        if self.size == 0: return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def front(self):
        return self.t[self.front] if self.size != 0 else -1

    def get_rear(self):
        return self.t[self.rear] if self.size != 0 else -1

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

class TestQueue(unittest.TestCase):
    def test_cq(self):
        my_circular_queue = CircularQueue(3)
        self.assertTrue(my_circular_queue.enqueue(1))
        self.assertTrue(my_circular_queue.enqueue(2))
        self.assertTrue(my_circular_queue.enqueue(3))
        self.assertFalse(my_circular_queue.enqueue(4))
        self.assertEqual(my_circular_queue.get_rear(), 3)
        self.assertTrue(my_circular_queue.is_full())
        self.assertTrue(my_circular_queue.dequeue())
        self.assertTrue(my_circular_queue.enqueue(4))
        self.assertEqual(my_circular_queue.get_rear(), 4)


