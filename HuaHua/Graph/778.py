from __future__ import annotations
import heapq
from collections import defaultdict
# 这题我虽然写出来了，但是我有许多地方能改进，一个就是bfs和dfs不一样，bfs的时候加入队列的时候就要标记，否则的话可能会遇到重复加入队列的事情
# 这一点我bfs写得少，所以没注意过。
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        clock, N, added = 0, len(grid), defaultdict(int)
        q = [(grid[0][0], 0, 0)]
        heapq.heapify(q)
        while q:
            t, i, j = heapq.heappop(q)
            clock = max(clock, t)
            if (i, j) == (N - 1, N - 1):
                return clock
            for k, l in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= k < N and 0 <= l < N and not added[k, l]:
                    heapq.heappush(q, (grid[k][l], k, l))
                    added[i, j] = 1

if __name__ == '__main__':
    sol = Solution()
    grid = [[0,2],[1,3]]
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    print(sol.swimInWater(grid))
