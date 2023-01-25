import unittest
import collections

# https://www.geeksforgeeks.org/deque-in-python/

class OpenTheLock(unittest.TestCase):
    """
    You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0' through '9'.
    The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
    Each move consists of turning one wheel one slot.

    The lock initially starts at '0000', a string representing the state of the 4 wheels.

    You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
    the wheels of the lock will stop turning and you will be unable to open it.

    Given a target representing the value of the wheels that will unlock the lock,
    return the minimum total number of turns required to open the lock, or -1 if it is impossible.
    """

    def open_the_lock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead_set = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = set('0000')

        while queue:
            (wheel_state, turns) = queue.popleft()
            if wheel_state == target:
                return turns
            elif wheel_state in dead_set:
                continue
            for i in range(4):
                # for each slot in wheel, move down 1, up 1 to get new combos
                digit = int(wheel_state[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_combo = wheel_state[:i]+str(new_digit)+wheel_state[i+1:]
                    if new_combo not in visited:
                        visited.add(new_combo)
                        queue.append((new_combo, turns+1))
        return -1

    def test_open_lock(self):
        self.assertEqual(self.open_the_lock(["0201","0101","0102","1212","2002"], "0202"), 6)
        self.assertEqual(self.open_the_lock(["8888"], "0009"), 1)
        self.assertEqual(self.open_the_lock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"), -1)



