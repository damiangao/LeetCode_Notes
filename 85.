class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        self.m, self.n = len(matrix), len(matrix[0])
        
        # left代表挡墙位置之前有多少个连续的1
        left = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            left[i][0] = 1 if matrix[i][0] == "1" else 0

        for i in range(self.m):
            for j in range(1, self.n):
                if matrix[i][j] == "1":
                    left[i][j] = left[i][j-1] + 1
                else:
                    left[i][j] = 0
        ret = 0
        for j in range(self.n):
            ret = max(ret, self.LRA(left, j))
        return ret

    def LRA(self, left, j):
        l = [0] * self.m
        r = [0] * self.m
        mono_stack = []
        for i in range(self.m):
            while mono_stack and left[mono_stack[-1]][j] >= left[i][j]:
                r[mono_stack[-1]] = i
                mono_stack.pop()
            l[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        return max((r[i] - l[i] - 1) * left[i][j] for i in range(self.m)) if self.m > 0 else 0
