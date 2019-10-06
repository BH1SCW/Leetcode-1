class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            gold, local = grid[i][j], 0
            grid[i][j] = 0
            for k, l in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= k < m and 0 <= l < n and grid[m][n]:
                    local = max(local, dfs(k, l))
            grid[i][j] = gold
            return gold + local
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans



