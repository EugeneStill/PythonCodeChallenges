import unittest
import random

class InsertDeleteGetRandom(object):
    """
    Implement the RandomizedSet class:

    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
    You must implement the functions of the class such that each function works in average O(1) time complexity.
    """

    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val):
        if val in self.data_map:
            return False
        # if val isn't in map then add val: index (end of list) to map and add val to list
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val):
        if not val in self.data_map:
            return False

        # swap val with last element in list & swap index values in map
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]
        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        # move val to end of list then pop i
        # t
        self.data[-1] = val
        self.data.pop()

        # remove val from the dictionary
        self.data_map.pop(val, False)
        return True

    def getRandom(self):
        return self.data[random.randrange(len(self.data))]

class TestRandomSet(unittest.TestCase):
    def test_randomized_set(self):
        rs = InsertDeleteGetRandom()
        self.assertTrue(rs.insert(1))
        self.assertFalse(rs.remove(2))
        self.assertTrue(rs.insert(2))
        self.assertIn(rs.getRandom(), [1, 2])
        self.assertTrue(rs.remove(1))
        self.assertFalse(rs.insert(2))
        self.assertEqual(rs.getRandom(), 2)




