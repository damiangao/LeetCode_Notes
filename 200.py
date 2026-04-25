class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        self.m, self.n = len(grid), len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    ret += 1
        return ret
 
    def dfs(self, grid, i, j):
        directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        grid[i][j] = '0'
        for x, y in directions:
            if 0 <= x < self.m and 0 <= y < self.n and grid[x][y] == "1":
                self.dfs(grid, x, y)
