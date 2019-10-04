from __future__ import annotations
class Solution:
    # 这个题我还是想复杂了，其实没有必要记前一个的，因为不会陷入死循环，前一个必定已经染过色了，所以不会反复搜索，因此代码还是可以继续简化，其他
    # 没什么特殊的技巧了。当然还有一个就是BFS，bottom up的方式，会快一点。
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(n):
            for nb in graph[n]:
                if nb in color:
                    if color[nb] == color[n]:
                        return False
                else:
                    color[nb] = not color[n]
                    if not dfs(nb, n):
                        return False
            return True
        for i in range(len(graph)):
            if not i in color:
                color[i] = False
                if not dfs(i):
                    return False
        return True


    def isBipartite2(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(n, pre):
            for nb in graph[n]:
                if nb == pre:
                    continue
                if nb in color:
                    if color[nb] == color[n]:
                        return False
                else:
                    color[nb] = not color[n]
                    if not dfs(nb, n):
                        return False
            return True
        for i in range(len(graph)):
            if not i in color:
                color[i] = False
                if not dfs(i, -1):
                    return False
        return True



if __name__ == '__main__':
    sol = Solution()
    graph = [[4],[],[4],[4],[0,2,3]]
    print(sol.isBipartite(graph))