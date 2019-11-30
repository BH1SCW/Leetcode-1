from __future__ import annotations
import math, itertools
class Solution:
    # 其实可以用第一排或第一列来纪录这一排或这一列的情况，不过我懒得写啊
    def setZeroes(self, matrix: List[List[int]]) -> None:
        K = math.inf
        m, n = len(matrix), len(matrix[0])
        for i, j in itertools.product(range(m), range(n)):
                if matrix[i][j]: continue
                for col in range(n):
                    if matrix[i][col]: matrix[i][col] = K
                for row in range(m):
                    if matrix[row][j]: matrix[row][j] = K
        for i, j in itertools.product(range(m), range(n)):
                if matrix[i][j] == K: matrix[i][j] = 0

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(sol.setZeroes(matrix))
    print(matrix)
    matrix = [ [0,1,2,0], [3,4,5,2], [1,3,1,5] ]
    print(sol.setZeroes(matrix))
    print(matrix)
