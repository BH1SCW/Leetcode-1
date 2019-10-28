from __future__ import annotations
import math
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dis = [triangle[0][0]]
        for row in triangle[1:]:
            new = [math.inf] * len(row)
            for c, n in enumerate(row):
                if c > 0:
                    new[c] = dis[c - 1] + n
                if c < len(row) - 1:
                    new[c] = min(new[c], dis[c] + n)
            dis = new
        return min(dis)

if __name__ == '__main__':
    sol = Solution()
    triangle = [ [2], [3,4], [6,5,7], [4,1,8,3] ]
    print(sol.minimumTotal(triangle))
