from __future__ import annotations
# 这道题我一共用了两种方法做，一种就是dfs，另外一个是union find。
# dfs的难点在于这是一个无向图，任何一条边都是一个圈，所以要多传递一个参数避免走回头路，另外一个是没有必要用纯正的dfs，这样的代码会比较冗余，一个聪明的办法就是一条边一条边的构建这个图，然后每加入一条新边的时候，看看这两条边是不是相连的，如果是的话，那么就是有圈的。
# 那么换到有向图可不可以用这个算法呢？也是可以的。所以处理有向图的时候还是要比无向图稍微麻烦一点的。
# union find的话，path compression网站上的那个算法是错误的。union find属于不太常用的算法，不过这个就不适合有向图了。
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 2))
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return True
            parent[p1] = p2
            return False
        for e in edges:
            u, v = e[0], e[1]
            if union(u, v):
                return e


    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     adj = {}
    #     for e in edges:
    #         u, v = e[0], e[1]
    #         adj[u], adj[v] = [], []
    #     def dfs(node, pre, des):
    #         for n in adj[node]:
    #             if n == pre:
    #                 continue
    #             if n == des:
    #                 return True
    #             if dfs(n, node, des):
    #                 return True
    #         return False
    #     for e in edges:
    #         u, v = e[0], e[1]
    #         if dfs(v, u, u):
    #             ans = e
    #         else:
    #             adj[u].append(v)
    #             adj[v].append(u)
    #     return ans



    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     graph = {}
    #     for p in edges:
    #         u, v = p[0], p[1]
    #         # for u, v in zip(*p):
    #         if u in graph:
    #             graph[u] += [v]
    #         else:
    #             graph[u] = [v]
    #         if v in graph:
    #             graph[v] += [u]
    #         else:
    #             graph[v] = [u]
    #     def dfs(node, pre, ans):
    #         visiting.add(node)
    #         for n in graph[node]:
    #             if n == pre:
    #                 continue
    #             if n in visiting:
    #                 return [node, n] if node < n else [n, node]
    #             if not n in visited:
    #                 ans = dfs(n)
    #                 if ans:
    #                     return ans
    #         visiting.remove(node)
    #     visited = set()
    #     visiting = set()
    #     for e in edges:
    #         u, v = e[0], e[1]
    #         if not u in visited:
    #             ans = dfs(u)
    #             if ans:
    #                 return ans
    #
    #

if __name__ == '__main__':
    sol = Solution()
    e = [[1,2], [1,3], [2,3]]
    print(sol.findRedundantConnection(e))
