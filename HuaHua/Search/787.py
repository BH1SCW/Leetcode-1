from __future__ import annotations
import math
class Solution:
    # 网上看到一个比较秒的做法，不过其实那个应该更为复杂一些，但是最坏的情况下是差不多的，https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115596/c%2B%2B-8-line-bellman-ford
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph, price, ans = {}, {}, {src:0}
        for u, v, p in flights:
            graph[u] = graph.get(u, []) + [v]
            price[u, v] = p
        q = [(src, 0)]
        for _ in range(K + 1):
            if not q: break
            new = []
            for u, p in q:
                for v in graph.get(u, []):
                    if p + price[u, v] < ans.get(v, math.inf):
                        ans[v] = p + price[u, v]
                        new.append((v, ans[v]))
            q = new
        return ans.get(dst, -1)

if __name__ == '__main__':
    sol = Solution()
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(sol.findCheapestPrice(n, edges, src, dst, k))



