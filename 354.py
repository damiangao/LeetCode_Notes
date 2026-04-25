# elegant solution
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x : (x[0], -x[1]))
        dp = [envelopes[0][1]]
        for i in range(1, len(envelopes)):
            j = bisect.bisect_left(dp, envelopes[i][1])
            if envelopes[i][1] > dp[-1]:
                dp.append(envelopes[i][1])
            else:
                dp[j] = envelopes[i][1]
        
        return len(dp)
 # O(n**2) 
 class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x : (x[0], -x[1]))
        dp = [1] * len(envelopes)

        for i, x in enumerate(envelopes):
            for j in range(i):
                if x[1] > envelopes[j][1]:
                    dp[i] = max(dp[i],  dp[j]+1)
        
        return max(dp)
