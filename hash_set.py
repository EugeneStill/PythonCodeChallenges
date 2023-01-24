import unittest

class HashSet(object):
    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        bucket, idx = self._index(key)
        if idx == -1:
            bucket.append(key)
        return

    def remove(self, key):
        bucket, idx = self._index(key)
        if idx >= 0:
            bucket.remove(key)
        return

    def contains(self, key):
        _, idx = self._index(key)
        return idx >= 0

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1

class TestHashSet(unittest.TestCase):
    def test_hash_set(self):
        mh = HashSet()
        mh.add(1)
        mh.add(2)
        self.assertTrue(mh.contains(1))
        self.assertFalse(mh.contains(3))
        self.assertTrue(mh.contains(2))
        mh.add(2)
        self.assertTrue(mh.contains(2))
        mh.remove(2)
        self.assertFalse(mh.contains(2))

