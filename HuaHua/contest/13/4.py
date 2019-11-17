from __future__ import annotations
class Solution:
    # 这题没什么特别的，就是普通dp
    def numberOfWays(self, num_people: int) -> int:
        dp = [0] * (num_people // 2 + 1)
        dp[0] = 1
        N = 10 ** 9 + 7
        for p in range(2, num_people + 1, 2):
            for n in range(2, p + 1):
                if n % 2: continue
                dp[p // 2] += (dp[(n - 2) // 2] * dp[(p - n) // 2]) % N
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    for n in range(2, 9, 2):
        print(sol.numberOfWays(n))
