from __future__ import annotations
from collections import defaultdict
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = defaultdict(int)
        for j in range(len(word2) + 1):
            dp[0, j] = j
        for i in range(len(word1) + 1):
            dp[i, 0] = i
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1, j + 1] = dp[i, j]
                else:
                    dp[i + 1, j + 1] = min(dp[i, j + 1], dp[i + 1, j]) + 1
        return dp[len(word1), len(word2)]

    def minDistance2(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                memo[i, j] = dfs(i + 1, j + 1)
            else:
                memo[i, j] = min(dfs(i + 1, j), dfs(i, j + 1)) + 1
            return memo[i, j]
        return dfs(0, 0)

if __name__ == '__main__':
    sol = Solution()
    w1 = ""
    w2 = ""
    w2 = "fjd"
    w2 = "eat"
    w1 = "sat"
    w2 = "dem"
    w1 = "sea"
    w2 = "sea"
    print(sol.minDistance(w1, w2))
