from __future__ import annotations
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # memory usage beats 100%, time beats 38%.memory用的小是因为别人用的都是boxes，我用的是stats，这样的话，别人都是O(n^3)，我要
        # 略少一些，当然worst case是一样的。这个是从最近的contest上学来的，很有用。
        # 这道题其实也可以算是0-1背包问题，要么爆，要么和后面相同的一起爆，因为假如要和后面的一起爆，中间的边界条件就会减少很多，变得简单很多。
        stats = [(boxes[0], 1)]
        for i in range(1, len(boxes)):
            if boxes[i] == boxes[i - 1]:
                stats[-1] = (boxes[i], stats[-1][1] + 1)
            else:
                stats.append((boxes[i], 1))
        memo = [[[0] * len(boxes) for i in range(len(stats))] for j in range(len(stats))]
        def dfs(i, j, k):
            if i > j:
                return 0
            if memo[i][j][k] > 0:
                return memo[i][j][k]
            res = dfs(i + 1, j, 0) + (stats[i][1] + k) * (stats[i][1] + k) # 这个对i==j成立
            for m in range(i + 1, j + 1):
                if stats[m][0] == stats[i][0]:
                    res = max(res, dfs(i + 1, m - 1, 0) + dfs(m, j, k + stats[i][1]))
            memo[i][j][k] = res
            return res
        return dfs(0, len(stats) - 1, 0)


    # 这个可以解决问题，但是并不是最优的，明天看一下答案，这个可以说是最最暴力的解法了
    def removeBoxes2(self, boxes: List[int]) -> int:
        stats = [(boxes[0], 1)]
        for i in range(1, len(boxes)):
            if boxes[i] == boxes[i - 1]:
                stats[-1] = (boxes[i], stats[-1][1] + 1)
            else:
                stats.append((boxes[i], 1))
        searched = {}
        def helper(l):
            if not l:
                return 0
            key = tuple(l)
            if key in searched:
                return searched[key]
            m = helper(l[1:]) + l[0][1] * l[0][1]
            for i in range(1, len(l) - 1):
                if l[i - 1][0] == l[i + 1][0]:
                    res = helper(l[:i - 1] + [(l[i - 1][0], l[i - 1][1] + l[i + 1][1])] + l[i + 2:]) + l[i][1] * l[i][1]
                else:
                    res = helper(l[:i] + l[i + 1:]) + l[i][1] * l[i][1]
                m = res if res > m else m
            res = helper(l[:-1]) + l[-1][1] * l[-1][1]
            m = res if res > m else m
            searched[key] = m
            return m
        return helper(stats)

if __name__ == '__main__':
    sol = Solution()
    e = [2, 5, 10, 9, 4, 8, 6, 9, 9, 1]
    e = [1, 9, 4, 9, 9, 2]
    e = [2, 5, 10, 9, 4, 8, 6, 9, 9, 1]
    e = [9, 4, 8, 9, 9]
    e = [1, 3, 2, 2, 2, 3, 4, 3, 1]
    print(sol.removeBoxes(e))
