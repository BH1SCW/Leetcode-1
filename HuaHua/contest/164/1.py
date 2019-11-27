from __future__ import annotations
class Solution:
    # 这题就是抖机灵
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def distance(x1, y1, x2, y2):
            dx, dy = abs(x2 - x1), abs(y2 - y1)
            return max(dx, dy)
            # if dx > dy:
            #     dx, dy = dy, dx
            # if dx == 0: return abs(dy)
            # return dx + (dy - dx)
        ans = 0
        for i in range(1, len(points)):
            ans += distance(*points[i], *points[i - 1])
        return ans



if __name__ == '__main__':
    sol = Solution()
    points = [[1, 1], [3, 4], [-1, 0]]
    print(sol.minTimeToVisitAllPoints(points))
    points = [[3, 2], [-2, 2]]
    print(sol.minTimeToVisitAllPoints(points))
