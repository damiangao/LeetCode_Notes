class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = 0
        max_profit = 0 
        ret_round = 0
        profit = 0
        i = 0
        while wait > 0 or i < len(customers):
            if i < len(customers):
                wait = customers[i] + wait
            board = 4 if wait >= 4 else wait
            wait -= board
            profit += board * boardingCost - runningCost
            if profit > max_profit:
                max_profit = profit
                ret_round = i
            i += 1
        return ret_round + 1  if max_profit > 0 else -1
