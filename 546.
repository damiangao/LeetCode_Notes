class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        self.boxes = boxes
        self.memo = defaultdict(int)
        return self.dfs(0, len(boxes)-1, 0)

    def dfs(self, l, r, k):
        if self.memo[(l,r,k)]:
            return self.memo[(l,r,k)]

        if l == r:
            return (k+1)**2
        
        if self.boxes[r] == self.boxes[r-1]:
            return self.dfs(l, r-1, k+1)
        
        res = (k+1)**2 + self.dfs(l, r-1, 0)

        for i in reversed(range(l, r-1)):
            if self.boxes[i] == self.boxes[r]:
                res = max(res, self.dfs(l, i, k+1) + self.dfs(i+1, r-1, 0))
        self.memo[(l,r,k)] = res
        return res
