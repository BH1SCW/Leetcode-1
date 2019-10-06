from __future__ import annotations
# 么想到python也有浮点精读的问题啊。。
# 其实out的概率可以不计算
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        searched = {}
        def next(r, c):
            for ri in (1, -1):
                for ci in (1, -1):
                    for (mr, mc) in ((1, 2), (2, 1)):
                        yield r + mr*ri, c + mc*ci
        def dfs(k, r, c):
            if (k, r, c) in searched:
                return searched[k, r, c]
            if k == 0:
                return 1
            prob_in = 0
            for nr, nc in next(r, c):
                if 0 <= nr < N and 0 <= nc < N:
                    prob_in += dfs(k - 1, nr, nc) / 8
            searched[k, r, c] = prob_in
            return prob_in
        return dfs(K, r, c)

    def knightProbability2(self, N: int, K: int, r: int, c: int) -> float:
        searched = {}
        def next(r, c):
            for ri in (1, -1):
                for ci in (1, -1):
                    for (mr, mc) in ((1, 2), (2, 1)):
                        yield r + mr*ri, c + mc*ci
        def dfs(k, r, c):
            if (k, r, c) in searched:
                return searched[k, r, c]
            if k == 0:
                return 1, 0
            prob_in, prob_out = 0, 0
            for nr, nc in next(r, c):
                if 0 <= nr < N and 0 <= nc < N:
                    pi, po = dfs(k - 1, nr, nc)
                    prob_in, prob_out = prob_in + pi / 8, prob_out + po / 8
                else:
                    prob_out += 0.125
            searched[k, r, c] = (prob_in, prob_out)
            if prob_in + prob_out != 1:
                print(k, r, c, prob_in + prob_out)
            return prob_in, prob_out
        return dfs(K, r, c)[0]



if __name__ == '__main__':
    sol = Solution()
    graph = [8, 30, 0, 0]
    print(sol.knightProbability(*graph))
