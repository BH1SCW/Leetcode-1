from __future__ import annotations
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        can_finish = lambda k: sum(math.ceil(p / k) for p in piles) <= H
        # def can_finish(k):
        #     t = H
        #     for p in piles:
        #         t -= math.ceil(p / k)
        #     return t >= 0
        l, h = 1, max(piles)
        while l < h:
            m = (l + h) // 2
            if can_finish(m):
                h = m
            else:
                l = m + 1
        return l

if __name__ == "__main__":
    sol = Solution()
    piles = [3, 6, 7, 11]
    H = 8
    print(sol.minEatingSpeed(piles, H))
