import unittest
import collections


class coinChange(unittest.TestCase):
    """
    You are given an integer array coins representing coins of different denominations
    and an integer amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
    """
    def coin_change(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        q = collections.deque([(amount, 0)])
        visited = set()

        while q:
            curr_amt, count = q.popleft()
            if curr_amt == 0:
                return count
            for coin in coins:
                new_amt = curr_amt - coin
                # for each coin determine if new amount is valid (>=0) and add it to visited if not already there
                # if the amount is already in visited then that means we arrived at that amount already with same or fewer coins
                if new_amt >= 0 and new_amt not in visited:
                    q.append((new_amt, count + 1))
                    visited.add(new_amt)
        return -1

    def test_coin_change(self):
        self.coin_change([1,2,5], 11)

# LOGGING
# POPPED: AMT 11 COIN COUNT 0
# COIN 1
# COIN 1 NEW AMOUNT 10
# ADDING AMT 10 COIN COUNT 1 TO Q
# COIN 2
# COIN 2 NEW AMOUNT 9
# ADDING AMT 9 COIN COUNT 1 TO Q
# COIN 5
# COIN 5 NEW AMOUNT 6
# ADDING AMT 6 COIN COUNT 1 TO Q
#
# POPPED: AMT 10 COIN COUNT 1
# COIN 1
# COIN 1 NEW AMOUNT 9
# COIN 2
# COIN 2 NEW AMOUNT 8
# ADDING AMT 8 COIN COUNT 2 TO Q
# COIN 5
# COIN 5 NEW AMOUNT 5
# ADDING AMT 5 COIN COUNT 2 TO Q
#
# POPPED: AMT 9 COIN COUNT 1
# COIN 1
# COIN 1 NEW AMOUNT 8
# COIN 2
# COIN 2 NEW AMOUNT 7
# ADDING AMT 7 COIN COUNT 2 TO Q
# COIN 5
# COIN 5 NEW AMOUNT 4
# ADDING AMT 4 COIN COUNT 2 TO Q
#
# POPPED: AMT 6 COIN COUNT 1
# COIN 1
# COIN 1 NEW AMOUNT 5
# COIN 2
# COIN 2 NEW AMOUNT 4
# COIN 5
# COIN 5 NEW AMOUNT 1
# ADDING AMT 1 COIN COUNT 2 TO Q
#
# POPPED: AMT 8 COIN COUNT 2
# COIN 1
# COIN 1 NEW AMOUNT 7
# COIN 2
# COIN 2 NEW AMOUNT 6
# COIN 5
# COIN 5 NEW AMOUNT 3
# ADDING AMT 3 COIN COUNT 3 TO Q
#
# POPPED: AMT 5 COIN COUNT 2
# COIN 1
# COIN 1 NEW AMOUNT 4
# COIN 2
# COIN 2 NEW AMOUNT 3
# COIN 5
# COIN 5 NEW AMOUNT 0
# ADDING AMT 0 COIN COUNT 3 TO Q
#
# POPPED: AMT 7 COIN COUNT 2
# COIN 1
# COIN 1 NEW AMOUNT 6
# COIN 2
# COIN 2 NEW AMOUNT 5
# COIN 5
# COIN 5 NEW AMOUNT 2
# ADDING AMT 2 COIN COUNT 3 TO Q
#
# POPPED: AMT 4 COIN COUNT 2
# COIN 1
# COIN 1 NEW AMOUNT 3
# COIN 2
# COIN 2 NEW AMOUNT 2
# COIN 5
# COIN 5 NEW AMOUNT -1
#
# POPPED: AMT 1 COIN COUNT 2
# COIN 1
# COIN 1 NEW AMOUNT 0
# COIN 2
# COIN 2 NEW AMOUNT -1
# COIN 5
# COIN 5 NEW AMOUNT -4
#
# POPPED: AMT 3 COIN COUNT 3
# COIN 1
# COIN 1 NEW AMOUNT 2
# COIN 2
# COIN 2 NEW AMOUNT 1
# COIN 5
# COIN 5 NEW AMOUNT -2
#
# POPPED: AMT 0 COIN COUNT 3