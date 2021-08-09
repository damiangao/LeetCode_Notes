class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                self.cur_size = 0
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    ret = max(ret, self.cur_size)
        return ret
 
    def dfs(self, grid, i, j):
        self.cur_size += 1
        directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        grid[i][j] = 0
        for x, y in directions:
            if 0 <= x < self.m and 0 <= y < self.n and grid[x][y] == 1:
                self.dfs(grid, x, y)
