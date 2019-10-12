from __future__ import annotations
from collections import defaultdict, deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        q = deque([])
        visited = defaultdict(int)
        target = (1 << len(graph)) - 1
        steps = 0
        for i in range(len(graph)):
            q.append((i, 1 << i))
        while q:
            for i in range(len(q)):
                node, state = q.popleft()
                if state == target:
                    return steps
                if visited[node, state]:
                    continue
                visited[node, state] = 1
                for nb in graph[node]:
                    q.append((nb, state | 1 << nb))
            steps += 1



if __name__ == '__main__':
    sol = Solution()
    graph = [[1,2,3],[0],[0],[0]]
    graph = [[1], [0]]
    graph = [[0]]
    graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    print(sol.shortestPathLength(graph))

