from collections import deque
import math
# author: Xianglong Hu
# speed: 36%
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(matrix), len(matrix[0])
        def neighbors(r, c):
            for row, col in (r - 1, c), (r + 1, c), (r, c - 1), (r, c+ 1):
                if 0 <= row < R and 0 <= col < C:
                    yield (row, col)
        q = deque([((r, c), 0) for r in range(R) for c in range(C) if not matrix[r][c]])
        distance = [[math.inf if matrix[r][c] else 0 for c in range(C)] for r in range(R)]
        while q:
            (r, c), d = q.popleft()
            for nr, nc in neighbors(r, c):
                if distance[nr][nc] > d + 1:
                    q.append(((nr, nc), d + 1))
                    distance[nr][nc] = d + 1
        return distance

if __name__ == '__main__':
    sol = Solution()
    matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(sol.updateMatrix(matrix))


