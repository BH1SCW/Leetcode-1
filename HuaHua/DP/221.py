from __future__ import annotations
class Solution:
    # dp实现起来比较简单，但是想到这个做法不是特别容易
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        ans, m, n = 0, len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not int(matrix[i][j]): continue
                if not i or not j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j])
        return ans * ans

if __name__ == '__main__':
    sol = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(sol.maximalSquare(matrix))
