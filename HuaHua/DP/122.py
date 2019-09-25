from __future__ import annotations

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        T = [[0, 0, 0] for i in range(len(prices))]
        for i in range(len(prices)):
            T[i][1] =
            T[i][0] = T[i - 1][0]

