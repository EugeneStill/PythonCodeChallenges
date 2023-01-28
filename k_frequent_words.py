import unittest
import collections
import heapq


class MaxHeap:
    def __init__(self):
        self._queue = []

    def push(self, count, word):
        """ add tuple to heap so that we can prioritize words based on count"""
        heapq.heappush(self._queue, (-count, word))

    def pop(self):
        return heapq.heappop(self._queue)

    def print_all(self):
        print(str(self._queue))


class TestKFrequentWords(unittest.TestCase):
    def k_frequent_words(self, words, k):
        # counter = collections.Counter(words)
        counter = collections.defaultdict(int)
        for w in words:
            counter[w] += 1

        heap = MaxHeap()

        for word, count in counter.items():
            heap.push(count, word)
        heap.print_all()
        # get the last element (word) in tuple when we pop
        return [heap.pop()[-1] for _ in range(k)]

    def test_kfw(self):
        res = self.k_frequent_words(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)
        for r in res:
            print(r)
        return


