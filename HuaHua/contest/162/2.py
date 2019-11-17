from __future__ import annotations
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum): return []
        res = [[0] * len(colsum) for _ in range(2)]
        for i, n in enumerate(colsum):
            if n == 2:
                res[0][i] = res[1][i] = 1
                upper, lower = upper - 1, lower - 1
        if upper < 0 or lower < 0: return []
        for i, n in enumerate(colsum):
            if n == 1:
                if upper:
                    res[0][i] = 1
                    upper -= 1
                elif lower:
                    res[1][i] = 1
                    lower -= 1
        return res

if __name__ == '__main__':
    sol = Solution()
    upper = 9
    lower = 2
    colsum = [0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2]
    print(sol.reconstructMatrix(upper, lower, colsum))
    upper = 9
    lower = 2
    colsum = [0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2]
    print(sol.reconstructMatrix(upper, lower, colsum))
