class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        ans = (0, 0, 1)
        for l in range(1, N + 1):
            for i in range(N - l + 1):
                dp[i][i + l - 1] = s[i] == s[i + l - 1] and (l <= 3 or dp[i + 1][i + l - 2])
                if dp[i][i + l - 1]: ans = (i, i + l - 1)
        return s[ans[0]: ans[1] + 1]



