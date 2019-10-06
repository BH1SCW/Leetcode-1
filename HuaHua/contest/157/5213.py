class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        n, total = 0, len(chips)
        for p in chips:
            if p % 2:
                n += 1
        return min(n, total - n)

