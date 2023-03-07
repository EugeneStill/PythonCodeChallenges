import unittest


class MaxProfit(unittest.TestCase):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        profit = 0

        for i, price in enumerate(prices):
            buy_price = min(price, buy_price)
            profit = max(profit, price-buy_price)
        return profit

    def test_profit(self):
        self.assertEqual(self.max_profit([7,1,5,3,6,4]), 5)
        self.assertEqual(self.max_profit([7,6,4,3,1]), 0)
