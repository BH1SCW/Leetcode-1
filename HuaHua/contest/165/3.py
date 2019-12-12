from __future__ import annotations
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        M, N  =len(matrix), len(matrix[0])
        ans = 0
        for i in range(M)[::-1]:
            for j in range(N)[::-1]:
                if not matrix[i][j]: continue
                right = down = diag = 0
                if i + 1 < M: down = matrix[i + 1][j]
                if j + 1 < N: right = matrix[i][j + 1]
                if i + 1 < M and j + 1 < N: diag = matrix[i + 1][j + 1]
                matrix[i][j] = min(right, down, diag) + 1
                ans += matrix[i][j]
        return ans




if __name__ == '__main__':
    sol = Solution()

