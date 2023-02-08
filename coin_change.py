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
        q = collections.deque()
        q.append((amount, 0))
        visited = set()
        visited.add(amount)

        # we will set coin count then iterate through all each coin in coins
        # for the number of coins in coin count we will determine the highest amount we can make with 1 coin, 2 coins, etc
        # use the stack to increment coin count and also check results
        while q:
            curr_amt, coin_count = q.popleft()
            print("\nPOPPED: AMT {} COIN COUNT {}".format(curr_amt, coin_count))
            if curr_amt == 0:
                return coin_count
            for c in coins:
                print("COIN {}".format(c))
                new_amt = curr_amt - c
                print("COIN {} NEW AMOUNT {}".format(c, new_amt))
                if new_amt >= 0 and new_amt not in visited:
                    print("ADDING AMT {} COIN COUNT {} TO Q".format(new_amt, coin_count + 1))
                    q.append((new_amt, coin_count + 1))
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