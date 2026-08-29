class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1 , -prices[i])
            sell1 = max(sell1, prices[i] + buy1)
            buy2 = max(buy2 , sell1 - prices[i])
            sell2 = max(sell2, prices[i] + buy2)

        return sell2