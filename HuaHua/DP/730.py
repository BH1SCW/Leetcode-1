from __future__ import annotations
class Solution:
    # 基本思路是对的，但是细节上有一定的问题，短时间内还是不太容易想清楚
    def countPalindromicSubsequences(self, S: str) -> int:
        N = len(S)
        dp = [[0] * N for _ in range(N)]
        mod = 10 ** 9 + 7
        for l in range(1, N + 1):
            for i, c in enumerate(S):
                j = i + l - 1
                if j > N - 1: break
                if l == 1:
                    dp[i][j] = 1
                elif S[i] != S[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] # 这个我自己独立想出来了
                else:
                    dp[i][j] = 2 * dp[i + 1][j - 1] # 不相等的时候情况比较复杂，我自己没有想出来
                    low, high = i + 1, j - 1
                    while low < j:
                        if S[low] == c: break
                        low += 1
                    while high > i:
                        if S[high] == c: break
                        high -= 1
                    if low == high:
                        dp[i][j] += 1
                    elif low > high:
                        dp[i][j] += 2
                    else:
                        dp[i][j] -= dp[low + 1][high - 1]
                dp[i][j] %= mod
        return dp[0][N - 1]

if __name__ == '__main__':
    sol = Solution()
    S = 'bccb'
    print(sol.countPalindromicSubsequences(S))
    S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
    print(sol.countPalindromicSubsequences(S))
