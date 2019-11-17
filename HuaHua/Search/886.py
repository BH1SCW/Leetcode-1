from __future__ import annotations
from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        hate = {}
        group = [-1] * (N + 1)
        for [u, v] in dislikes:
            hate[u] = hate.get(u, []) + [v]
            hate[v] = hate.get(v, []) + [u]
        def bfs(n):
            q = [n]
            cur = group[n] = 0
            while q:
                new = []
                for u in q:
                    for v in hate.get(u, []):
                        if group[v] == -1:
                            group[v] = 1 - cur
                            new.append(v)
                        elif group[v] == cur: return False
                cur = 1 - cur
                q = new
            return True
        for n in range(N):
            if group[n] == -1:
                if not bfs(n):
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    N = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    print(sol.possibleBipartition(N, dislikes))
    N = 3
    dislikes = [[1, 2], [1, 3], [2, 3]]
    print(sol.possibleBipartition(N, dislikes))
    N = 5
    dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    print(sol.possibleBipartition(N, dislikes))


