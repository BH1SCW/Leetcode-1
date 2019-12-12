from __future__ import annotations
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        N = 10 ** 9 + 7
        for k in range(d):
            for i in range(0, target + 1)[::-1]:
                if i < k: dp[i] = 0
                if i == k: dp[i] = 1
                dp[i] = sum(dp[max(i - f, 0) : i]) % N
        return dp[target] % N

if __name__ == '__main__':
    sol = Solution()
    d = 30
    f = 30
    target = 500
    print(sol.numRollsToTarget(d, f, target))
    d = 1
    f = 2
    target = 3
    print(sol.numRollsToTarget(d, f, target))
    d = 2
    f = 5
    target = 10
    print(sol.numRollsToTarget(d, f, target))
    d = 2
    f = 6
    target = 7
    print(sol.numRollsToTarget(d, f, target))
    d = 1
    f = 6
    target = 3
    print(sol.numRollsToTarget(d, f, target))
