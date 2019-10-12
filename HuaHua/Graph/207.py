from __future__ import annotations
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, visited, visiting = defaultdict(list), defaultdict(int), defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
        def dfs(u):
            visiting[u] = 1
            for nxt in graph[u]:
                if visiting[nxt]:
                    return False
                if not visited[nxt]:
                    if not dfs(nxt):
                        return False
            visited[u],  visiting[u] = 1, 0
            return True
        for u in range(numCourses):
            if not visited[u]:
                if not dfs(u):
                    return False
        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited, visiting = defaultdict(int), defaultdict(int)
        order = deque([])
        for u, v in prerequisites:
            graph[v].append(u)
        def dfs(u, order):
            visiting[u] = 1
            for nxt in graph[u]:
                if visiting[nxt]:
                    return False
                if not visited[nxt]:
                    if not dfs(nxt, order):
                        return False
            visited[u] = 1
            visiting[u] = 0
            order.appendleft(u)
            return True
        for u in range(numCourses):
            if not visited[u]:
                if not dfs(u, order):
                    return False
        visited, visiting = defaultdict(int), defaultdict(int)
        for u in order:
            if not visited[u]:
                if not dfs(u, deque([])):
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    num = 2
    pre = [[1,0]]
    print(sol.canFinish(num, pre))


