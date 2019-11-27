from __future__ import annotations

from functools import lru_cache


class Solution:
    def numWays2(self, steps: int, n: int) -> int:

        MOD = 10 ** 9 + 7
        dp = {}
        def calculate(pos, steps):
            if pos < 0 or pos >= n: return 0
            if pos > steps: return 0
            if steps == pos: return 1
            if (pos, steps) in dp: return dp[pos, steps]
            dp[pos, steps] = (calculate(pos + 1, steps - 1) + calculate(pos - 1, steps - 1) + calculate(pos, steps - 1)) % MOD
            return dp[pos, steps]

        return calculate(0, steps)


    # 这个写法不好，把很多if else放在一行上，语法上有歧义
    def numWays(self, steps: int, arrLen: int) -> int:
        N = 10 ** 9 + 7
        L, H = 0, min(steps // 2 + 1, arrLen)
        dp = [[0] * (steps + 1) for _ in range(H)]
        for step in range(0, steps + 1):
            for i in range(min(step + 1, H)):
                if i == step:
                    dp[i][step] = 1
                else:
                    # a = dp[i - 1][step - 1] if i else 0
                    # b = dp[i][step - 1]
                    # c = dp[i + 1][step - 1] if i + 1 < H else 0
                    dp[i][step] = ((dp[i - 1][step - 1] if i else 0) + (dp[i][step - 1]) + (dp[i + 1][step - 1] if i + 1 < H else 0)) % N
        return dp[0][steps]

    def numWays3(self, steps: int, arrLen: int) -> int:
        N = 10 ** 9 + 7
        low, high = 0, min(steps // 2 + 1, arrLen)
        dp = {}
        def helper(i, s):
            if (i, s) in dp:
                return dp[i, s]
            if i < low or i >= high or i > s: return 0
            if i == s: return 1
            dp[i, s] = (helper(i + 1, s - 1) + helper(i, s - 1) + helper(i - 1, s - 1)) % N # 这一步有问题，因为mod以后求和不对
            return dp[i, s]
        return helper(0, steps)



if __name__ == '__main__':
    sol = Solution()
    steps = 4
    arrLen = 2
    print(sol.numWays(steps, arrLen))
    print(sol.numWays2(steps, arrLen))
    steps = 27
    arrLen = 7
    print(sol.numWays(steps, arrLen))
    print(sol.numWays2(steps, arrLen))
    steps = 3
    arrLen = 2
    print(sol.numWays(steps, arrLen))
    print(sol.numWays2(steps, arrLen))
    steps = 2
    arrLen = 4
    print(sol.numWays(steps, arrLen))
    print(sol.numWays2(steps, arrLen))
