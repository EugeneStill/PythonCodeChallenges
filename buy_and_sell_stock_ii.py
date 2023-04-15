import unittest


class BuyAndSellStockII(unittest.TestCase):
    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

    On each day, you may decide to buy and/or sell the stock.
    You can only hold at most one share of the stock at any time.
    However, you can buy it then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.
    """
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit += max(prices[i+1] - prices[i], 0)
        return max_profit


    def test_max_profit(self):
        self.assertEqual(self.max_profit([7,6,4,3,1]), 0)
        self.assertEqual(self.max_profit([7,1,5,3,6,4]), 7)