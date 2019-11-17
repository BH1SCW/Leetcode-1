from __future__ import annotations
class Solution:
    # 还不错，就是麻烦一点，唯一的纰漏就是没考虑起点的情况
    # Time: O(m * n * 2 ^ keys)
    # Storage: O(m * n * 2 ^ keys)
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        def neighbor(x, y):
            for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= i < M and 0 <= j < N:
                    yield i, j
        q, K, M, N = [], 0, len(grid), len(grid[0])
        visited = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '@':
                    q = [(i, j, 0, 0)]
                if grid[i][j].islower():
                    K = K | 1 << ord(grid[i][j]) - ord('a')
        while q:
            new = []
            for i, j, step, seen in q:
                if seen == K: return step
                if (i, j, seen) in visited: continue
                visited.add((i, j, seen))
                for ni, nj in neighbor(i, j):
                    if grid[ni][nj] == '#': continue
                    if grid[ni][nj] == '.' or grid[ni][nj] == '@' or (grid[ni][nj].isupper() and 1 << ord(grid[ni][nj]) - ord('A') & seen):
                            new.append((ni, nj, step + 1, seen))
                    if grid[ni][nj].islower():
                        n = 1 << ord(grid[ni][nj]) - ord('a')
                        new.append((ni, nj, step + 1, seen | n))
            q = new
        return -1

if __name__ == '__main__':
    sol = Solution()
    grid = ["@...a",".###A","b.BCc"]
    print(sol.shortestPathAllKeys(grid))
    grid = ["@.a.#", "###.#", "b.A.B"]
    print(sol.shortestPathAllKeys(grid))
    grid = ["@..aA","..B#.","....b"]
    print(sol.shortestPathAllKeys(grid))
