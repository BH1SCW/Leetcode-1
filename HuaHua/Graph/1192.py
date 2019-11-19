from __future__ import annotations

class Solution:
    # 这个不是最原始的算法，这道题的复杂度在于变种比较多，有向图和无向图又略有区别，所以比较容易搞错
    # https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
    # https://leetcode.com/problems/critical-connections-in-a-network/discuss/382526/Tarjan-Algorithm-(DFS)-Python-Solution-with-explanation
    # https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        low = [0] * n
        index = [0] * n
        graph = {}
        for [u, v] in connections:
            graph[u] = graph.get(u, []) + [v]
            graph[v] = graph.get(v, []) + [u]
        self.depth = 0
        def dfs(u, parent):
            self.depth += 1
            low[u] = index[u] = self.depth
            for nb in graph.get(u, []):
                if nb == parent: continue
                if not low[nb]:
                    dfs(nb, u)
                low[u] = min(low[u], low[nb])
        dfs(1, 1)
        return [[u, v] for [u, v] in connections if low[u] > index[v] or low[v] > index[u]]


if __name__ == '__main__':
    sol = Solution()
    n = 5
    connections = [[1, 0], [2, 1], [3, 2], [4, 2], [2, 0], [3, 0], [4, 0]]
    print(sol.criticalConnections(n, connections))
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    print(sol.criticalConnections(n, connections))
    n = 5 + 1
    connections = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
    print(sol.criticalConnections(n, connections))
    n = 6 + 1
    connections = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]
    print(sol.criticalConnections(n, connections))
    n = 9 + 1
    connections = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
    print(sol.criticalConnections(n, connections))

