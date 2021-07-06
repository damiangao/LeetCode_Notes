class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.m = len(s)
        self.n = len(p)
        self.memo = {}
        return self.dp(0,0)
    
    def dp(self, i, j):
        if j == self.n:
            return i == self.m
        
        if i == self.m:
            if (self.n-j)%2 == 1:
                return False
            for t in range(j, self.n, 2):
                if self.p[t+1] != '*':
                    return False
            return True
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        res = False
        if self.s[i] == self.p[j] or self.p[j] == '.':
            if j < self.n - 1 and self.p[j + 1] == '*':
                res = self.dp(i, j + 2) or self.dp(i + 1, j)
            else:
                res = self.dp(i + 1, j + 1)
        else:
            if j < self.n - 1 and self.p[j + 1] == '*':
                res = self.dp(i, j + 2)
            else:
                res = False
        self.memo[(i, j)] = res
        return res 

