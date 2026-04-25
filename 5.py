# expand around center
class Solution:
    def expandAroundCenter(self, s, l, r):
        while l>=0 and r<=len(s)-1 and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = self.expandAroundCenter(s, i, i)
            s2 = self.expandAroundCenter(s, i, i+1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res
# dp O(n^2) O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        begin = 0
        end = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        for L in range(2, n+1):
            for i in range(n):
                j = L + i -1
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                elif j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and L > max_len:
                    max_len = L
                    begin = i
                    end = j
                    
        return s[begin: end+1]
