from __future__ import annotations
class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N = len(s)
        cost = [[0] * N for _ in range(N)]
        for l in range(2, N + 1):
            for i in range(N):
                j = i + l - 1
                if j >= N: continue
                if s[j] == s[i]: cost[i][j] = cost[i + 1][j - 1]
                else: cost[i][j] = cost[i + 1][j - 1] + 1
        dp = [[N] * N for _ in range(k + 1)]
        for i in range(N):
            dp[1][i] = cost[i][N - 1]
        for n in range(2, k + 1):
            for i in range(N - n + 1)[::-1]:
                for j in range(i, N - n + 1):
                    dp[n][i] = min(cost[i][j] + dp[n - 1][j + 1], dp[n][i])
        return dp[k][0]


if __name__ == '__main__':
    sol = Solution()
    s = "caaabdef"
    k = 4
    print(sol.palindromePartition(s, k))
    s = "aabbc"
    k = 3
    print(sol.palindromePartition(s, k))
    s = "aabbc"
    k = 4
    print(sol.palindromePartition(s, k))
    s = "aabbc"
    k = 5
    print(sol.palindromePartition(s, k))
    s = "abc"
    k = 2
    print(sol.palindromePartition(s, k))
    s = "leetcode"
    k = 8
    print(sol.palindromePartition(s, k))
