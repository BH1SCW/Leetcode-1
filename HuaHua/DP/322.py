import math
class Solution:
    # 这题没有什么困难的，主要是要写的简洁，一开始写错了，因为并不是大的数用的越多越好，跟具体情况有关系
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [math.inf] * amount
        for c in sorted(coins):
            for t in range(c, amount + 1):
                dp[t] = min(dp[t - c] + 1, dp[t])
        return dp[amount] if dp[amount] != math.inf else -1

