from __future__ import annotations
import itertools
class Solution:
    # 这题比较适合union find做，比较简洁，但是union find的时候有很多细节需要注意
    # 还有就是初步运用了itertools
    # *的话不如直接一个tuple简洁
    def regionsBySlashes(self, grid: List[str]) -> int:
        parent = {}
        def find(x, y, k):
            if not (x, y, k) in parent:
                parent[x, y, k] = (x, y, k)
            if (x, y, k) != parent[x, y, k]:
                parent[x, y, k] = find(*parent[x, y, k])
            return parent[x, y, k]
        # 这里我一开是就写错了
        def union(g1, g2):
            parent[find(*g1)] = find(*g2)
        for (i, j) in itertools.product(range(len(grid)), repeat=2):
            if i:
                union((i, j, 4), (i - 1, j, 2))
            if j:
                union((i, j, 1), (i, j - 1, 3))
            if grid[i][j] != "\\":
                union((i, j, 1), (i, j, 4))
                union((i, j, 2), (i, j, 3))
            if grid[i][j] != "/":
                union((i, j, 1), (i, j, 2))
                union((i, j, 3), (i, j, 4))
        return len(set(map(lambda x: find(*x), parent.keys())))


if __name__ == '__main__':
    sol = Solution()
    grid = [ " /", "/ " ]
    grid = [" /", "  "]
    grid = ["\\/", "/\\"]
    grid = ["/\\", "\\/"]
    grid = ["//", "/ "]
    print(sol.regionsBySlashes(grid))
