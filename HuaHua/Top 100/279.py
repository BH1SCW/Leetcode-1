from __future__ import annotations
from math import sqrt, floor
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # dp[i] = dp[i - floor(sqrt(i)) ** 2] + 1
            dp[i] = min(dp[i - k ** 2] for k in range(1, floor(sqrt(i)) + 1)) + 1
        return dp[-1]



if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(1))
    print(sol.numSquares(5))
    print(sol.numSquares(12))
    print(sol.numSquares(13))

