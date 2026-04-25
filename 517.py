class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        ret =  sum_ = 0
        avg = total // n
        if total % n != 0:
            return -1
        for i, x in enumerate(machines[:-1]):
            sum_ += x
            need = (i + 1) * avg
            ret = max(ret, abs(sum_ - need), x - avg)
        return ret
