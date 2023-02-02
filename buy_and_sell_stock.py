import unittest


class MaxProfit(unittest.TestCase):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            # update buy price if  current price i< previous buy price
            if prices[i] < buy_price:
                buy_price = prices[i]
            # else compare the previous profit with the current profit
            else:
                profit = max(profit, prices[i] - buy_price)
        return profit

    def test_profit(self):
        self.assertEqual(self.max_profit([7,1,5,3,6,4]), 5)
        self.assertEqual(self.max_profit([7,6,4,3,1]), 0)
