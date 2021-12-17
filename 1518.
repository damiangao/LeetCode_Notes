class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = numBottles // (numExchange - 1)
        return cnt + numBottles - 1 if numBottles % (numExchange - 1) == 0 else cnt + numBottles
