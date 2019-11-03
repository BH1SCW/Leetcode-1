from __future__ import annotations
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if not i and not j:
                    continue
                elif not i:
                    matrix[i][j] = matrix[i][j - 1] + matrix[i][j]
                elif not j:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j]
                else:
                    matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j] - matrix[i - 1][j - 1] + matrix[i][j]
        self.matrix = matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        if not row1 and not col1:
            return matrix[row2][col2]
        elif not row1:
            return matrix[row2][col2] - matrix[row2][col1 - 1]
        elif not col1:
            return matrix[row2][col2] - matrix[row1 - 1][col2]
        else:
            return matrix[row2][col2] - matrix[row1 - 1][col2] - matrix[row2][col1 - 1] + matrix[row1 - 1][col1 - 1]

if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    sol = NumMatrix(matrix)
    print(sol.sumRegion(2, 1, 4, 3))
    print(sol.sumRegion(1, 1, 2, 2))
    print(sol.sumRegion(1, 2, 2, 4))
    print(sol.sumRegion(0, 2, 2, 4))
    print(sol.sumRegion(0, 0, 2, 4))
    print(sol.sumRegion(2, 0, 2, 4))

