from __future__ import annotations
from collections import defaultdict
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * len(t) + [1]
        for i in reversed(range(len(s))):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]
        return dp[0]

    # 初始化比较tricky, 这个还是不够快
    def numDistinct3(self, s: str, t: str) -> int:
        dp = defaultdict(int)
        for i in reversed(range(len(s))):
            for j in reversed(range(len(t))):
                if s[i] == t[j]:
                    if j + 1 == len(t):
                        dp[i, j] = dp[i + 1, j] + 1
                    else:
                        dp[i, j] = dp[i + 1, j + 1] + dp[i + 1, j]
                else:
                    dp[i, j] = dp[i + 1, j]
        return dp[0, 0]

    # 这个能过，不过太慢了，我换一个 bottom-up的方法
    def numDistinct2(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        dp = {}
        def dfs(i, j):
            ans = 0
            if j == M:
                return 1
            if N - i < M - j or i > N - 1 or j > M - 1:
                return 0
            if (i, j) in dp:
                return dp[i, j]
            for k in range(i, N):
                if s[k] == t[j]:
                    ans += dfs(k + 1, j + 1)
            dp[i, j] = ans
            return ans
        return dfs(0, 0)

if __name__ == '__main__':
    sol = Solution()
    s = "ddd"
    t = "dd"
    print(sol.numDistinct(s, t))
