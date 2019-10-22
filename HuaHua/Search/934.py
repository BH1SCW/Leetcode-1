from __future__ import annotations
import itertools
class Solution:
    # 换了一个两头找，好久没写了， 随便写写
    def shortestBridge(self, A: List[List[int]]) -> int:
        def neighbor(i, j):
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n:
                    yield x, y

        def helper(i, j):
            contour, q, visited[i][j] = set(), [(i, j)], 1
            while q:
                i, j = q.pop(0)
                for x, y in neighbor(i, j):
                    if visited[x][y]:
                        continue
                    if A[x][y]:
                        visited[x][y] = 1
                        q.append((x, y))
                    else:
                        contour.add((i, j))
            return contour

        n = len(A)
        visited = [[0] * n for i in range(n)]
        q1 = q2 = set()
        for i, j in itertools.product(range(n), range(n)):
            if A[i][j] and not visited[i][j]:
                if not q1:
                    q1 = helper(i, j)
                else:
                    q2 = helper(i, j)
                    break

        d = 0
        while True:
            new = set()
            for i, j in q1:
                for x, y in neighbor(i, j):
                    if (x, y) in q2:
                        return d
                    if visited[x][y]:
                        continue
                    visited[x][y] = 1
                    new.add((x, y))
            d += 1
            q1, q2 = q2, new


    def shortestBridge2(self, A: List[List[int]]) -> int:
        # 这题也是比较直觉，没有什么特别好的办法
        def neighbor(i, j):
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                    yield x, y

        def helper(i, j):
            contour = set()
            q = [(i, j)]
            visited[i][j] = 1
            while q:
                i, j = q.pop(0)
                for x, y in neighbor(i, j):
                    if A[x][y]:
                        visited[x][y] = 1
                        q.append((x, y))
                    else:
                        contour.add((i, j))
            return contour

        n = len(A)
        visited = [[0] * n for i in range(n)]
        q = []
        for i, j in itertools.product(range(n), range(n)):
            if A[i][j]:
                q = list(helper(i, j))
                break

        d = 0
        while True:
            new = []
            for i, j in q:
                for x, y in neighbor(i, j):
                    visited[x][y] = 1
                    if not A[x][y]:
                        new.append((x, y))
                    else:
                        return d
            d += 1
            q = new


if __name__ == '__main__':
    sol = Solution()
    A = [[0,1,0],[0,0,0],[0,0,1]]
    print(sol.shortestBridge(A))
    A = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    print(sol.shortestBridge(A))
