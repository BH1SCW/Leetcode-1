from __future__ import annotations
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        def neighbor(i, j):
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n:
                    yield x, y
        def bfs(q):
            visited, connected = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
            for i, j in q:
                visited[i][j] = connected[i][j] = 1
            while q:
                new = []
                for i, j in q:
                    for ni, nj in neighbor(i, j):
                        if not visited[ni][nj] and matrix[ni][nj] >= matrix[i][j]:
                            connected[ni][nj], visited[ni][nj] = 1, 1
                            new.append([ni, nj])
                q = new
            return connected
        p = bfs([[0, i] for i in range(n)] + [[i, 0] for i in range(m)])
        q = bfs([[m - 1, i] for i in range(n)] + [[i, n - 1] for i in range(m)])
        return [[i, j] for i in range(m) for j in range(n) if p[i][j] and q[i][j]]


if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(sol.pacificAtlantic(matrix))
