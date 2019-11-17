from __future__ import annotations
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def neighbor(x, y):
            for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= i < M and 0 <= j < N:
                    yield i, j
        if not grid or not grid[0]: return 0
        M, N = len(grid), len(grid[0])
        visited = [[0] * N for _ in range(M)]
        def dfs(i, j):
            visited[i][j] = 1
            n = 1 - int(i == 0 or j == 0 or i == M - 1 or j == N - 1)
            for ni, nj in neighbor(i, j):
                if grid[ni][nj] == 0 and not visited[ni][nj] and not dfs(ni, nj):
                        n = 0
            return n
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0 and not visited[i][j]:
                    res += dfs(i, j)
        return res


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    print(sol.closedIsland(grid))
    grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
    print(sol.closedIsland(grid))
    grid = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]
    print(sol.closedIsland(grid))
