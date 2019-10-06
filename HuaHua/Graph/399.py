from __future__ import annotations
class Solution:
    # 这题就是普通的dfs，没啥技术难度
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        connections = {}
        edges = {}
        for (a, b), val in zip(equations, values):
            connections[a], connections[b] = connections.get(a, []) + [b], connections.get(b, []) + [a]
            edges[a, b], edges[b, a] = val, 1 / val
        def dfs(n, target, searched):
            if not target in connections or not n in connections:
                return -1
            if (n, target) in edges:
                return edges[n, target]
            searched.add(n)
            for neighbor in connections[n]:
                if neighbor == target:
                    return edges[n, target]
                if not neighbor in searched:
                    val = dfs(neighbor, target, searched)
                    if val != -1:
                        val *= edges[n, neighbor]
                        edges[n, target], edges[target, n] = val, 1 / val
                        connections[n] += [target]
                        connections[target] += [n]
                        return val
            return -1
        ans = []
        for q in queries:
            ans.append(dfs(*q, set()))
        return ans


if __name__ == '__main__':
    sol = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(sol.calcEquation(equations, values, queries))
