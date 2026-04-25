# elegant solution 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10 ** 4
        max_profit = 0
        for x in prices:
            max_profit = max(max_profit, x - min_price)
            min_price = min(min_price, x)
        return max_profit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_earn = 0
        for price in prices:
            max_today = price - min_price
            if max_today > max_earn:
                max_earn = max_today
            if price < min_price:
                min_price = price
        return max_earn
