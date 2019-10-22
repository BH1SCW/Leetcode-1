from __future__ import annotations
from collections import defaultdict
# 其实dp的精髓就是state machine， 但是我这道题卡住了是因为state machine里，状态和action是两码事，状态和action要分开
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        rest, hold, sold = defaultdict(int), defaultdict(int), defaultdict(int)
        hold[-1] = sold[-1] = - prices[0]
        for i, p in enumerate(prices):
            rest[i] = max(rest[i - 1], sold[i - 1])
            hold[i] = max(hold[i - 1], rest[i - 1] - p)
            sold[i] = hold[i - 1] + p
        return max(rest[n-1], sold[n-1])

if __name__ == '__main__':
    sol = Solution()
    prices = [1, 2, 3, 0, 2]
    print(sol.maxProfit(prices))
    prices = [6,1,3,2,4,7]
    print(sol.maxProfit(prices))
