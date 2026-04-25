class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        track = [] # 用来记录当前的路径
        self.backtrack(n, 0, track, k)
        return self.res
    
    def backtrack(self, n, start, track, k):
        if len(track) == k:
            self.res.append(track[:])
            return
        for i in range(start, n):
            track.append(i + 1)
            self.backtrack(n, i + 1, track, k)
            track.pop()
            
# pruning
class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        track = [] # 用来记录当前的路径
        self.backtrack(n, 0, track, k)
        return self.res
    
    def backtrack(self, n, start, track, k):
        if len(track) == k:
            self.res.append(track[:])
            return
        for i in range(start, n - k + len(track) + 1): # pruning
            track.append(i + 1)
            self.backtrack(n, i + 1, track, k)
            track.pop()
