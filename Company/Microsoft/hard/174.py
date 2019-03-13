import math
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        T = [[0] * n] * m
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                right = down = math.inf
                if j + 1 <= n - 1:
                    right = T[i][j + 1]
                if i + 1 <= m - 1:
                    down = T[i + 1][j]
                if i == m - 1 and j == n - 1:
                    T[i][j] = 1 if dungeon[i][j] > 0 else - dungeon[i][j] + 1
                else:
                    if dungeon[i][j] >= 0:
                        difference = min(right, down) - dungeon[i][j]
                        # if difference > 0:
                        #     T[j][j] = difference
                        # if difference == 0:
                        #     T[j][j] = 1
                        # if difference < 0:
                        T[i][j] = difference if difference > 0 else 1
                    else:
                        T[i][j] = min(right, down) - dungeon[i][j]
        return T[0][0]

