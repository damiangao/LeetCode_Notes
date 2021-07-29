class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n
        s = []

        for i in reversed(range(n)):
            while s and temperatures[i] >= temperatures[s[-1]]:
                s.pop()
            
            ret[i] = s[-1]-i if s else 0
            s.append(i)
        return ret
