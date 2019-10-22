from __future__ import annotations
from collections import Counter, defaultdict
# 这道题和house robber一模一样
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = Counter(nums)
        nums, dp = sorted(list(set(nums))), defaultdict(int)
        for i, n in enumerate(nums):
            if i and nums[i - 1] + 1 == n:
                dp[i] = max(dp[i - 2] + n * count[n], dp[i - 1])
            else:
                dp[i] = dp[i - 1] + n * count[n]
        return dp[len(nums) - 1]


