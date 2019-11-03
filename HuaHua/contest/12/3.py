class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = {}
        for [u, v] in edges:
            graph[u] = graph.get(u, []) + [v]
            graph[v] = graph.get(v, []) + [u]
        def dfs(n):
            visited.add(n)
            d1, d2 = 1, 1
            for nb in graph[n]:
                if not nb in visited:
                    d = dfs(nb) + 1
                    if d > d1:
                        d1, d2 = d, d1
                    elif d > d2:
                        d2 = d
            self.ans = max(self.ans, d1 + d2 - 1)
            return max(d1, d2)
        self.ans = 0
        visited = set()
        for n in graph:
            if not n in visited:
                dfs(n)
        return self.ans - 1

