from __future__ import annotations
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_low, cur_max_profit = math.inf, 0
        for p in prices:
            cur_low = min(cur_low, p)
            cur_max_profit = max(cur_max_profit, p - cur_low)
        return cur_max_profit

if __name__ == '__main__':
    sol = Solution()
    s = [-2,-3,-1]
    s = [3,-2,2,-3]
    s = [5,-3,5]
    s = [3,-1,2,-1]
    s = [2,-2,2,7,8,0]
    s = [-2,4,-5,4,-5,9,4]
    s = [1, -2, 3, -2]
    print(sol.maxSubarray(s))

