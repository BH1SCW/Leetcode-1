from __future__ import annotations


class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        def helper(bottomLeft, topRight):
            x1, y1, x2, y2 = bottomLeft.x, bottomLeft.y, topRight.x, topRight.y
            if not sea.hasShips(topRight, bottomLeft): return 0
            ym = (y1 + y2) // 2
            xm = (x1 + x2) // 2
            if x1 == x2 and y1 == y2:
                return int(sea.hasShips(topRight, bottomLeft))
            if x1 == x2:
                return helper(Point(x1, y1), Point(x1, ym)) + helper(Point(x1, ym + 1), Point(x1, y2))
            if y1 == y2:
                return helper(Point(x1, y1), Point(xm, y1)) + helper(Point(xm + 1, y1), Point(x2, y1))
            return helper( Point(x1, y1), Point(xm, ym)) + helper( Point(xm + 1, y1), Point(x2, ym)) + helper( Point(x1, ym + 1), Point(xm, y2)) + helper( Point(xm + 1, ym + 1), Point(x2, y2))
        return helper(bottomLeft, topRight)



if __name__ == '__main__':
    sol = Solution()
